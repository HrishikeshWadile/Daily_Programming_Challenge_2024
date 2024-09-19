def group_anagrams(words):
    anagrams = {}  # Create a dictionary to hold anagrams

    for word in words:
        # Sort the word alphabetically and use it as the key
        sorted_word = ''.join(sorted(word))

        # If the sorted word is already a key, append the word to the value list
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    # Convert the dictionary values to a list of lists
    return list(anagrams.values())


# Example list
example_list = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Asking user for input
user_input = input("Enter words separated by spaces (or press Enter to use the example list): ")

if user_input.strip():  # If user provides input
    # Split the input into a list of words
    words = user_input.split()
else:  # If no input is provided, use the example list
    words = example_list

output = group_anagrams(words)
print(output)
