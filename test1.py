val = []
sum = 0
i = 0
while True:
    inputNum = int(input())
    if inputNum == 0:
        break
    val.append(inputNum)
    if i % 2 == 0:
        sum += val[i]
    i += 1

print(val)
print(sum)