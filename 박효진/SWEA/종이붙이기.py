def sqr(N):
    if N == 1:
        return 1
    elif N == 2:
        return 3
    else:
        return sqr(N-1) + 2*sqr(N-2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N = N // 10
    result = sqr(N)
    print(f'#{tc} {result}')
    #시간복잡도 2의 N제곱
----------------------------------------메모이제이션
# 중간 계산값에 대해서 배열에 저장하고 이를 활용!
# 시간복잡도 N
memo = []
memo[10] =31
memo[20] = 3
def f2(N):
    if memo[N] != 0:
        return memo[N]
    # 중간 값에 대한 계산을 진행하고 메모에 이 값을 저장하겠다
    memo[N] = f2(N-10) + 2*f2(N-20)
    return memo[N]

----------------------------------------메모이제이션에서 반복문을 통한 표현 = DP 동적계획법
# 시간복잡도 N
memo = [0] * 301 # 미리 크기를 301 까지 확보한 리스트 초기화
memo[10] = 1
memo[20] = 3
    # 반복문을 통해서 해당 연산을 아래로부터 위로 차근차근 해결
for x in range(30, 301, 10):
    memo[x] = memo[x - 10] + 2*memo[x - 20]
# 출력
print(f'#{tc} {memo[N]}')