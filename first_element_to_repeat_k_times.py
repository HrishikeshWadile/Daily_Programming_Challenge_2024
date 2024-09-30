
def first_element_to_repeat_k_times(arr, k):
    # Create a dictionary to store the frequency of each element
    frequency = {}

    # Traverse through the array and update frequencies
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    # Traverse through the array again to find the first element with frequency k
    for num in arr:
        if frequency[num] == k:
            return num

    # If no element appears exactly k times, return -1
    return -1


use_default = input("Do you want to use default values ([3, 1, 4, 4, 5, 2, 6, 1, 4]) and (k = 2)? (y/n): ").strip().lower()

if use_default == "n":
    arr = list(map(int, input("Enter the stack values separated by spaces: ").split()))
    k = int(input("Enter the value times to check (k): "))
else:
    arr = [3, 1, 4, 4, 5, 2, 6, 1, 4]
    k = 2

print(first_element_to_repeat_k_times(arr, k))  # Output: 1
