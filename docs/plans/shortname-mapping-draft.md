# Draft Pemetaan Shortname Entity — Divine Alignment

> Status: DRAFT untuk review owner (2026-11-27). Belum dieksekusi.
> Mekanisme: field opsional `slug` per entity (fallback = segmen terakhir ID).
> ID stabil TIDAK di-rename (public API contract); slug cuma dipakai untuk
> filename/URL output split. Title tetap tampil penuh di H1, TOC, dan label link.
> Aturan slug: lowercase-kebab, 1-3 kata, harus unik per module.

## Statistik

Total entity divine-alignment: 136. Terflag panjang (≥4 kata atau >24 char
di segmen terakhir ID): 55. Sisanya sudah pendek, slug otomatis = ID segmen
terakhir, tidak perlu entri.

## Warning: nama lokal duplikat antar container

Nama lokal ini muncul di lebih dari satu container (slug-nya sama, full ID
beda). Kalau URL pakai slug saja, harus di-scope per container path atau
diberi slug unik manual:

- `why-it-fails-on-aligned-kernel` (2 container case-study)
- `the-phenomenon` / `the-problem` / `technical-specification` / `protocol-rule`
  (pola generik, masing-masing 1 container tapi rawan dipakai lagi)
- `drift-timeline`, `profil-node`

Rekomendasi: URL final = `<container-slug>/<slug>`, jadi duplikat aman
selama slug unik dalam container-nya.

## Peta slug (per container)

### Container: prerequisite / section headers (artifact penanda bagian)

| Local ID (dipotong) | Slug usulan |
|---|---|
| prerequisite-axiom-0-foundation-layer-solid-qalb-nafs-iradah-qada-qadar | prereq-foundation |
| prerequisite-axiom-0-agency-layer-solid-paham-ownership-qadar-branching-alignment-recovery | prereq-agency |
| prerequisite-axiom-0-threat-model-layer-solid-paham-jin-bypass-signal-attribution-istidraj-mechanism | prereq-threat-model |
| prerequisite-axiom-0-all-previous-layers-solid-ini-adalah-integration-test | prereq-integration |

### Container: case-studies (Firaun, Umar, Istidraj)

| Local ID | Slug usulan |
|---|---|
| case-studies-firaun-umar-and-istidraj-drift-realignment-and-degradation-patterns (container) | firaun-umar-istidraj |
| istidraj-nikmat-as-alignment-test-vs-degradation-path | istidraj-test-vs-degradation |
| why-firaun-s-tobat-wasn-t-accepted | firaun-tobat-rejected |
| contrast-umar-bin-khattab | umar-contrast |
| firaun-as-diagnostic-tool | firaun-diagnostic |
| scenario-a-ujian-naik-tier-alignment | scenario-ujian-naik |
| scenario-b-istidraj-degradation-path | scenario-istidraj |
| drift-timeline | drift-timeline (sudah pendek, keep) |

### Container: secure-by-alignment

| Local ID | Slug usulan |
|---|---|
| kernel-level-immunity-why-deep-divine-alignment-is-intrinsically-unexploitable | kernel-immunity |
| introduction-from-defense-in-depth-to-secure-by-alignment | defense-to-alignment |
| cross-node-observation-layer-mismatch-as-frequency-detection | cross-node-observation |
| case-study-reward-centric-daawah-as-invalid-system-call | case-reward-daawah |
| case-study-social-media-as-non-existent-infrastructure | case-social-media |
| case-study-knowledge-holders-and-ujub-as-ujub-as-uncomputable / case-study-knowledge-holders-and-ujub-as-uncomputable | case-ujub-uncomputable |
| applied-principles-secure-by-alignment | applied-principles |

### Container: threat-model & attack vectors

| Local ID | Slug usulan |
|---|---|
| threat-model-alignment-attack-vectors (container) | threat-model (keep, sudah oke) |
| malaikat-as-network-security-alignment-logging | malaikat-security-logging |
| jin-exploit-sihir-collaborative-attack-model | jin-sihir-attack |
| istidraj-vs-ujian-alignment-decision-tree | istidraj-vs-ujian |
| istidraj-self-selected-degradation-path | istidraj-degradation |
| jin-bypass-direct-signal-injection | jin-bypass-injection |
| signal-attribution-protocol | signal-attribution (keep) |

### Container: agency-architecture (the alignment agent)

| Local ID | Slug usulan |
|---|---|
| agency-architecture-the-alignment-agent (container) | alignment-agent |
| manusia-as-authorized-executor-not-independent-actor | authorized-executor |
| boot-sequence-niat-as-alignment-activation-protocol | boot-sequence-niat |
| alignment-statement-vs-transactional-request | statement-vs-transaction |
| the-hold-out-vs-the-boot | hold-out-vs-boot |
| agency-vs-fatalisme | agency-vs-fatalisme (keep) |
| alignment-recovery-protocol | alignment-recovery (keep) |

### Container: operational-lifecycle (the alignment session)

| Local ID | Slug usulan |
|---|---|
| operational-lifecycle-the-alignment-session (container) | alignment-session |
| resource-management-time-bound-alignment-window | time-bound-window |
| termination-maut-final-state-commit | maut-final-commit |
| provisioning-rahim-token-injection | rahim-token-injection |
| runtime-life-alignment-maintenance | runtime-maintenance |

### Container: foundation

| Local ID | Slug usulan |
|---|---|
| entity-types-different-node-roles-in-alignment-network (container) | entity-types |
| manusia-primary-user-node-alignment-training-mode | manusia-user-node |
| jin-parallel-user-node-different-vessel | jin-user-node |
| malaikat-immutable-background-service | malaikat-service |
| hewan-alam-non-user-nodes | hewan-alam-nodes |
| cosmic-architecture-multi-tier-signal-network (container, muncul 2x: folder + entity) | cosmic-architecture |
| parallel-tiers-same-source-different-filter-configs | parallel-tiers |
| layer-stack | layer-stack (keep) |
| human-node-architecture-alignment-stack (container) | human-node-stack |
| qalb-transparency-index-the-alignment-meter | qalb-transparency-index |
| nafs-states-the-internal-noise-source | nafs-noise-source |
| qalb-alignment-rules | qalb-rules |
| the-llm-analogy-model-in-runtime | llm-analogy |
| operational-flow-the-alignment-pipeline | alignment-pipeline |
| component-mapping | component-mapping (keep) |
| the-alignment-stack | alignment-stack (keep) |
| core-philosophy-divine-alignment (container + entity) | core-philosophy |
| the-central-problem-is-ontological-read-through-axiom-0 | ontological-problem |
| lauhul-mahfuzh-as-alignment-map | lauhul-mahfuzh-map |

### Container: sleep & death / finalization

| Local ID | Slug usulan |
|---|---|
| sleep-death-alignment-finalization (container) | sleep-death-finalization |
| tidur-minor-death-temporary-alignment-state-suspension | tidur-suspension |
| maut-permanent-alignment-state-lock-in | maut-lock-in |
| tier-access-during-sleep | sleep-tier-access |
| integration-of-all-layers-into-terminal-alignment-state | terminal-alignment |
| sleep-and-death (section header) | sleep-and-death (keep) |

### Container: mitsaq alast

| Local ID | Slug usulan |
|---|---|
| mitsaq-alast-provisioning-handshake-record (container) | mitsaq-alast |
| dzikr-re-acknowledgment-terhadap-record-yang-sama | dzikr-re-acknowledgment |
| memory-semantics-config-bukan-episodic | memory-config-semantics |
| double-excuse-firewall-di-final-audit | double-excuse-firewall |
| fitrah-dapat-provenance-nya | fitrah-provenance |

### Container: axiom-zero leaves

| Local ID | Slug usulan |
|---|---|
| wujud-mumkin-disustain-bukan-dilaunch | wujud-mumkin |
| amr-sebagai-input-class-bukan-substance-transfer | amr-input-class |
| kasb-manusia-mengakses-kun-bukan-memiliki-kun | kasb-akses-kun |
| af-al-vs-dzat-kunci-baca-istilah-manifestasi | afal-vs-dzat |
| niyyah-sebagai-titik-kasb-bukan-action | niyyah-titik-kasb |
| ringkasan-cara-membaca-part-i-ix-melalui-axiom-ini | ringkasan-pembacaan |
| dua-kelas-wujud / implikasi-awal | keep (sudah pendek) |

### Container: drift detection & maintenance

| Local ID | Slug usulan |
|---|---|
| drift-detection-system-alignment-monitoring (container) | drift-monitoring |
| counter-drift-protocols-alignment-maintenance | counter-drift-protocols |
| drift-cascade-pattern / early-warning-signals | keep |
| drift-detection-system-alignment-monitoring (entity di drift-detection/) | drift-monitoring-sistem |
| alignment-maintenance-protocols (container + entity) | maintenance-protocols |
| tazkiyah-deep-alignment-remediation | tazkiyah-remediation |
| puasa-full-system-realignment-scan | puasa-realignment |
| transmutasi-fuel-redirect-protocol (container) | transmutasi-redirect |
| the-redirect-mechanism | redirect-mechanism |
| redirect-vs-deny | redirect-vs-deny (keep) |
| jamaah-alignment-mesh-network | jamaah-mesh |
| sholat-daily-alignment-sync | sholat-daily-sync |

### Container: qadar & qada

| Local ID | Slug usulan |
|---|---|
| qadar-qada-branching-alignment-logic (container) | qadar-qada-branching |
| node-config-mu-allaq-ports-and-realized-path | muallaq-ports |
| the-only-way-in-is-in | only-way-in |
| exact-sufficiency-protocol (container + entity) | exact-sufficiency |
| exact-sufficiency-vs-barakah | sufficiency-vs-barakah |
| the-10v-threshold | 10v-threshold |

### Container: translation protocol & misc

| Local ID | Slug usulan |
|---|---|
| translation-protocol-communicating-across-layer-gaps (container) | translation-protocol |
| the-superiority-encoding-rule | superiority-encoding |
| lossy-translation-warning | lossy-warning |
| the-protocol-stack | protocol-stack (keep) |
| the-problem | the-problem (keep, scope container) |
| authorized-exceptions-dalam-qadar | exceptions-dalam-qadar |
| applied-across-all-layers-practical-alignment-implementation | practical-implementation |
| advanced-understanding-the-boundaries-of-the-alignment-system | system-boundaries |
| key-principles-consolidated-refactored | key-principles |
| change-log-v3-1-v5-0-7 | change-log |
| glossary-axiom-0-terms | glossary-axiom-0 |
| validation-tag-legend | validation-legend |
| core-quotes-updated | core-quotes |
| dalil-references | dalil-references (keep) |
| why-ujub-is-uncomputable-on-aligned-kernel | ujub-uncomputable-kernel |
| why-it-fails-on-aligned-kernel (2x, beda container) | fails-on-aligned-kernel (scope container) |
| the-infrastructure-layer-drift | infrastructure-drift |
| the-phenomenon-layer-drift / the-trap-layer-drift | phenomenon-drift / trap-drift |
| the-ownerless-audit-revised | ownerless-audit |
| the-firaun-parallel-revisited | firaun-parallel |
| the-auto-routing-behavior | auto-routing |
| the-stateless-aligned-node | stateless-node |
| case-study-* (section headers) | keep |
| foundation/appendix/threat-model/case-studies/drift-detection/sleep-and-death/secure-by-alignment/agency-and-qadar/maintenance-and-sync/authorized-exceptions (section headers) | keep |
| axiom-zero (axiom container) | axiom-zero (keep) |
| divine-alignment (framework root) | divine-alignment (keep) |

## Catatan eksekusi (kalau disetujui)

1. Field `slug` belum ada di schema VDL — perlu ditambahkan dulu di
   `schema.vdl` + support di compiler split renderer (round 5 kecil di
   compiler, bisa digabung setelah round 4 beres).
2. Tanpa field slug, alternatif jangka pendek: rename ID via `vdl rename`
   (dry-run dulu). Tapi itu menyentuh public API contract — lebih baik
   slug field.
3. Setelah slug diisi: output split harus dicek ulang (jumlah halaman sama,
   link resolve, tidak ada hash suffix).
4. Human OS belum dipetakan — belum distandarisasi ke pola DA; slug-nya
   menyusul saat standarisasi.
