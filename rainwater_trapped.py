
def calculate_water_trapped(heights):
    if not heights:  # Edge case if heights list is empty
        return 0

    n = len(heights)

    # Arrays to store the maximum height to the left and right of each bar
    left_max = [0] * n
    right_max = [0] * n

    # Fill left_max array
    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    # Fill right_max array
    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    # Calculate the water trapped
    water_trapped = 0
    for i in range(n):
        # Water trapped on top of the current bar is the difference between the minimum
        # of left and right max heights and the height of the current bar
        water_trapped += min(left_max[i], right_max[i]) - heights[i]

    return water_trapped


# Ask the user if they want to use the example list or input their own
choice = input("Do you want to use the example list (Y/N)? ").strip().lower()

if choice == 'y':
    # Use the predefined example list
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"Using the example list: {heights}")

else:
    # Let the user define their own list
    heights = input("Enter the heights of the bars as a list of integers (e.g., 0,1,2,0,1,3,4,0,0): ")
    heights = list(map(int, heights.split(',')))  # Convert the string input to a list of integers
    print(f"Using the user-defined list: {heights}")

# Calculate and display the total water trapped
water = calculate_water_trapped(heights)
print(f"Total water trapped: {water} units")
