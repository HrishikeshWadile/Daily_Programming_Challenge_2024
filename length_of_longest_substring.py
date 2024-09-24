def length_of_longest_substring(s: str) -> int:
    # Dictionary to store the last positions of occurrence
    char_map = {}
    # Initialize the starting point of the current window
    start = 0
    # Result variable to store the maximum length
    max_length = 0

    for i, char in enumerate(s):
        # If the character is found in the dictionary and is within the current window
        if char in char_map and char_map[char] >= start:
            # Move the start to one position ahead of the last occurrence of the current character
            start = char_map[char] + 1

        # Update the last seen index of the character
        char_map[char] = i
        # Update the result if we get a larger window
        max_length = max(max_length, i - start + 1)

    return max_length


# Ask the user if they want to use example input or provide their own
choice = input("Do you want to use example input 'abcabcbb'? (y/n): ").strip().lower()

if choice == "y":
    # Example input
    example = "abcabcbb"
else:
    # User-defined input
    example = input("Enter a string: ")
print("Length of the longest substring without repeating characters:", length_of_longest_substring(example))
