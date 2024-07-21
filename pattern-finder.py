#!/usr/bin/env python3

def banner():
    print(r"""
,---,---,---,---,---,---,---,---,---,---,---,---,---,-------,
| ~ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | [ | ] | <-    |
|---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-----|
| ->| | " | , | . | P | Y | F | G | C | R | L | / | = |  \  |
|-----',--',--',--',--',--',--',--',--',--',--',--',--'-----|
| Caps | A | O | E | U | I | D | H | T | N | S | - |  Enter |
|------'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'--------|
|        | ; | Q | J | K | X | B | M | W | V | Z |          |
|------,-',--'--,'---'---'---'---'---'---'-,-'---',--,------|
| ctrl |  | alt |                          | alt  |  | ctrl |
'------'--'-----'--------------------------'------'--'------'

         get yourself a cup of coffee this might take a while... :)
    """)

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
    banner()
    # change file name
    file_path = "rockyou2024.txt"
    pattern = input("Enter the pattern to search for: ")
    search_pattern_in_file(file_path, pattern)
