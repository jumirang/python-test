fp = open("data.txt", "w")
while True:
    name = input("이름: ")
    age = input("나이: ")
    ch = input("계속 입력하시겠습니까(y/n)? ")

    data = name + ',' + age + '\n'
    fp.write(data)

    if ch == 'n':
        break

fp.close()

print("\n")
print("------------------")
print("이름       나이")
print("------------------")

fp = open("data.txt", "r")
for r in fp:
    data = r.split(',')
    print(data[0], "\t", data[1])

fp.close()
