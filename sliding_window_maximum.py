
from collections import deque


def sliding_window_maximum(arr, k):
    # Deque to store indexes of elements
    deq = deque()
    result = []

    for i in range(len(arr)):
        # Remove elements out of the current window
        if deq and deq[0] == i - k:
            deq.popleft()

        # Remove elements that are smaller than the current element
        while deq and arr[deq[-1]] < arr[i]:
            deq.pop()

        deq.append(i)

        # Append the max element of the current window to result
        if i >= k - 1:
            result.append(arr[deq[0]])

    return result


def main():
    use_example = input("Do you want to use the example input? (y/n): ").lower()

    if use_example == 'y':
        # Example input
        arr = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
    elif use_example == 'n':
        arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
        k = int(input("Enter the window size (k): "))
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        return

    result = sliding_window_maximum(arr, k)
    print("Sliding window maximum:", result)


if __name__ == "__main__":
    main()
