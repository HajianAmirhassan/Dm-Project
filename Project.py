def SplitBinary(s, max_len=3):
    def backtrack(start, Current):
        if start == len(s):
            result.append(Current[:])
            return
        
        for length in range(1, min(max_len + 1, len(s) - start + 1)):
            substring = s[start:start + length]
            Current.append(substring)
            backtrack(start + length, Current)
            Current.pop()
    
    result = []
    backtrack(0, [])
    return result

def hasPrefixInArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[j].startswith(arr[i]) and arr[i] != arr[j]:
                return True
    return False

def Filter(splits):
    ArrayOut = []
    for split in splits:
        hasPrefix = hasPrefixInArray(split)
        if not hasPrefix:
            ArrayOut.append(split)
    return ArrayOut

def Validation():
    user_input = input("")
    for char in user_input:
        if char not in {'0', '1'}:
             print("Invalid input.")
             break
    return user_input

def CalculateX(n):
  if n == 0:
    return 0 
  else:
    result = 1
    for i in range(0 , n):
      result *= (26 - i)
    return result

input_string = Validation()

allSplits = SplitBinary(input_string)
valid = Filter(allSplits)
for i in range (len(valid)):
    valid[i] = set(valid[i])

lengths = [len(item) for item in valid]

Sum = 0
for i in lengths:
    Sum += CalculateX(i)

print(len(lengths))
print(Sum)
