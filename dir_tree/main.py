# Homework 6, Task 3: Create program to print directory tree for given path.
# Files and dirs are separated by colors:
# - dir names are cyan
# - file names are green
# Important. Before launch, ensure that you created and activated virtual environment and 
# installed all requirements from requirements.txt

import sys
from dir_tree import dir_tree

def main():
    # In this program, main() function only handles command-line calls. 
    # All application logic is contained in separate functions.
    
    # Check if user provided path as an argument when launch program via CLI
    if len(sys.argv) < 2:
        raise ValueError('Run as python main.py <path>')
    
    # Assign path to root directory/file from args
    path = sys.argv[1]

    # Call function to build directory tree. 'indent' specifies 
    # how indentation will be implemented to show directory nesting
    dir_tree(path, indent='    ')

# This code executes main() function if script is launched from command line
if __name__ == "__main__":
    main()