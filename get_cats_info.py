# Homework 6, Task 2: Create a function that read cats data from file and return it as 
# a list of dictionaries.

from read_parse import read_raw_data, parse_record

def get_cats_info(path):
    # Create empty list for cats' data
    cats_info = []
    
    # Read cats records from file
    cats_records = read_raw_data(path)
    
    for cat in cats_records:
        # Parse fields from each records
        id, name, age = parse_record(cat, expected_fields=3)
        # For each cat, format its data as separate dictionary and add dict to list
        cats_info.append({'id': id, 'name': name, 'age': age})
    return cats_info