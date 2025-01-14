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
huffman_codes = generate_huffman_codes(3)