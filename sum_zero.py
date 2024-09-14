def find_zero_sum_subarrays(array):
    zero_sum_indices = []
    sum_dict = {}
    current_sum = 0

    for i in range(len(array)):
        current_sum += array[i]

        # If the current sum is zero, we found a subarray from index 0 to i
        if current_sum == 0:
            zero_sum_indices.append((0, i))

        # If the current sum has been seen before, it means we found a zero sum subarray
        if current_sum in sum_dict:
            # Find all subarrays that end at the current index
            for start_index in sum_dict[current_sum]:
                zero_sum_indices.append((start_index + 1, i))

        # Store the current sum with its corresponding index
        if current_sum not in sum_dict:
            sum_dict[current_sum] = []
        sum_dict[current_sum].append(i)

    return zero_sum_indices


def get_user_list():
    user_input = input("Enter your list of integers separated by spaces: ")
    return list(map(int, user_input.split()))


# Ask the user if they want to use the example list or input their own
choice = input("Do you want to use the example list [1, 2, -3, 3, -1, -2]? \nType 'y' or 'n': ").strip().lower()

if choice == 'y':
    arr = [1, 2, -3, 3, -1, -2]
else:
    arr = get_user_list()

# Find and display the zero-sum subarrays
result = find_zero_sum_subarrays(arr)
print("Subarrays with sum zero:", result)
