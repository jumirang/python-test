ch = 'y'
while ch != 'n':
    name = input('이름: ')
    age = int(input('나이: '))
    ch = input('계속 입력하시겠습니까(y/n)? ')
else:
    print('종료')

data = [('홍길동', 20), ('이순신', 30)]
print('----------------')
print('이름   나이')
print('----------------')
for k, v in data:
    print(k, '\t', v)