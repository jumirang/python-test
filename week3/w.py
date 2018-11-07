# 함수
# def 함수 (인자...):
#     ...
#     return            # 리턴값이 여러개 올수 있다.(파이썬 특징)
#
# 특징
# 두 개 이상의 값 리턴 가능
# 명시적 인자 호출
# 디폴트 인자
# 가변 인자
# 정의되지 않은 인자

def hello():
    print('hello')
    print('fn')
# hello()
# hello()

def hap(a, b):
    return a + b
# rst = hap(10, 20)
# print(rst)

def fn1():              # 두 개 이상의 값 리턴 가능
    return 10, 20, 30   # (10, 20, 30) 자동으로 packing 되어 tuple로 나옴
# rst = fn1()
# print(rst)
#
# (a, b, c) = fn1()
# print (a, b, c)

def fn2(a ,b):
    print(a, b)
fn2(10 ,20)
fn2(b = 100, a = 200)  # 명시적 인자 호출

n = 10
m = 20
print (n, m, sep = '-') # sep 인자가 디폴트로 스페이스 이다. 명시적으로 다른 값 주면 해당 값 할당
print('hello', end = ' ') # end 인자가 디폴트로 개행문자 이다.
print('hi')

def fn3(a=10, b=20, c=30): # 디폴트 인자
    print(a, b, c)
# fn3()
# fn3(100)
# fn3(100, 200)
# fn3(100, 200, 300)
# fn3(b=1000)


def fn4(*args): # 가변 인자
    print(args) # 넘어온 인자는 tuple 타입을 가짐
    for n in args:
        print(n)
# fn4(10, 20)
# fn4(10, 20, 30)
# fn4('aa', 'bb', 'cc', 'dd')

def fn5(*args):
    for n in args:
        print(n, "의 원의 면적:", n ** 2 * 3.14, sep='')
# fn5(3, 4, 5)

def fn6(**args):    # 정의되지 않은 인자
    print(args)
# fn6(name='홍길동', age=20)
# fn6(aa=100, bb=200, cc=300)
