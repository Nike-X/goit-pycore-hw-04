This repo contains a few separate programs:
* total_salary.py: read salaries from file and calculate total. It uses read_parse.py to read from file and parse records
* get_cats_info.py: read cats' data from file return it as a list of dictionaries. It uses read_parse.py to read from file and parse records
* read_parse.py: provides aux function to read from file and parse records (and raise errors)
* dir_tree subdir: contains program that build directory tree (subdirs and files) for given root directory. IMPORTANT: create virtual env and install all dependencies from requirements.txt before launch. Run via CLI, provide root path
* assistant_bot subdir: assistant bot to save, change and show phone contacts via CLI. Run via CLI (interactive mode)
* test_data: few .txt files to test total_salary.py and get_cats_info.py
