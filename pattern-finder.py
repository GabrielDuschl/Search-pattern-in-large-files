#!/usr/bin/env python3

def search_pattern_in_file(file_path, pattern):
    red_color = "\033[91m"
    reset_color = "\033[0m"
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line_number, line in enumerate(file, start=1):
                if pattern in line:
                    highlighted_line = line.replace(pattern, f"{red_color}{pattern}{reset_color}")
                    print(f"Line {line_number}: {highlighted_line.strip()}")
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except IOError:
        print(f"An error occurred while reading the file {file_path}.")

if __name__ == "__main__":
    // change file name
    file_path = "rockyou2024.txt"
    pattern = input("Enter the pattern to search for: ")
    search_pattern_in_file(file_path, pattern)
