# 반복문 for

s = 'abcdefg'
for n in s:
    print(n)

myList = [10,20,30,40,50]
for n in myList:
    print(n)

myT = (100,200,300,400)
for n in myT:
    print(n)

myS = {1,2,3,4}
for n in myS:
    print(n)

myD = {10:'aa', 20:'bb', 30:'cc'}
# for n in myD:
#     print(n)    # key 출력
for n in myD.keys():    # [10, 20 ,30]
    print(n)
for n in myD.values():  # [aa, bb, cc]
    print(n)
for n in myD.items():   # [(10, aa), (20, bb), (30,cc)]
    print(n)
for k, v in myD.items():
    print(k, v)         # tuple unpacking. ex) a, b = (100, 200)

stdData = [{'name':'홍길동', 'age':20}, {'name':'이순신', 'age':30}, {'name':'임꺽정', 'age':40}]
stdData1 = [('홍길동',20), ('이순신',30), ('임꺽정',40)]
# for n,a in stdData:
#     print(n,a)
for n in stdData:
    print(n)
    print('이름:%(name)s 나이:%(age)d'%n)

a = 10
b = 3.14
c = 'aa'
print ('a=%d b=%f c=%s' %(a,b,c))
d = {'name':'홍길동', 'age':20}
print ('이름:%(name)s 나이:%(age)d'%d)  # 딕셔너리 포맷
