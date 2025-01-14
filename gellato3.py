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

def main():
    T = '0111011010111100'
    all_splits = split_binary(T)
    valid_splits = filter_valid_splits(all_splits)
    print(valid_splits)

if __name__ == '__main__':
    main()