# CYM-NM28C5 SD Assets

Public SD-card asset pack for JimGat/CYM-NM28C5 (Cheap Yellow Monster).

This repository is intentionally separate from the firmware repository so SD-card
assets and third-party dictionary content can be managed independently.

## Install on SD card

Format a MicroSD card as FAT32 (32 GB or smaller), then copy the contents of
`sdcard/` to the card root. The resulting layout starts with:

```text
/sdcard/
└── lab/
    ├── ouilist.bin
    ├── ble/blueduck/scripts/*.duck
    ├── htmls/basic_portal.html
    └── rfid/keys/mf_keys.dic
```

## Manual setup for devices without PSRAM

CYM v3.0.2 Development skips automatic Validate & Provision when no usable PSRAM
is registered. This applies to every board, including Classic CYD and HackerBox.
Press OK to continue booting or return to the SD Card menu; no files are changed.
Format + Provision is also unavailable on these devices. Format on a computer instead.

1. Back up an existing card. For a new card, prepare FAT32 on your computer.
2. Download this repository with **Code > Download ZIP** and extract it.
3. Copy the **contents** of `sdcard/` to the card root. The card should contain
   `lab/`, not another `sdcard/` directory. Keep the complete directory structure.
4. When copying onto an existing card, **skip existing files**; do not replace
   credentials, configuration, captures or saves with templates.
5. On a new card, copy each `*.example` template to the same folder without the
   `.example` suffix. Never replace an existing file. API-key templates contain
   no credentials; edit only your private SD-card copy and never commit keys.
6. Safely eject the card, insert it in CYM and boot. Missing optional resources
   are not magically validated by dismissing the PSRAM warning.

Alternatively, Python 3 can perform steps 3-5 without overwriting existing files.
From the extracted repository folder, replace the example path with the actual
mounted card root:

```sh
python3 tools/install_sd.py "/media/YOUR_USER/YOUR_SD_CARD"
```

Windows example (replace E: with the SD card drive):

```powershell
py tools/install_sd.py "E:/"
```

The command reports JSON `copied` and `preserved` counts. A second run preserves
all existing files. It does not format a card, flash firmware or write keys.
`SD_LAYOUT.json` inventories the required firmware directories and seed filenames.
Empty directories have zero-byte `.gitkeep` files so GitHub ZIP downloads retain
all folders. The installer creates those folders without copying the placeholders.

## Included assets

- `sdcard/lab/ouilist.bin` — generated OUI vendor table for CYM BLE vendor lookup.
- `sdcard/lab/rfid/keys/mf_keys.dic` — MIFARE Classic default-key dictionary, copied from the RfidResearchGroup Proxmark3 default key dictionary for CYM SD placement.
- `sdcard/lab/ble/blueduck/scripts/*.duck` — CYM BlueDuck demo scripts from the firmware repository.
- `sdcard/lab/htmls/basic_portal.html` — minimal captive portal template for authorized lab use.
- `*.example` files — templates only; do not rename and commit real API keys or captured data.

Generated/captured runtime output directories are included with `.gitkeep` so the
SD tree is visible, but live captures, credentials, tokens, wardrive logs, and card
saves are ignored by `.gitignore`.

## Refresh OUI vendor database

The CYM README currently points to the IEEE MA-L CSV URL:

```text
https://standards-oui.ieee.org/oui/oui.csv
```

Refresh with:

```bash
curl -L https://standards-oui.ieee.org/oui/oui.csv -o oui.csv
python tools/oui_convert.py oui.csv sdcard/lab/ouilist.bin
```

The converter writes the CYM binary format:

- magic: `OUI1`
- uint32 little-endian entry count
- sorted 32-byte records: 3 OUI bytes + 29-byte null-padded vendor string

## Refresh RFID dictionary

CYM wiki reference:

- NFC/RFID wiki: `mf_keys.dic` lives at `/sdcard/lab/rfid/keys/mf_keys.dic`, one 12-hex-character key per line, `#` comments ignored.
- CYM Home wiki: the SD Asset Repository is the pre-built source for the OUI vendor table and extended MIFARE key dictionary.

Source used for `mf_keys.dic`:

```text
https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/refs/heads/master/client/dictionaries/mfc_default_keys.dic
```

Refresh with:

```bash
curl -L https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/refs/heads/master/client/dictionaries/mfc_default_keys.dic \
  -o sdcard/lab/rfid/keys/mf_keys.dic
```

The ChameleonUltraGUI download menu points to these dictionary download locations:

| Dictionary | Download URL |
|---|---|
| Proxmark3 Mifare Classic | https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/refs/heads/master/client/dictionaries/mfc_default_keys.dic |
| Proxmark3 T55XX | https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/refs/heads/master/client/dictionaries/t55xx_default_pwds.dic |
| Proxmark3 Mifare Ultralight C | https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/refs/heads/master/client/dictionaries/mfulc_default_keys.dic |
| Proxmark3 Mifare Plus | https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/refs/heads/master/client/dictionaries/mfp_default_keys.dic |
| Flipper Zero Unleashed Mifare Classic | https://raw.githubusercontent.com/DarkFlippers/unleashed-firmware/refs/heads/dev/applications/main/nfc/resources/nfc/assets/mf_classic_dict.nfc |

See `DICTIONARY_SOURCES.md` for the ChameleonUltraGUI source-file reference and
verified URL notes.

## Contributing

This repo is deliberately kept separate from the main [CYM-NM28C5 firmware repo](https://github.com/JimGat/CYM) so SD-card assets can evolve on their own schedule, with a lower bar for contribution than firmware code. If you've got something that would help other CYM users, a PR here is very welcome:

- **New or better dictionaries** — RFID/NFC key lists, wordlists, or other lookup tables useful to a CYM feature.
- **Refreshed data** — the OUI vendor table and MIFARE key dictionary both go stale as new devices/keys are published; a PR that reruns the refresh steps above (with an updated `ASSET_MANIFEST.md` entry) is genuinely useful even without any code changes.
- **New asset categories** — if a CYM feature could use a bundled reference file that doesn't belong in firmware (e.g. a new vendor/manufacturer table, a protocol signature list), open an issue first to discuss the shape before a large PR.
- **Fixes** — corrections to install paths, broken source URLs, or SD directory layout.

A few ground rules, matching the Notes below: no private keys/credentials/captures in any PR, and please note the source/license of any third-party data you add (see `DICTIONARY_SOURCES.md` for the existing pattern). Small, well-sourced PRs are easiest to review and merge quickly.

For questions or to discuss a larger contribution first, the [LAB5 Discord](https://discord.gg/Vuq2SmCbk5) has a CYM thread, or open an issue here.

## Notes

- This repo must not contain private API keys, captured credentials, captured handshakes, wardrive logs, or personal card dumps.
- Use only in authorized lab, research, and owned-device environments.
