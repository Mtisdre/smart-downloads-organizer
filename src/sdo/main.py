#!/usr/bin/env python3
import argparse
import os
import shutil
from pathlib import Path

# Kullanıcının Downloads klasörü yolu
DOWNLOADS_DIR = Path.home() / "Downloads"

# Kategorilere göre uzantı eşleşmeleri
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".wmv"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".json", ".xml", ".yml", ".yaml"],
    "Others": []
}

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
