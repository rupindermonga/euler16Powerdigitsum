# summing the digits of npowerm

def PowerDigitSum(n,m):
    number = str(n**m)
    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
    return sum


final = PowerDigitSum(2,1000)
print(final)
