# 파일 다루기
def fileWrite():
    fp = open("test.txt", "w") # w, 새롭게 생성하여 write 한다
    # print(fp.tell()) # file 위치 0
    # fp.write("abcdefg") # file 위치 7
    fp.write("abc\ndef\nghi")
    # print(fp.seek(3)) # file 위치 3
    # print(fp.tell())
    # fp.write("hello")
    fp.close()

def fileRead():
    fp = open("test.txt", "r")
    # rd = fp.read() # 파일 전체 내용 읽음
    # print(rd)
    # rd = fp.readline() # 라인 다위로 읽음
    # print(rd)
    # rd = fp.readline()
    # print(rd)
    # for r in fp: # r = readLine
    #     print(r)
    rd = fp.readlines() # 출력: ['abc\n', 'def\n', 'ghi']
    print(rd)
    fp.close()

# def fileRead():
#     fp = open("test.txt", "r")
#     # rd = fp.read() # 파일 전체 내용 읽음
#     # rd = fp.read(3) # 3bytes 읽음
#     # print(rd)
#     # rd = fp.read(3) # 3bytes 읽음
#     # print(rd)
#     while True:
#         rd = fp.read(3)
#         # if rd == None:
#         if not rd:
#             break
#         print(rd)
#     fp.close()

fileWrite()
fileRead()
