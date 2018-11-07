def doDivisor(n):
    res = list()
    for i in range(1, n+1):
        if n % i == 0:
            res.append(i)
    return res

n = int(input("정수 입력: "))
print(n, "의 약수: ", sep='', end='')

for n in doDivisor(n):
    print(n, end=' ')
