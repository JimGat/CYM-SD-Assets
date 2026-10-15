#!/usr/bin/env python3
"""Install SD assets and blank templates without overwriting existing user files."""
from pathlib import Path
import argparse
import json
import shutil

def install(source, destination):
    source, destination = Path(source).resolve(), Path(destination).resolve()
    if destination == source or source in destination.parents:
        raise ValueError("Destination must be outside the source sdcard directory")
    destination.mkdir(parents=True, exist_ok=True)
    copied = preserved = 0
    entries = sorted(source.rglob("*"), key=lambda p: (p.name.endswith(".example"), str(p)))
    for path in entries:
        if path.is_symlink():
            continue
        relative = path.relative_to(source)
        if path.name == ".gitkeep":
            relative = relative.parent
        elif path.name.endswith(".example"):
            relative = relative.with_name(path.name[:-8])
        target = destination / relative
        if any(p.is_symlink() for p in [target, *target.parents] if p != destination and destination in p.parents):
            preserved += 1
            continue
        if path.is_dir() or path.name == ".gitkeep":
            target.mkdir(parents=True, exist_ok=True)
        elif target.exists() or target.is_symlink():
            preserved += 1
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            try:
                with path.open("rb") as src, target.open("xb") as dst:
                    shutil.copyfileobj(src, dst)
                copied += 1
            except FileExistsError:
                preserved += 1
    return {"copied": copied, "preserved": preserved}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="Mounted SD card root")
    args = parser.parse_args()
    result = install(Path(__file__).resolve().parents[1] / "sdcard", args.destination)
    print(json.dumps(result, sort_keys=True))
