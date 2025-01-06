T = '0101010'
Array_out = set()
SetOut = set()
out = []
for t in T :
    out.append(t)
    SetOut.add(t)
outCopy = out.copy()
Array_out.add(frozenset(SetOut))
SetOut = set()

#remove 0's from the output

i = 0
while i < len(out):
    if out[i] == '0' and i < len(out) - 1:
        out[i] = out[i] + out[i+1]
        out.pop(i+1)
    elif out[i] == '0' and i-1 > 0:
        out[i] = out[i-1] + out[i]
        out.pop(i-1)
    i+=1
for outs in out:
    SetOut.add(outs)
Array_out.add(frozenset(SetOut))
SetOut = set()
out0 = out.copy()
print(out,"0's removed")

#remove 01's from the output

i = 0
while i < len(out):
    if out[i] == '01' and i < len(out) - 1 and len(out[i+1]) == 1:
        out[i] = out[i] + out[i+1]
        out.pop(i+1)
    elif out[i] == '01' and len(out[i-1]) == 1 and i-1 > 0:
        out[i] = out[i-1] + out[i]
        out.pop(i-1)
    elif out[i] == '01' and i < len(out) - 1 and len(out[i+1]) == 2:
        out[i] = out[i] + out[i+1][0]
        out[i+1] = out[i+1][1]
    elif out[i] == '01' and len(out[i-1]) == 2 and i-1 > 0:
        out[i] = out[i-1][0] + out[i]
        out[i-1] = out[i-1][1]
    i+=1
for outs in out:
    SetOut.add(outs)
Array_out.add(frozenset(SetOut))
SetOut = set()
print(out,"01's removed")


#remove 00's and 01's from the output

i = 0
while i < len(out):
    if out[i] == '00' and i < len(out) - 1 and len(out[i+1]) == 1:
        out[i] = out[i] + out[i+1]
        out.pop(i+1)
    elif out[i] == '00' and len(out[i-1]) == 1 and i-1 > 0:
        out[i] = out[i-1] + out[i]
        out.pop(i-1)
    elif out[i] == '00' and i < len(out) - 1 and len(out[i+1]) == 2:
        out[i] = out[i] + out[i+1][0]
        out[i+1] = out[i+1][1]
    elif out[i] == '00' and len(out[i-1]) == 2 and i-1 > 0:
        out[i] = out[i-1][0] + out[i]
        out[i-1] = out[i-1][1]
    i+=1
for outs in out:
    SetOut.add(outs)
Array_out.add(frozenset(SetOut))
SetOut = set()
print(out,"00's and 01's removed")

#remove 00's from the output

out = out0.copy()
i = 0
while i < len(out):
    if out[i] == '00' and i < len(out) - 1 and len(out[i+1]) == 1:
        out[i] = out[i] + out[i+1]
        out.pop(i+1)
    elif out[i] == '00' and len(out[i-1]) == 1 and i-1 > 0:
        out[i] = out[i-1] + out[i]
        out.pop(i-1)
    elif out[i] == '00' and i < len(out) - 1 and len(out[i+1]) == 2:
        out[i] = out[i] + out[i+1][0]
        out[i+1] = out[i+1][1]
    elif out[i] == '00' and len(out[i-1]) == 2 and i-1 > 0:
        out[i] = out[i-1][0] + out[i]
        out[i-1] = out[i-1][1]
    i+=1
for outs in out:
    SetOut.add(outs)
Array_out.add(frozenset(SetOut))
SetOut = set()
print(out,"00's removed")

#remove 1's from the output

out = outCopy.copy()
i = 0
while i < len(out):
    if out[i] == '1' and i < len(out) - 1:
        out[i] = out[i] + out[i+1]
        out.pop(i+1)
    elif out[i] == '1' and i-1 > 0:
        out[i] = out[i-1] + out[i]
        out.pop(i-1)
    i+=1
for outs in out:
    SetOut.add(outs)
Array_out.add(frozenset(SetOut))
SetOut = set()
out0 = out.copy()
print(out,"1's removed")

#remove 11's from the output

i = 0
while i < len(out):
    if out[i] == '11' and i < len(out) - 1 and len(out[i+1]) == 1:
        out[i] = out[i] + out[i+1]
        out.pop(i+1)
    elif out[i] == '11' and len(out[i-1]) == 1 and i-1 > 0:
        out[i] = out[i-1] + out[i]
        out.pop(i-1)
    elif out[i] == '11' and i < len(out) - 1 and len(out[i+1]) == 2:
        out[i] = out[i] + out[i+1][0]
        out[i+1] = out[i+1][1]
    elif out[i] == '11' and len(out[i-1]) == 2 and i-1 > 0:
        out[i] = out[i-1][0] + out[i]
        out[i-1] = out[i-1][1]
    i+=1
for outs in out:
    SetOut.add(outs)
Array_out.add(frozenset(SetOut))
SetOut = set()
print(out,"11's removed")

#remove 10's and 11's from the output

i = 0
while i < len(out):
    if out[i] == '10' and i < len(out) - 1 and len(out[i+1]) == 1:
        out[i] = out[i] + out[i+1]
        out.pop(i+1)
    elif out[i] == '10' and len(out[i-1]) == 1 and i-1 > 0:
        out[i] = out[i-1] + out[i]
        out.pop(i-1)
    elif out[i] == '10' and i < len(out) - 1 and len(out[i+1]) == 2:
        out[i] = out[i] + out[i+1][0]
        out[i+1] = out[i+1][1]
    elif out[i] == '10' and len(out[i-1]) == 2 and i-1 > 0:
        out[i] = out[i-1][0] + out[i]
        out[i-1] = out[i-1][1]
    i+=1
for outs in out:
    SetOut.add(outs)
Array_out.add(frozenset(SetOut))
SetOut = set()
print(out,"10's and 11's removed")

#remove 10's from the output

out = out0.copy()
i = 0
while i < len(out):
    if out[i] == '11' and i < len(out) - 1 and len(out[i+1]) == 1:
        out[i] = out[i] + out[i+1]
        out.pop(i+1)
    elif out[i] == '11' and len(out[i-1]) == 1 and i-1 > 0:
        out[i] = out[i-1] + out[i]
        out.pop(i-1)
    elif out[i] == '11' and i < len(out) - 1 and len(out[i+1]) == 2:
        out[i] = out[i] + out[i+1][0]
        out[i+1] = out[i+1][1]
    elif out[i] == '11' and len(out[i-1]) == 2 and i-1 > 0:
        out[i] = out[i-1][0] + out[i]
        out[i-1] = out[i-1][1]
    i+=1
for outs in out:
    SetOut.add(outs)
Array_out.add(frozenset(SetOut))
SetOut = set()
print(out,"10's removed")
print(Array_out)