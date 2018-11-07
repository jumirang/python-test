# sys 모듈
import sys
# print(sys.argv) # 콘솔 상에서 argv 문자열을 받음
# my = sys.argv
# print(my[1])

myList = [10, 20 ,30]
myList1 = myList
print(sys.getrefcount(myList) - 1) # sys.getrefcount()가 myList 객체를 참조하여 ref count 1 증가시킴. 따라 해당 것은 -1 해줌

sys.stdout.write('aa\n')    # like print()
sys.stdout.write('bb\n')

# random 모듈
import random
for n in range(5):
    print(random.randint(1, 5)) # 1 ~ 5 사이 값 랜덤

myList = [1, 2, 3, 4, 5]
print(myList)
random.shuffle(myList)  # 시퀀스 타입을 임의로 재배치 해줌
print(myList) # ex) [5, 3, 4, 2, 1]


myList = [1, 2, 3, 4, 5]
print(myList)
print(random.choice(myList))    # 시퀀스 타입 중 임의로 하나 선택
print(random.sample(myList, 2)) # 시퀀스 타입 중 임의로 n개 선택

# 로또 1~16 임의로 6개 선택
rotto = [n for n in range(1, 17)]
print(rotto)
for n in range(5):
    print(random.sample(rotto, 6))
