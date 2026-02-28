# Homework 6, Task 1: Create a function that read salaries from file and calculate total 
# and average salaries.

from read_parse import read_raw_data, parse_record

def total_salary(path):
    # We assume that each line in file is unique salary record, where 
    # employee name and salary value are separated by comma.

    # Prepare variable to sum each salary
    total = float(0)

    # Read salary records from file
    salary_records = read_raw_data(path)
    
    # Process each line from file in loop
    for record in salary_records:
        # Parse fields from each records
        name, salary = parse_record(record, expected_fields=2)
        # Convert salary value to float and add to total salary
        total = total + float(salary)
    
    # Calculate average salary and return tuple with total and average salaries
    average = total / len(salary_records)
    return (total, average)
