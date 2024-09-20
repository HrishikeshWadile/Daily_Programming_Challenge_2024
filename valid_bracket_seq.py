def is_valid_bracket_sequence(example: str) -> bool:
    # Stack to keep track of opening brackets
    stack = []

    # Dictionary to match corresponding closing and opening brackets
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    # Loop through each character in the string
    for char in example:
        if char in bracket_pairs.values():
            # If it's an opening bracket, push to stack
            stack.append(char)
        elif char in bracket_pairs.keys():
            # If it's a closing bracket, check if the stack is not empty and matches the top of the stack
            if stack and stack[-1] == bracket_pairs[char]:
                stack.pop()
            else:
                return False
        # Ignore any non-bracket characters like letters, spaces, etc.
        else:
            continue

    # If the stack is empty at the end, the brackets are balanced
    return len(stack) == 0


# Ask the user if they want to use example input or provide their own
choice = input("Do you want to use example input '[{()}]'? (yes/no): ").strip().lower()

if choice == "yes":
    # Use example input
    s = "[{()}]"
else:
    # User-defined input
    s = input("Enter a string of brackets to validate: ").strip()

print(is_valid_bracket_sequence(s))
