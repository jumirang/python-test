# range

# r = range(0, 10, 1) # (초기값, 끝값, 증가치), 슬라이싱 처럼 끝값은 포함되지 않음
# r = range(10)
# r = range(1, 10, 2)
# print( list(r) )

# for n in range(1, 10):
#     print(n)

# mySum = 0
# for n in range(1, 11):
#     mySum += n
# print(mySum)

for n in range(1, 11):
    if n == 3:
        continue
    print(n)
        # break
else:   # 옵션
    print('else...')
