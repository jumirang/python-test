a = 10
# a = a + 2
# a += 2
# a -= 2
# a = a ** 2
a **= 2
print (a)

a = 10
# a = a + 1
# a += 1
# a++   # 파이썬은 전치, 후치 연산자를 지원하지 않음
++a     # 에러발생하지 않으나, +(+a): 양수 a임을 나타냄
print(a)