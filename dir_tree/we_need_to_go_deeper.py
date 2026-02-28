from pathlib import Path
from colorama import Fore

def we_need_to_go_deeper(root_path: Path, nesting_level: int, indent: str) -> None:
    # So, we get all items in provided directory (root_path), and sort them alphabetically
    items = sorted(root_path.iterdir(), key=lambda p: p.name.lower())

    # Process all found subdirs and files
    for item in items:
        # Set aprropriate padding for current nesting level
        padding = indent * nesting_level

        # If item is directory:
        if item.is_dir():
            # Print its name in cyan...
            print(padding + Fore.CYAN + item.name + '/' + Fore.RESET)
            # ... and we need to go deeper. Again.
            we_need_to_go_deeper(item, nesting_level + 1, indent)
        else:
            # If item is file, we just print its name in green
            print(padding + Fore.GREEN + item.name + Fore.RESET)
    return