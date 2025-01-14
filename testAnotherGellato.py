def can_construct_dp(binary_string, string_array):
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

def is_prefix_free(codes):
    for i in range(len(codes)):
        for j in range(len(codes)):
            if i != j and codes[i].startswith(codes[j]):
                return False
    return True

def generate_binary_strings(max_length):
    result = []
    for length in range(1, max_length + 1):
        for i in range(2 ** length):
            binary = bin(i)[2:].zfill(length)
            result.append(binary)
    return result

def generate_combinations(arr, size):
    def backtrack(start, current_combination):
        if len(current_combination) == size:
            result.append(current_combination[:])
            return
        
        for i in range(start, len(arr)):
            current_combination.append(arr[i])
            backtrack(i + 1, current_combination)
            current_combination.pop()
    result = []
    backtrack(0, [])
    return result

def generate_huffman_codes(max_digits=3):
    binary_strings = generate_binary_strings(max_digits)
    valid_combinations = []
    for set_size in range(2, len(binary_strings) + 1):
        possible_combinations = generate_combinations(binary_strings, set_size)
        for combo in possible_combinations:
            if is_prefix_free(combo):
                valid_combinations.append(set(combo))
    
    return valid_combinations

def FindPossibleHoffmanSets(T):
    result = [{'0','1'}]
    prefix_free_sets = generate_huffman_codes(3)
    print(len(prefix_free_sets))
    prefix_free_sets.pop(0)
    for set in prefix_free_sets:
        if can_construct_dp(T, list(set)):
            result.append(set)
    print(result)

T = "01110"
FindPossibleHoffmanSets(T)