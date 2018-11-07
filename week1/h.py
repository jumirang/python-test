# 순서있는 데이터 타입 (인덱스, 슬라이싱)
# 리스트, 튜플, 문자열, 바이트

# 변경가능(mutable) 데이터 타입
# 리스트, 딕셔너리, 세트

# 순서없는 데이터 타입 (인덱스, 슬라이싱 X)
# 딕셔너리, 세트

# 변경불가능(immutable) 데이터 타입
# 튜플, 문자열, 바이트

# myList = [10, 3.14, True, "abc"] # list()
# print ( myList )
# print ( type(myList) )
# print ( myList[0] )
# print ( myList[3] )
# print ( myList[-1] )
# print ( myList[0:3:1] )
# print ( myList[1:3:2] )

myList = [10, 20, 30, 40, 20]
myList[0] = 100 # mutable
# myList.append(50)
# myList.insert(1, 200)
# myList.extend( [1, 2, 3] )
# myList += [1, 2, 3]
# myList = myList * 3
# myList.remove(30)
# myList.pop() # 맨 마지막 객체 삭제
# myList.pop(1)
# del ( myList[0] )

# n = myList.index(20)
# n = myList.count(20)
n = len(myList)
print (n)
print (myList)
