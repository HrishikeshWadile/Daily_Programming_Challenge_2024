
def count_substrings_with_exactly_k_distinct(s_, _k_):
    def at_most_k_distinct(k_):
        char_map = {}
        left = 0
        count = 0

        for right in range(len(s_)):
            char_map[s_[right]] = char_map.get(s_[right], 0) + 1

            while len(char_map) > k_:
                char_map[s_[left]] -= 1
                if char_map[s_[left]] == 0:
                    del char_map[s_[left]]
                left += 1

            count += right - left + 1

        return count

    # The number of substrings with exactly k distinct characters is
    # the difference between those with at most k and at most k-1.
    return at_most_k_distinct(_k_) - at_most_k_distinct(_k_ - 1)


# Ask the user if they want to use example input or provide their own
choice = input("Do you want to use example input 'pqpqs'? (yes/no): ").strip().lower()

if choice == "yes":
    # Example input
    s = "pqpqs"
    k = 2
else:
    # User-defined input
    s = input("Enter a string: ")
    k = int(input("Enter the number of distinct characters you want: "))
print(count_substrings_with_exactly_k_distinct(s, k))
