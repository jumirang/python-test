# 연산자
a = 10 + 2
b = 10 - 2
c = 10 * 2
d = 10 / 3  # 정수/정수 ==> 실수
e = 10 ** 2 # 거듭제곱 연산자
f = 10 // 3 # 몫 연산자
g = 10 % 3
print(a, b, c, d, e, f, g)

# 결합도 좌-->우
# **
# * / // %
# + -

a = 10 + 2 - 3 * 2 ** 2
print(a)

# 반지름이 5인 원의 면적을 구하시요
c = 5 ** 2 * 3.14
print("원의 면적: ", c)

s = input("입력: ")
print(s)
print(type(s))

# 하나의 반지름을 입력받아 원의 면적을 구하시요
# a = '10'
# a = int(a)  # int 형변환
# b = 10
# b = str(b)  # str 형변환
# c = (10,20,30)
# c = list(c) # list 형변환

r = input("반지름: ")
r = int(r)
c = r ** 2 * 3.14
print("원의 면적: ", c)
