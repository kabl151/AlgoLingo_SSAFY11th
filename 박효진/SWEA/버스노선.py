T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bus_stops = [0] * 5001
    for i in range(N):
        A, B = map(int,input().split())
        for j in range(A, B + 1):
            # 해당 버스정류장의 카운트 값을 1 씩 증가
            bus_stops[j] += 1
    
    # 내가 알고싶은 버스 정류장의 갯수 P
    P = int(input())
    result = []
    for i in range(P):
        C = int(input())
        result.append(bus_stops[C]) # 버스 정류장에 몇개의 노선이 지나갔는지 카운트 된다.

    # 출력
    print(f'#{tc}', *result)
