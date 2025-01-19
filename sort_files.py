import os
import asyncio
import aiofiles
from pathlib import Path
import argparse
import logging
from colorama import Fore, Style, init

# Initialize colorama for colored console output
init(autoreset=True)

# Logging configuration
logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s"
)


async def copy_file(src: Path, dest_folder: Path):
    """Asynchronous file copying to the appropriate folder by extension"""
    try:
        # Create a folder for files with this extension if it doesn't exist
        dest_folder.mkdir(parents=True, exist_ok=True)
        dest_path = dest_folder / src.name

        # Check if the file already exists in the target folder
        if dest_path.exists():
            print(Fore.YELLOW + f"[SKIP] File {src} already exists in {dest_folder}")
            return

        # Perform asynchronous file copying
        async with aiofiles.open(src, "rb") as src_file:
            async with aiofiles.open(dest_path, "wb") as dest_file:
                while chunk := await src_file.read(1024):
                    await dest_file.write(chunk)

        print(Fore.GREEN + f"[INFO] File {src} copied to {dest_folder}")

    except Exception as e:
        logging.error(f"Error copying file {src} to {dest_folder}: {e}")


async def read_folder(source_folder: Path, output_folder: Path):
    """Asynchronously read the source folder and copy files to the target folder"""
    try:
        # Iterate over all files in the source folder
        for entry in os.scandir(source_folder):
            if entry.is_file():
                # Determine the target folder based on the file extension
                ext = entry.name.split(".")[-1]
                dest_folder = output_folder / ext
                await copy_file(Path(entry.path), dest_folder)
            elif entry.is_dir():
                # Recursively process subfolders
                await read_folder(Path(entry.path), output_folder)

    except Exception as e:
        logging.error(f"Error reading folder {source_folder}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Sort files by extension")
    parser.add_argument("--source", required=True, help="Source folder")
    parser.add_argument("--output", required=True, help="Output folder")
    args = parser.parse_args()

    source_folder = Path(args.source)
    output_folder = Path(args.output)

    if not source_folder.exists():
        print(Fore.RED + f"[ERROR] Source folder {source_folder} does not exist")
        return

    if not output_folder.exists():
        print(Fore.YELLOW + f"[INFO] Creating target folder {output_folder}")
        output_folder.mkdir(parents=True)

    # Run the asynchronous function to sort files
    asyncio.run(read_folder(source_folder, output_folder))
    print(Fore.CYAN + "[DONE] All files processed")


if __name__ == "__main__":
    main()