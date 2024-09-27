
def postfix_evaluation(postfix_s):
    global result
    stack = []

    # Traverse the characters in the postfix expression
    for char in postfix_s:
        # If the character is a digit, push it to the stack
        if char.isdigit():
            stack.append(int(char))
        elif char == " ":
            pass
        else:
            # Pop the top two elements from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()

            # Perform the operation based on the operator
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2

            # Push the result back to the stack
            stack.append(result)

    # The final result will be the only element left in the stack
    return stack.pop()


# Taking input from user or using default values
use_default = input("Do you want to use default values (2 1 + 3 *)? (y/n): ").strip().lower()

if use_default == "n":
    postfix = input("Enter the first number: ")
else:
    postfix = "2 1 + 3 *"

lcm = postfix_evaluation(postfix)
print(f"Answer of ({postfix}) = {postfix_evaluation(postfix)}")
