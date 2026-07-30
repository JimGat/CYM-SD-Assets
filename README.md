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

## Notes

- This repo must not contain private API keys, captured credentials, captured handshakes, wardrive logs, or personal card dumps.
- Use only in authorized lab, research, and owned-device environments.
