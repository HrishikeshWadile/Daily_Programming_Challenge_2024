def reverse_stack(input_stack):
    # Base case: If stack is empty, return
    if not input_stack:
        return

    # Remove the top element
    top = input_stack.pop()

    # Reverse the remaining stack recursively
    reverse_stack(input_stack)

    # Insert the top element at the bottom of the reversed stack
    insert_at_bottom(input_stack, top)


def insert_at_bottom(input_stack, element):
    # Base case: If stack is empty, push the element at the bottom
    if not input_stack:
        input_stack.append(element)
        return

    # Remove the top element
    top = input_stack.pop()

    # Insert the element at the bottom of the stack
    insert_at_bottom(input_stack, element)

    # Push the removed element back
    input_stack.append(top)


use_default = input("Do you want to use default values ([3, 1, 4, 2])? (y/n): ").strip().lower()

if use_default == "n":
    stack = list(map(int, input("Enter the stack values separated by spaces: ").split()))
else:
    stack = [3, 1, 4, 2]

# Reverse the stack
reverse_stack(stack)

# Print the reversed stack
print(f"Reversed stack: {stack}")
