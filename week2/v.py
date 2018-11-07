# 축약문법 // 라인 수 감소
# 내장리스트: [ 변수 for .. in .. if ]
# my = [n * 10 for n in range(1, 6)] # n은 최종적으로 구성된 리스트
# my = [n % 2 for n in range(1, 6)]
# print(my)

# 세금 3.3% 제외한 실수령액
# 급여 - 급여*0.033
# salary = [1000, 2000, 3000, 4000, 5000]
# sil = [n - n * 0.003 for n in salary]
# print(sil)

data = [n for n in range(1, 11) if n % 2 == 0] # for의 각 값을 if 조건 만족하면, 결과 변수(제일 왼쪽)로 넘어간다
print(data)
