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

def part2(input):
    print("part2")


input_string = Validation()
# print("You entered:", input_string)

# listLen = part2(input_string)


listLen = [ 1 , 2 ,2]

Sum = 0
for i in listLen:
    Sum += CalculateX(i)

print(len(listLen))
print(Sum)
