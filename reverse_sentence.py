
def reverse_sentence(sentence):
    sent_list = sentence.split(" ")  # Split the sentence into words
    rev_list = []  # Initialize an empty list to store reversed words
    rev_sent = ""  # Initialize an empty string to store the final reversed sentence

    # Insert each word at the beginning of rev_list to reverse the order
    for item in sent_list:
        rev_list.insert(0, item)

    # Join the reversed words with a space between them
    rev_sent = " ".join(rev_list)

    return rev_sent


choice = input("Do you want to use the example string (Y/N)? ").strip().lower()

if choice == 'y':
    # Use the predefined example list
    ex_str = "the sky is blue"
    print(f"Using the example string: {ex_str}")

else:
    # Let the user define their own list
    ex_str = input("Enter the example string: ")
    print(f"Using the user-defined string: {ex_str}")

# Calculate and display the total water trapped
reverse = reverse_sentence(ex_str)
print(f"Reversed string: {reverse}")
