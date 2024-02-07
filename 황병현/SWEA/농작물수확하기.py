t = int(input())
for tc in range(1,t+1):
    # 입력값
    n = int(input())
    lst = [list(map(int,input())) for _ in range(n)]
    
    # 로직
    result = 0
    # 모든 row 탐색
    for x in range(n):
        # column을 row 중간으로 고정
        y = n//2
        result += lst[x][y]
        # 만약 x가 4를 넘지기 않는다면 : 위쪽 탐색
        if 0 < x <= y:
            for i in range(1,x+1):
                result += lst[x][y-i] + lst[x][y+i]
        # 그렇지 않다면 : 아래 탐색
        elif y < x < n-1 :
            for i in range(n-x-1,0,-1):
                result += lst[x][y-i] + lst[x][y+i]

    # 출력
    print(f'#{tc}',result)