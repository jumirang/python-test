s1 = "ab\n" \
     "\t\t\tc"
s2 = 'ab' \
     'c'
s3 = '''ab
            c'''
s4 = """ab
c"""
print(s1)
print(s2)
print(s3)
print(s4)
print( type(s1) )
print( type(s2) )
print( type(s3) )
print( type(s4) )

# 복합(시퀀스) 여러개의 데이터
# 순서있는 데이터 타입 ( 인덱스, 슬라이싱 )
s1 = 'abc'  # 0 1 2 ... / ... -3 -2 -1
print ( s1[0] )
print ( s1[1] )
print ( s1[-3] )

# 슬라이싱 [시작: 끝: 증가치]
s1 = 'abcdefghi'
print ( s1[0:4:1] )   # 0 <= .. < 4, 4는 포함 안됨
print ( s1[1:4] )   # 증가치 디폴트 1
print ( s1[:5:2] )  # 시작 디폴트 0
print ( s1[1:] )    # 끝 디폴트는 끝까지
print ( s1[-1:-4:-1] )

# 문자열 연산자 : +, *, %
s1 = 'abcdefghi'
s1 = s1 + 'korea'
print ( s1 )
s1 = s1 * 2
print ( s1 )

a = 10
b = 3.14
s = 'abc'
s1 = 'a=%10d b=%.2f s=%s' %( a, b, s )  # c언어 printf 유사
print ( s1 )

s = "   abcd efg    "
#s = s.split()   # space로 자름
s = s.strip()   # 좌우의 white space 제거 (공백, \n, \t) // 중간 안됨
print ( s )

s = 'abc'
print ( s[0] )
s[0] = 'A'      # 문자열 데이터 타입은 수정 불가능한 immutable 타입이므로 수정 불가

# s3 = '''ab
#         c'''
# print (s3)
