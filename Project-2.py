from typing import List, Set
def split_binary(s: str, max_len: int = 3) -> List[List[str]]:
    n = len(s)
    dp = [[] for _ in range(n + 1)]
    dp[n] = [[]] 
    for i in range(n - 1, -1, -1):
        for length in range(1, min(max_len + 1, n - i + 1)):
            substring = s[i:i + length]
            for rest in dp[i + length]:
                dp[i].append([substring] + rest)
    return dp[0]

def has_prefix_in_array(arr: List[str]) -> bool:
    arr_set = set(arr)
    for s in arr:
        for i in range(1, len(s)):
            if s[:i] in arr_set:
                return True
    return False

def filter_valid_splits(splits: List[List[str]]) -> List[Set[str]]:
    return [set(split) for split in splits if not has_prefix_in_array(split)]
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

input_string = validate_input()

all_splits = split_binary(input_string)
valid_splits = filter_valid_splits(all_splits)
valid_splits = [set(split) for split in valid_splits]

lengths = [len(item) for item in valid_splits]

total_sum = sum(calculate_x(length) for length in lengths)

print(len(lengths))
print(total_sum)