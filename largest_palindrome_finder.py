
def largest_palindrome_finder(word):
    substrings = []
    length = len(word)

    # Loop through each starting point of the substring
    for start in range(length):
        # Loop through each ending point of the substring
        for end in range(start + 1, length + 1):
            substrings.append(word[start:end])

    # Sort substrings by length in descending order
    substrings.sort(key=len, reverse=True)

    for substring in substrings:
        reverse = ""
        for i in substring:
            reverse = i + reverse
        if reverse == substring:
            return substring

    return word[0]


ans = input("Enter 'y' is you want to use 'babad' or enter 'n': ").lower()
if ans == 'y':
    largest_palindrome = largest_palindrome_finder("babad")
else:
    word_input = input("Enter the word: ")
    largest_palindrome = largest_palindrome_finder(word_input)
print(largest_palindrome)
