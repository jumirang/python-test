# 구성원연산자 (True, False)
# in 구성원에 있다
# not in 구성원에 없다
# s = "abcdef hello"
# print("hello" in s)
# print("zzz" not in s)

# myList = [10, 20, 30, 40, 50]
# print(100 in myList)
#
# myD = {10:"aa", 20:"bb", 30:"cc"}
# print(20 in myD) # dictionary는 key에 대해서만 확인 가능함

# 식별연산자
# is 객체가 같다
# not is 객체가 틀리다
# 메모리 설명이 필요하다
a = 10
# b = 10 # a, b는 동일한 대상 객체 10을 리퍼런스 한다
b = 10
b = 100 # b는 대상 객체가 10 -> 100으로 바뀐다
print(a is b)
print(id(a)) # 대상 객체 id 확인
print(id(b))

a = 10
a = "abc" # a는 "abc" 대상 객체를 참조로 변경, 10 객체는 RC가 0이므로 메모리에서 소멸됨

myList = [10, 20, 30, 40]
# myList1 = myList          # shallow copy (얉은 복사, 대상 객체는 동일하고 address만 copy)
myList1 = myList.copy()   # deep copy (깊은 복사, 별도의 리스트 객체로 만듦)
# myList1 = [10, 20, 30, 40] # myList 대상 객체와는 다르다
myList1[0] = 100
print(myList)
print(myList is myList1)
print(id(myList))
print(id(myList1))
