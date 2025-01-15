def validate_input():
    user_input = input("")
    if not all(char in {'0', '1'} for char in user_input):
        print("Invalid input.")
        return validate_input()
    return user_input

def calculate_x(n):
    result = 1
    for i in range(n):
        result *= (26 - i)
    return result if n > 0 else 0
def can_construct_dp(binary_string, string_array):
    dp = [False] * (len(binary_string) + 1)
    dp[0] = True  
    used_words = [set() for _ in range(len(binary_string) + 1)]
    for i in range(1, len(binary_string) + 1):
        for word in string_array:
            if i >= len(word) and binary_string[i - len(word):i] == word and dp[i - len(word)]:
                dp[i] = True
                used_words[i] = used_words[i - len(word)].copy()
                used_words[i].add(word)
    return dp[-1] and set(string_array).issubset(used_words[-1])

def generate_binary_strings(max_length):
    result = []
    for length in range(1, max_length + 1):
        for i in range(2 ** length):
            binary = bin(i)[2:].zfill(length)
            result.append(binary)
    return result

def is_prefix_free(codes):
    for code1 in codes:
        for code2 in codes:
            if code1 != code2 and (code1.startswith(code2) or code2.startswith(code1)):
                return False
    return True

def generate_binary_strings(max_length):
    result = []
    for length in range(1, max_length + 1):
        for i in range(2 ** length):
            binary = bin(i)[2:].zfill(length)
            result.append(binary)
    return result

def get_all_subsets(arr):
    n = len(arr)
    subsets = []
    for i in range(2 ** n):
        subset = set()
        for j in range(n):
            if (i & (1 << j)):
                subset.add(arr[j])
        if len(subset) > 0:
            subsets.append(subset)
    return subsets

def generate_huffman_codes(max_digits=3):
    binary_strings = generate_binary_strings(max_digits)
    all_subsets = get_all_subsets(binary_strings)
    valid_combinations = [subset for subset in all_subsets if is_prefix_free(subset)]
    return sorted(valid_combinations, key=lambda x: (len(x), sorted(x)))

def FindPossibleHoffmanSets(T):
    result = []
    prefix_free_sets = generate_huffman_codes(3)
    for set in prefix_free_sets:
        if can_construct_dp(T, list(set)):
            result.append(set)
    return result
input_string = validate_input()

valid_splits = FindPossibleHoffmanSets(input_string)
print(valid_splits)

lengths = [len(item) for item in valid_splits]
print(lengths)
total_sum = sum(calculate_x(length) for length in lengths)

print(len(lengths))
print(total_sum%1000000007)