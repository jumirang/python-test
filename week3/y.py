# 일급함수 (First Class Function)
# 함수의 할당
# 함수의 리턴
# 함수의 인자
# 함수내 함수정의 // 클래스 및 데코레이터를 배워야 함

def fn():
    print('hello')

# fn1 = fn    # fn은 Text Area의 함수의 시작주소를 갖음
# fn()
# fn1()

def my(a):
    print(id(a))
    a()

# print(id(fn))
# my(fn)

def my1():
    return fn

# rst = my1()
# rst()

# 파이썬, switch 문이 없음 -> 딕셔너리와 일급함수로 완벽하게 대치 가능함

def afn():
    print('afn')
def bfn():
    print('bfn')

d = {0:afn, 1:bfn}

menu = int(input("메뉴를 선택: "))
d[menu]()
