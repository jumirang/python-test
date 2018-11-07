s = b'abc'
print (s)
print (type(s)) # <class 'bytes'>
s = s.decode('utf-8')
print (s)
print (type(s))

s1 = 'abc'
s1 = s1.encode('utf-8') # bytes 타입으로 변환
print (s1)
print (type(s1))

# 통신 : 어플 --octet(byte)-(send, write)-> 장비(시리얼), 호스트(소켓)
# str -> bytes
# 통신 : 어플 <-octet(byte)-(recv, read)-- 장비(시리얼), 호스트(소켓)
# str <- bytes
