# RFID Dictionary Sources

Jim pointed at GameTec-live/ChameleonUltraGUI as the source of truth for where the Chameleon Ultra GUI downloads dictionaries.

Inspected source file:

```text
https://github.com/GameTec-live/ChameleonUltraGUI/blob/main/chameleonultragui/lib/gui/menu/tools/dictionary_download.dart
```

The current GUI download menu lists these dictionary URLs:

| GUI label | URL | Verified |
|---|---|---|
| Proxmark3 (Mifare Classic) | https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/refs/heads/master/client/dictionaries/mfc_default_keys.dic | HTTP 200 |
| Proxmark3 (T55XX) | https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/refs/heads/master/client/dictionaries/t55xx_default_pwds.dic | HTTP 200 |
| Proxmark3 (Mifare Ultralight C) | https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/refs/heads/master/client/dictionaries/mfulc_default_keys.dic | HTTP 200 |
| Proxmark3 (Mifare Plus) | https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/refs/heads/master/client/dictionaries/mfp_default_keys.dic | HTTP 200 |
| Flipper Zero Unleashed Firmware (Mifare Classic) | https://raw.githubusercontent.com/DarkFlippers/unleashed-firmware/refs/heads/dev/applications/main/nfc/resources/nfc/assets/mf_classic_dict.nfc | HTTP 200 |

For CYM's requested SD placement, this repository installs the Proxmark3 Mifare Classic dictionary as:

```text
sdcard/lab/rfid/keys/mf_keys.dic
```

Refresh command:

```bash
curl -L https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/refs/heads/master/client/dictionaries/mfc_default_keys.dic \
  -o sdcard/lab/rfid/keys/mf_keys.dic
```
