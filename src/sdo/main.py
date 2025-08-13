#!/usr/bin/env python3
import argparse

def organize_files():
    print("Organizing files... (MVP placeholder)")

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
