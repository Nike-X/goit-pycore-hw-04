def read_raw_data(path, encoding='utf8'):
    # This function read file and return list of records, stripped of unnecessary characters
    # Function raises different exceptions if cannot read file correctly:
    # - OSError if file does not exist
    # - ValueError if file is empty or cannot be decoded

    # Try to read file line by line using context manager
    try:
        # Open file using with statement to ensure file always would be correctly closed
        with open(path, 'r', encoding=encoding) as fh:
            # Read file line by line
            raw_data = fh.readlines()
            
            # Strip unnecessary characters for each line
            records = [record.strip() for record in raw_data if record.strip()]
    
    # Raise error if file encoding is incompatible
    except UnicodeDecodeError as e:
        raise ValueError(f'Cannot decode file {path}, file encoding is not compatible with UTF-8') from e
    
    # Raise error for other causes (e.g., file does not exist)
    except OSError as e:
        raise OSError(f'Cannot read file from {path}, file is damaged or does not exist') from e

    # Raise error if file is empty
    if not records:
        raise ValueError(f'File {path} is empty')
    
    # Return read records
    return records

def parse_record(record: str, expected_fields: int, separator: str = ',') -> list[str]:
    # This function parses a separate record, splitting it by the specified 
    # separator and removing unnecessary characters.

    # Split record and strip it. '-1' because number of splits is always 
    # lesser than number of obtained fields (e.g., we split string 2 times and 
    # get 3 expected fields)
    fields = [f.strip() for f in record.strip().split(separator, expected_fields - 1)]

    # Raise error, if record does not splitted in expected number of fields
    if len(fields) < expected_fields:
        raise ValueError(f"Invalid record format: {record}")
    
    return fields