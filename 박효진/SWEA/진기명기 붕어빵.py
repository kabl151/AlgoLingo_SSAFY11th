T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # N:몇명오는지, M:시간, K:붕어빵 갯수
    sec_lst = list(map(int, input().split())) # 각각 몇초에 오는지
    t = 0 #단위시간 카운팅
    result = 1
    for i in range(11112):
        t += 1
        made = K * (t // M)   # 만들어진 붕어빵
        people = 0
        for j in sec_lst:
            if j <= t:
                people += 1
        if made < people:
            result = 0
    if 0 in sec_lst:
        result = 0
    if result == 1:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')