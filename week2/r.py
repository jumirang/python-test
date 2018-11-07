# 3항 연산자 (c, java 등 사용)
# int a = 3;
# int rst;
# rst = a > 0 ? 100 : 200; # 3항 연산자
# printf("rst = %d\n", rst);

# if문 축약형 (참일때의 값 if 판단 else 거짓일때 값), 3항 연산자 대체
# a = 3
# rst = 100 if a > 0 else 200
# print (rst)

n = int(input('정수입력: '))
print('짝수' if n % 2 == 0 else '홀수')
