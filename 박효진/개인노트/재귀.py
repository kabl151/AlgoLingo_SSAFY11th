
def factorial(n):
    # 종료 조건(=기저 조건) : n = 0이면 1을 반환한다
    if n == 0:
        return 1
    # 재귀 호출 : n과 n-1의 팩토리얼을 곱한 결과를 반환한다
    return n * factorial(n - 1)     # return에 자기 함수를 다시 넣음으로써 재귀 함수를 호출

# 함수 계산 예시
print(factorial(5)) # 120
