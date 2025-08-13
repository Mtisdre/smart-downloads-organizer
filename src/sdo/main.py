#!/usr/bin/env python3
import argparse
import os
import shutil
from pathlib import Path
import yaml

CONFIG_PATH = Path(__file__).resolve().parents[2] / "config.yaml"
if not CONFIG_PATH.exists():
    raise FileNotFoundError(f"Config file not found: {CONFIG_PATH}")

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

DOWNLOADS_DIR = Path(config["DownloadsPath"])
FILE_TYPES = config["FileTypes"]

def organize_files():
    if not DOWNLOADS_DIR.exists():
        print(f"Downloads folder not found: {DOWNLOADS_DIR}")
        return

    files_moved = 0
    for file_path in DOWNLOADS_DIR.iterdir():
        if file_path.is_file():
            moved = False
            for category, extensions in FILE_TYPES.items():
                if file_path.suffix.lower() in extensions:
                    target_dir = DOWNLOADS_DIR / category
                    target_dir.mkdir(exist_ok=True)
                    shutil.move(str(file_path), str(target_dir / file_path.name))
                    files_moved += 1
                    moved = True
                    break

            if not moved:
                target_dir = DOWNLOADS_DIR / "Others"
                target_dir.mkdir(exist_ok=True)
                shutil.move(str(file_path), str(target_dir / file_path.name))
                files_moved += 1

    print(f"Organized {files_moved} files in {DOWNLOADS_DIR}")

def main():
    parser = argparse.ArgumentParser(
        description="Smart Downloads Organizer - Organize your Downloads folder easily."
    )

    parser.add_argument(
        "--organize",
        action="store_true",
        help="Organize the Downloads folder now."
    )

    args = parser.parse_args()

    if args.organize:
        organize_files()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
