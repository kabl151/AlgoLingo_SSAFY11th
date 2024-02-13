# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    arr = list(map(int, input().split()))
    max_high = 0
    for i in range(N):
        cnt = 0
        for j in range(i + 1, N):
            if arr[i] > arr[j]:
                cnt += 1
        if cnt >= max_high:
            max_high = cnt
    print(f'#{test_case} {max_high}')


# 강사님 코드
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = 0
    for i in range(N-1):
        cnt = 0
        for j in range(i + 1, N):
            if arr[i] > arr[j]:
                cnt += 1
        if max_v < cnt:
            max_v = cnt
    print(max_v)