import sys
import hashlib
import re

def remove_last_line_from_string(s):
    return s[:s.rfind('\n')]

# Function to calculate the SHA-256 hash of a string
def calculate_sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Function to calculate the SHA-256 hash of a file
def calculate_sha256_file(file_path):
    try:
        with open(file_path, 'rb') as original_file:
            data = original_file.read()
        return hashlib.sha256(data).hexdigest()
    except FileNotFoundError:
        return '-1'

def count_concatenated_zeros(s):
    count = 0
    for char in s:
        if char == '0':
            count += 1
        else:
            break  # Stop counting when a non-'0' character is encountered
    return count

def is_valid_line(input_string):
    # Split the string into lines
    lines = input_string.split('\n')

    # Check if there is at least one line
    if len(lines) < 1:
        return False

    # Get the last line
    last_line = lines[-1]

    # Define a regular expression pattern for the required format
    pattern = r'^[0-9a-f]{8}\t[0-9a-f]{2}\t100$'

    # Use regex to check if the last line matches the pattern
    if re.match(pattern, last_line):
        return True
    else:
        return False

def lab05A3(original_file_path, hash_file_path):
    # Read the content of the original file
    with open(original_file_path, 'rb') as original_file:
        content_original = original_file.read()

    # Read the content of the hash file
    with open(hash_file_path, 'rb') as hash_file:
        content_hash = hash_file.read()

    return (content_original.decode() == (remove_last_line_from_string(content_hash.decode()))) and (count_concatenated_zeros(calculate_sha256(content_hash.decode())) > 0) and is_valid_line(content_hash.decode())