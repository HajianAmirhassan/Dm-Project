from typing import List, Set

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

def can_construct_dp(binary_string: str, string_array: List[str]) -> bool:
    dp = [False] * (len(binary_string) + 1)
    dp[0] = True
    
    # Tracking positions where each word can end
    word_ends = [set() for _ in range(len(binary_string) + 1)]
    
    for i in range(len(binary_string) + 1):
        if not dp[i]:
            continue
        for word in string_array:
            if i + len(word) <= len(binary_string):
                if binary_string[i:i + len(word)] == word:
                    dp[i + len(word)] = True
                    word_ends[i + len(word)].add(word)
    
    if not dp[-1]:
        return False
        
    # Reconstruct the path to verify all words are used
    current_pos = len(binary_string)
    used_words = set()
    
    while current_pos > 0:
        found = False
        for prev_pos in range(current_pos):
            if dp[prev_pos]:
                for word in string_array:
                    if (prev_pos + len(word) == current_pos and 
                        binary_string[prev_pos:current_pos] == word):
                        used_words.add(word)
                        current_pos = prev_pos
                        found = True
                        break
            if found:
                break
                
    return set(string_array) == used_words

def is_prefix_free(codes: Set[str]) -> bool:
    codes_list = list(codes)
    for i in range(len(codes_list)):
        for j in range(i + 1, len(codes_list)):
            if (codes_list[i].startswith(codes_list[j]) or 
                codes_list[j].startswith(codes_list[i])):
                return False
    return True

def generate_binary_strings(max_length: int) -> List[str]:
    result = []
    for length in range(1, max_length + 1):
        for i in range(2 ** length):
            binary = bin(i)[2:].zfill(length)
            result.append(binary)
    return result

def get_all_subsets(binary_strings: List[str]) -> List[Set[str]]:
    n = len(binary_strings)
    subsets = []
    for i in range(1, 2 ** n):  # Start from 1 to exclude empty set
        subset = set()
        for j in range(n):
            if (i & (1 << j)):
                subset.add(binary_strings[j])
        subsets.append(subset)
    return subsets

def generate_huffman_codes(max_digits: int = 3) -> List[Set[str]]:
    binary_strings = generate_binary_strings(max_digits)
    all_subsets = get_all_subsets(binary_strings)
    return [subset for subset in all_subsets if is_prefix_free(subset)]

def FindPossibleHoffmanSets(T: str) -> List[Set[str]]:
    prefix_free_sets = generate_huffman_codes(3)
    return [set(s) for s in prefix_free_sets if can_construct_dp(T, list(s))]

def main():
    input_string = validate_input()
    valid_splits = FindPossibleHoffmanSets(input_string)
    
    print(len(valid_splits))
    print(sum(calculate_x(len(split)) for split in valid_splits))

if __name__ == "__main__":
    main()