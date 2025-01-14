from itertools import combinations

# Define all binary strings of up to 3 bits
binary_strings = [
    "0", "1",
    "00", "01", "10", "11",
    "000", "001", "010", "011", "100", "101", "110", "111"
]

# Function to check if a set of strings satisfies the prefix-free property
def is_prefix_free(code_set):
    for s1 in code_set:
        for s2 in code_set:
            if s1 != s2 and s2.startswith(s1):  # s2 starts with s1
                return False
    return True

# Generate all subsets and count the prefix-free ones
valid_prefix_free_sets = 0

# Loop over all possible subset sizes
for r in range(1, len(binary_strings) + 1):
    for subset in combinations(binary_strings, r):
        if is_prefix_free(subset):
            valid_prefix_free_sets += 1

print(valid_prefix_free_sets)
