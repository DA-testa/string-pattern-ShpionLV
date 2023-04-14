# python3

import os


def read_input():
    input_type = input("Enter input type (I for user input, F for file input): ").strip().lower()

    if input_type == 'i':
        pattern = input("Enter pattern: ").strip()
        text = input("Enter text: ").strip()
        return pattern, text
    elif input_type == 'f':
        filename = input("Enter file name: ").strip()
        if not filename.endswith(".txt"):
            raise ValueError("Invalid file format")
        if not os.path.isfile(filename):
            raise ValueError("File not found")
        with open(filename) as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
            return pattern, text
    else:
        raise ValueError("Invalid input type")


def print_occurrences(occurrences):
    if not occurrences:
        print("No occurrences found")
    else:
        print("Occurrences found at positions:", *occurrences)


def rabin_karp(pattern, text):
    prime = 101
    base = 256

    pattern_hash = 0
    text_hash = 0
    for i in range(len(pattern)):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % prime
        text_hash = (text_hash * base + ord(text[i])) % prime

    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash and pattern == text[i:i+len(pattern)]:
            occurrences.append(i)
        if i < len(text) - len(pattern):
            text_hash = ((text_hash - ord(text[i]) * (base**(len(pattern)-1))) * base + ord(text[i+len(pattern)])) % prime

    return occurrences


if __name__ == '__main__':
    try:
        pattern, text = read_input()
        occurrences = rabin_karp(pattern, text)
        print_occurrences(occurrences)
    except ValueError as e:
        print("Error:", e)


