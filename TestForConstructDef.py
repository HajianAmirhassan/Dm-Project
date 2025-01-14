def can_construct_with_all_used(binary_string, string_array):
    dp = [False] * (len(binary_string) + 1)
    dp[0] = True  # Empty string can always be constructed

    # Tracking usage of words in string_array
    used_words = [set() for _ in range(len(binary_string) + 1)]

    for i in range(1, len(binary_string) + 1):
        for word in string_array:
            if i >= len(word) and binary_string[i - len(word):i] == word and dp[i - len(word)]:
                dp[i] = True
                used_words[i] = used_words[i - len(word)].copy()
                used_words[i].add(word)

    # Check if the final construction includes all words
    return dp[-1] and set(string_array).issubset(used_words[-1])

# Example Usage
binary_string = "01110"
string_array = ["10", "011", "110"]

result = can_construct_with_all_used(binary_string, string_array)
print(result)  # Output: False (not all words are used)
