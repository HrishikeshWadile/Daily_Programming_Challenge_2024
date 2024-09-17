
def common_prefix(ex_list):
    if not ex_list:  # Check if the list is empty
        return ""

        # Start with the first string in the list as the base for comparison
    prefix = ex_list[0]

    # Loop over the remaining strings
    for item in ex_list[1:]:
        # Keep reducing the prefix until it matches the start of the current string
        while not item.startswith(prefix):
            prefix = prefix[:-1]  # Reduce the prefix one character at a time
            if prefix == "":  # If prefix becomes empty, no common prefix exists
                return ""

    return prefix


# Ask the user whether they want to use the predefined list or enter their own
choice = input("Do you want to use the example list (Y/N)? ").strip().lower()

if choice == 'y':
    # Use the predefined example list
    exa_list = ["flower", "flow", "flight"]
    print(f"Using the example list: {exa_list}")

else:
    # Let the user define their own list of words
    exa_list = input("Enter words separated by spaces: ").split()
    print(f"Using the user-defined list: {exa_list}")

# Calculate and display the common prefix
result = common_prefix(exa_list)
if result:
    print(f"Common prefix: {result}")
else:
    print("No common prefix found.")
