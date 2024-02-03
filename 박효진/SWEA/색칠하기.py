T = int(input())

for tc in range(1, T + 1):

    # 테스트케이스의 첫 줄에 칠할 영역의 개수 N
    N = int(input())
    # 행(i)과 열(k)의 크기를 지정
    a = 10
    b = 10
    # 10x 10 으로 이루어진 블록 배열 생성
    block = [[0 for _ in range(a)] for _ in range(b)]
    
    cnt = 0 # 카운트 횟수 초기화 (보라색 된 타일 개수)

    # N번 첫출에 칠할 영역 개수
    for _ in range(N):
        color_info = list(map(int, input().split())) # 색칠할 정보 입력

        for i in range(color_info[0], color_info[2]+ 1): # 인덱스0과 2에 해당하는 행좌표
            for j in range(color_info[1], color_info[3] + 1): # 인덱스 1과 3에 해당하는 열좌표
                block[i][j] += color_info[4] # 칠해진다면 인덱스 4에 해당하는 색을 더해준다

    # 전체 블록 접근
    for k in range(a):  #행
        for l in range(b):  #열

            if block[k][l] == 3: # 빨강+파랑이면 block 안 정수가 3일 것이므로 있을때마다 cnt 1증가
                cnt += 1

    print(f'#{tc} {cnt}')   #최종출력