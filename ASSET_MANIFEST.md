# Asset Manifest

## OUI database

- Generated: 2026-09-22T02:39:19Z
- Source: https://standards-oui.ieee.org/oui/oui.csv
- CSV path: `oui.csv`
- Output: `sdcard/lab/ouilist.bin`
- Magic: `OUI1`
- Entries: 40202
- oui.csv SHA256: `99ba26f2ebb59b0b5c6511a7a77d5f8abbc85140549fab80dc00d89f19e8fba2`
- ouilist.bin SHA256: `4fb11677af953c1b1957e0c645cdcab54ecd94baa89cf09a20195e4443a3cda6`

Previous refresh: 2026-07-30T05:22:29Z (39856 entries)

## RFID key dictionary

- Refreshed: 2026-09-28
- Source selected: https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/refs/heads/master/client/dictionaries/mfc_default_keys.dic
- ChameleonUltraGUI source list: `DICTIONARY_SOURCES.md`
- SD path: `sdcard/lab/rfid/keys/mf_keys.dic`
- Non-comment key lines: 2511
- mf_keys.dic SHA256: `48e4c9a5748a00549119dace2c06895b9c97eed409da11efbedd2a046bdc545e`

Previous refresh: 2026-07-30 (2509 keys)


## Game-data asset

- Source: Freedoom Phase 1 v0.13.0, official release archive.
- Asset path: `sdcard/doom/doom1.wad`; runtime: `/sdcard/doom/doom1.wad`.
- WAD bytes: 28795076; lumps: 3163; header/directory/lump bounds verified.
- SHA256: `7323bcc168c5a45ff10749b339960e98314740a734c30d4b9f3337001f9e703d`.
- Full source/license/provenance: `sdcard/doom/README.md`, `PROVENANCE.json`, and adjacent Freedoom license/credits.
- Data redistribution only; WS-C5 prototype firmware remains unqualified and unpublished.

## Manual SD layout (v3.0.2 Development)

- Directory/seed inventory: `SD_LAYOUT.json`, matched to firmware `SD_ITEMS`.
- Missing runtime folders retained with zero-byte `.gitkeep` files.
- Missing seeds supplied as credential-free `.example` templates.
- Optional installer: `tools/install_sd.py`; existing files are never overwritten.
- Existing reference assets and dictionaries are unchanged.
