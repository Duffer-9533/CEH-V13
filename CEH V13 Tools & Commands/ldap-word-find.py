import re

def format_to_regex(format_str):
    regex = ''
    for char in format_str:
        if char == 'A':
            regex += '[A-Z]'  # Uppercase letter
        elif char == 'a':
            regex += '[a-z]'  # Lowercase letter
        elif char == 'N':
            regex += '[0-9]'  # Number
        elif char == 'S':
            regex += r'[!@#$%^&*()_+={}\[\]:;"\'<>,.?/\\|`~'  # Special characters
        else:
            regex += re.escape(char)  # for any literal characters like @, _, etc.
    return '^' + regex + '$'  # match entire line

def main():
    format_str = input("Enter the format (e.g., AaaaaaNNNNS): ")
    wordlist_path = input("Enter the path to the wordlist file: ")

    regex_pattern = format_to_regex(format_str)
    compiled_regex = re.compile(regex_pattern)

    print(f"\nMatching words for format '{format_str}':\n")
    try:
        with open(wordlist_path, 'r') as f:
            for line in f:
                word = line.strip()
                if compiled_regex.match(word):
                    print(word)
    except FileNotFoundError:
        print(f"File not found: {wordlist_path}")

if __name__ == "__main__":
    main()
