def split_binary(s, max_len=3):
    def backtrack(start, current):
        if start == len(s):
            result.append(current[:])
            return

        for length in range(1, min(max_len + 1, len(s) - start + 1)):
            current.append(s[start:start + length])
            backtrack(start + length, current)
            current.pop()

    result = []
    backtrack(0, [])
    return result

def has_prefix_in_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[j].startswith(arr[i]) and arr[i] != arr[j]:
                return True
    return False

def filter_splits(splits):
    return [split for split in splits if not has_prefix_in_array(split)]

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
valid_splits = filter_splits(all_splits)
valid_splits = [set(split) for split in valid_splits]

lengths = [len(item) for item in valid_splits]

total_sum = sum(calculate_x(length) for length in lengths)

print(len(lengths))
print(total_sum)