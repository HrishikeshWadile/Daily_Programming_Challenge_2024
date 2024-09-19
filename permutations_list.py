def permute(word):
    # Base case: if the word has only one character, return it as the only permutation
    if len(word) == 1:
        return [word]
    
    # Recursive case: get permutations of the word by removing one character at a time
    permutations = []
    for i in range(len(word)):
        # Take each character at position i
        char = word[i]
        # Get the remaining word after removing the current character
        remaining_word = word[:i] + word[i+1:]
        # Recursively find permutations of the remaining word
        for perm in permute(remaining_word):
            permutations.append(char + perm)
    
    return permutations

# Example default word
default_word = "abc"

# Ask user for input
user_input = input("Enter a word (or press Enter to use the default word 'abc'): ")

if user_input.strip():  # If the user provides input
    word = user_input
else:  # If no input is provided, use the default word
    word = default_word

# Generate permutations
result = permute(word)

# Output the result
print("Permutations of the word in a list:")
print(result)
