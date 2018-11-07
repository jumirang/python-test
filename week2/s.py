# 반복문 (while)

# a = 0
# while a < 5:
#     print('a =', a)
#     # if a == 3:
#     #     break
#     a += 1
# else: # 옵션. while 조건문이 false 되는 경우, break로 탈출 시 else 수행하지 않음
#     print('else...')
# print('hello')

# 1+2+...+10
n = 1
mySum = 0
while n <= 10:
    # print(n)
    mySum += n
    n += 1
print('합은:', mySum)
