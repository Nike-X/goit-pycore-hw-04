from pathlib import Path
from colorama import Fore
from we_need_to_go_deeper import we_need_to_go_deeper

def dir_tree(path: Path, indent='    '):
    # Create Path object from string
    root_path = Path(path)

    # Check if provided path exists
    if not root_path.exists():
        # Return error message in red color
        print(Fore.RED + f'{root_path} not found' + Fore.RESET)
        return

    # Print root name in cyan
    print(Fore.CYAN + root_path.name + '/' + Fore.RESET)

    # If root is directory... we need to go deeper
    # And transfer our root path and indent, of course
    if root_path.is_dir():
        we_need_to_go_deeper(root_path, nesting_level=1, indent=indent)
    return