# Game-data asset for the WS-C5 prototype

`doom1.wad` is **Freedoom Phase 1, version 0.13.0**, not the commercial id Software Doom IWAD and not a shareware copy. Its bytes are unchanged; only the filename is adapted to the prototype's fixed lookup path.

Copy the contents of this repository's `sdcard/` directory to the FAT32 SD-card root. The game-data file must be at `doom/doom1.wad` on the card, mounted by CYM as `/sdcard/doom/doom1.wad`. Keep the adjacent copyright/license and contributor files with it.

This is game data only, not a firmware release or a claim that the prototype works on hardware. The current private integration targets Waveshare WS-C5-28 and WS-C5-35; builds for those two targets remain unresolved. The prototype validates the exact official Phase 1 digest before starting; a different WAD is not interchangeable just because it has the same filename. Physical memory/display/touch/launch-exit qualification is pending. No audio promise.

Source: https://github.com/freedoom/freedoom/releases/tag/v0.13.0
Archive: https://github.com/freedoom/freedoom/releases/download/v0.13.0/freedoom-0.13.0.zip
Official published checksum: https://github.com/freedoom/freedoom/releases/download/v0.13.0/freedoom-0.13.0-CHECKSUM
Archive SHA256: `3f9b264f3e3ce503b4fb7f6bdcb1f419d93c7b546f4df3e874dd878db9688f59`
WAD SHA256: `7323bcc168c5a45ff10749b339960e98314740a734c30d4b9f3337001f9e703d`

Redistribution is under the Freedoom three-clause BSD-style terms reproduced byte-for-byte in `COPYING-FREEDOOM.txt`. Preserve the notice/disclaimer and do not imply project/contributor endorsement. Engine licensing is separate (GPL); this asset does not relicense any engine or CYM source. The upstream PGP-signed checksum was fetched over HTTPS and its digest matched; no PGP signer-key validation is claimed.
