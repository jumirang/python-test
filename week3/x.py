# 메모리 구조와 LGB 규칙
# ---------------------------------
# Text Area   |   static (global) //
#             |   heap (free)     // c++ new 키워드, 파이썬 new 키워드 없음. 대신, 변수 = 클래스 수행 시 힙 영역 할당
# ---------------------------------
# String Area |   stack           // 함수 로컬 영역
# ---------------------------------
# (변수) 우선 순위 : 1. Local 2. Global 3. Builtins(빌트인)
#

# g = 10
#
# def fn():
#     global g    # 지역 변수인 g를 만들지 않고, 글로벌 변수 g에 100을 할당해 버림(10이 아니라 100이 저장됨)
#     g = 100
#     print('fn() g =', g)
#
# fn()
# print('g =', g)

# def fn():
#     myList = [10, 20, 30] # myList = list([10, 20, 30]), list 클래스로 [10, 20, 30]을 힙 영역 할당 후 myList 변수가 참조. myList는 참조 포인터 를 가짐(ex. 1000)
#     print (id(myList))
#     return myList
#
# rst = fn()        # fn() 리턴 시, myList 로컬 변수는 사라지고 CPU 레지스터 영역의 eax의 참조 포인터 1000을 가짐. rst에 1000 할당. list [10, 20, 30]은 rst에 의해 RC 1을 유지하므로 힙 영역에 존재하게 됨.
# print(id(rst))    # myList와 rst의 id는 동일함 (참조이므로)
# print(rst)

# 빌트인
# print( dir(__builtins__) )

# a = 10
# a = str(a)
# print (a, type(a))

str = "abc"
def fn():
    # str = "cde"
    print(str)

fn()
print(str)
a = 10
a = str(a)      # LGB 규칙에 의해, str = "abc"로 먼저 사용되게 됨
print(a)        # TypeError: 'str' object is not callable
