def sort_stack(input_stack):
    # Base case: If stack is empty, return
    if not input_stack:
        return

    # Remove the top element
    top = input_stack.pop()

    # Sort the remaining stack recursively
    sort_stack(input_stack)

    # Insert the top element back in the sorted stack
    insert_sorted(input_stack, top)


def insert_sorted(input_stack, element):
    # Base case: If stack is empty or the top element is less than or equal to the element
    if not input_stack or input_stack[-1] <= element:
        input_stack.append(element)
        return

    # Remove the top element
    top = input_stack.pop()

    # Insert the element in the sorted stack
    insert_sorted(input_stack, element)

    # Push the removed element back
    input_stack.append(top)


use_default = input("Do you want to use default values ([3, 1, 4, 2])? (y/n): ").strip().lower()

if use_default == "n":
    stack = list(map(int, input("Enter the stack values separated by spaces: ").split()))
else:
    stack = [3, 1, 4, 2]

# Sort the stack
sort_stack(stack)

# Print the sorted stack
print(f"Sorted stack: {stack}")
