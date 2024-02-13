
# 0으로 초기화 되어있는 memo 배열을 생성한다.
# 미리 fibo(0) = 0, fibo(1) = 1 처럼 종료조건(기저조건)을 설정해준다.
# memo[0] = 0, memo[1] = 1 이다.

def fibo(n):    # 피보나치 함수 정의
    global memo # global 선언을 통해 memo 변수를 끌고온다.
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo(n-1) + fibo(n-2) # 재귀호출 형태 확인
    print(memo)
    return memo[n]  # memo에 저장할 데이터 리턴하여 자동으로 넣는다.

n = int(input())
memo = [0] * (n + 1)    # 저장할 데이터 공간 설정
memo[0] = 0             # 기저조건, 종료조건은 미리 넣어둔다
memo[1] = 1             # 이하동문

print(memo)
print(fibo(n))          # 출력

# dynamic programming (DP)
# 바텀 업
def fibo(n):            # 피보나치 함수 정의
    f = [0] * (n + 1)   # 저장할 수 있게 0으로 초기화되어있는 배열 설정
    f[0] = 0            # 기저조건
    f[1] = 1            # 이하동문
    for i in range(2, n + 1):   # 반복문을 통해 f[n] 을 구하러 올라간다
        f[i] = f[i-1] + f[i-2]  # 피보나치 식
    return f[n]         # 최종 목적지인 f[n] 을 반환

n = int(input())
print(fibo(n))

# 재귀함수를 이용한 피보나치 구현
def fibo(n):    
    if n < 2:       # 기저조건
        return n    # n = 1, n = 0 일때를 표현
    else:
        return fibo(n-1) + fibo(n-2)    # 피보나치 식
    
n = int(input())
print(fibo(n))
