#!/usr/bin/env python3
"""Fetch evidence, not verification verdicts. Stdlib only.
Usage: python vdl/tools/dalil-fetch.py quran 2:117 50:15 2:7
       python vdl/tools/dalil-fetch.py hadith bukhari:773 muslim:2653
Quran: .raw.json + .txt and separate .tafsir.raw.json + .tafsir.txt.
Hadith: .raw.html + .txt (HTML is not verbatim JSON).
Raw files preserve bytes. Extracts retain whitespace and punctuation.
Tafsir tags are removed. Hadith text nodes decode HTML entities without
inserting whitespace. Section delimiters are not part of source text.
Exit codes: 0 all OK, 1 any coordinate failed, 2 CLI usage error.
"""
import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import ipaddress
import json
from pathlib import Path
import re
import socket
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

API = "https://api.quran.com/api/v4"
ALLOWED_HOSTS = {"api.quran.com", "sunnah.com"}
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
VOID = set("area base br col embed hr img input link meta param source track wbr".split())

class FetchError(Exception):
    pass

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise HTTPError(newurl, code, "redirect blocked (SSRF guard)", headers, fp)

OPENER = build_opener(NoRedirect)

def guard(url):
    parts = urlsplit(url)
    if parts.scheme != "https":
        raise FetchError(f"SSRF_GUARD scheme not https: {parts.scheme}")
    if parts.hostname not in ALLOWED_HOSTS or parts.port not in (None, 443):
        raise FetchError(f"SSRF_GUARD host not pinned: {parts.hostname}:{parts.port}")
    if parts.username or parts.password:
        raise FetchError("SSRF_GUARD userinfo in URL")
    for _, _, _, _, sockaddr in socket.getaddrinfo(parts.hostname, 443, type=socket.SOCK_STREAM):
        ip = ipaddress.ip_address(sockaddr[0])
        if not ip.is_global:
            raise FetchError(f"SSRF_GUARD non-public resolved IP: {ip}")

def say(value):
    print(str(value).encode("ascii", "backslashreplace").decode("ascii"), flush=True)

def write(path, value):
    with path.open("w", encoding="utf-8", newline="") as stream:
        stream.write(value)

def fetch(url, raw, timeout):
    guard(url)
    try:
        request = Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
        with OPENER.open(request, timeout=timeout) as response:
            status, body = response.status, response.read()
    except HTTPError as exc:
        status, body = exc.code, exc.read()
    except (URLError, OSError) as exc:
        raise FetchError(f"URL={url}\nHTTP_STATUS=unavailable\nNETWORK_ERROR={exc}") from exc
    raw.write_bytes(body)
    if status != 200:
        raise FetchError(f"URL={url}\nHTTP_STATUS={status}\nRAW={raw}\n"
                         f"RESPONSE_SNIPPET={body[:2000].decode('utf-8', 'replace')}")
    return body

def fetch_json(url, raw, timeout):
    body = fetch(url, raw, timeout)
    try:
        return json.loads(body)
    except (ValueError, UnicodeError) as exc:
        raise FetchError(f"URL={url}\nHTTP_STATUS=200\nINVALID_JSON={exc}\nRAW={raw}\n"
                         f"RESPONSE_SNIPPET={body[:2000].decode('utf-8', 'replace')}") from exc

def text(value):
    if not isinstance(value, str) or not value or value.isspace():
        raise ValueError("Expected nonempty text field")
    return value

def section(label, value):
    return f"--- BEGIN {label} ---\n" + value + f"\n--- END {label} ---\n"

def quran(coord, stem, out, timeout):
    errors = []
    sources = [("verse", f"{API}/verses/by_key/{coord}?fields=text_uthmani&translations=33", ""),
               ("tafsir", f"{API}/tafsirs/16/by_ayah/{coord}", ".tafsir")]
    for kind, url, suffix in sources:
        raw = out / (stem + suffix + ".raw.json")
        try:
            data = fetch_json(url, raw, timeout)
            result = f"COORDINATE={coord}\nURL={url}\nRAW={raw}\n"
            if kind == "verse":
                verse = data["verse"]
                if verse["verse_key"] != coord:
                    raise ValueError("verse_key mismatch")
                translation = verse["translations"][0]
                if translation["resource_id"] != 33:
                    raise ValueError("Translation resource_id mismatch")
                result += section("TEXT_UTHMANI", text(verse["text_uthmani"]))
                result += section("TRANSLATION_RESOURCE_33", text(translation["text"]))
            else:
                tafsir = data["tafsir"]
                if tafsir["resource_id"] != 16 or coord not in tafsir["verses"]:
                    raise ValueError("Tafsir resource or verse coverage mismatch")
                value = re.sub(r"<[^>]*>", "", text(tafsir["text"]))
                result += section("TAFSIR_MUYASSAR_RESOURCE_16", text(value))
            write(out / (stem + suffix + ".txt"), result)
        except (FetchError, KeyError, IndexError, TypeError, ValueError) as exc:
            if not isinstance(exc, FetchError):
                exc = FetchError(f"HTTP_STATUS=200\nRAW={raw}\nSCHEMA_ERROR={exc}")
            errors.append(f"SOURCE={kind}\nURL={url}\nERROR={exc}")
    if errors:
        raise FetchError("\n\n".join(errors))

class HadithParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.active = [], []
        self.blocks = {"arabic_text_details": [], "arab": [], "english_hadith_full": []}

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            return
        self.stack.append(tag)
        classes = dict(attrs).get("class", "").split()
        for key in self.blocks:
            if key in classes:
                block = []
                self.blocks[key].append(block)
                self.active.append((len(self.stack), block))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag not in self.stack:
            return
        index = len(self.stack) - 1 - self.stack[::-1].index(tag)
        self.active = [(d, b) for d, b in self.active if d <= index]
        del self.stack[index:]

    def handle_data(self, data):
        for _, block in self.active:
            block.append(data)

    def texts(self, key):
        return ["".join(block) for block in self.blocks[key]]

def hadith(coord, stem, out, timeout):
    url = f"https://sunnah.com/{coord}"
    raw = out / (stem + ".raw.html")
    parser = HadithParser()
    parser.feed(fetch(url, raw, timeout).decode("utf-8"))
    parser.close()
    arabic = parser.texts("arabic_text_details") or parser.texts("arab")
    english = parser.texts("english_hadith_full")
    if not arabic or not english:
        raise FetchError(f"URL={url}\nHTTP_STATUS=200\nRAW={raw}\n"
                         "HTML_SHAPE_ERROR=Arabic or English block missing; possible challenge page")
    result = f"COORDINATE={coord}\nURL={url}\nRAW={raw}\n"
    for label, blocks in [("ARABIC", arabic), ("ENGLISH", english)]:
        for index, value in enumerate(blocks, 1):
            result += section(f"{label}_BLOCK_{index}", text(value))
    write(out / (stem + ".txt"), result)

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("kind", choices=["quran", "hadith"])
    parser.add_argument("coordinates", nargs="+")
    parser.add_argument("--output", type=Path, help="New output directory; must not exist")
    parser.add_argument("--timeout", type=float, default=40)
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("--timeout must be positive")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    out = args.output or Path(__file__).resolve().parents[2] / ".scratch" / "dalil" / stamp
    try:
        out.mkdir(parents=True, exist_ok=False)
    except OSError as exc:
        parser.error(ascii(str(exc)))
    say(f"OUTPUT={out.resolve()}")
    failed = 0
    pattern = r"[0-9]+:[0-9]+" if args.kind == "quran" else r"[a-z][a-z0-9_-]*:[0-9]+[a-z]?"
    for index, coord in enumerate(dict.fromkeys(args.coordinates), 1):
        valid = re.fullmatch(pattern, coord) is not None
        stem = coord.replace(":", "-") if valid else f"invalid-{index}"
        try:
            if not valid:
                raise FetchError(f"INVALID_COORDINATE={coord!r}")
            (quran if args.kind == "quran" else hadith)(coord, stem, out, args.timeout)
            say(f"OK {coord} EXTRACT={out / (stem + '.txt')}")
            if args.kind == "quran":
                say(f"  TAFSIR={out / (stem + '.tafsir.txt')}")
        except (FetchError, OSError, ValueError) as exc:
            failed += 1
            error = out / (stem + ".error")
            try:
                write(error, f"KIND={args.kind}\nCOORDINATE={coord}\n{exc}\n")
            except OSError as write_error:
                say(f"ERROR {coord} CANNOT_WRITE_ERROR={write_error}")
            say(f"ERROR {coord} DETAIL={error}")
    say(f"SUMMARY total={len(set(args.coordinates))} failed={failed} output={out.resolve()}")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
