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

T = '01110'
allSplits = SplitBinary(T)
valid = Filter(allSplits)
for i in range (len(valid)):
    valid[i] = set(valid[i])
print(valid)