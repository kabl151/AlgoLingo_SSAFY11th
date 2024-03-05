from collections import deque

for tc in range(1,11):
    N = int(input())
    arr = list(map(int, input().split()))   # lst 생성
    dq = deque(arr)                     # arr를 deque로 형변환 
    while True:                         # 특정한 상황일 때 while문 탈출
        for i in range(1,6):            # 1부터 5까지가 한싸이클
            dq[0] -= i                  # dq의 0번째 요소에 연산 작용
            dq.rotate(-1)               # 이후 0번인덱스를 반대쪽으로 보내는 rotate 사용
            if dq[-1] <= 0:             # 옮기고 나서 [-1] 인덱스 요소가 0 이하일때 for문 탈출
                dq[-1] = 0              # 출력 값을 위해 0으로 바꿔줌
                break                   # for문 강제 탈출
        if dq[-1] == 0:                 # 강제탈출 조건
            break                       # while 문 강제 탈출
    print(f'#{N}', *dq)                 # 출력