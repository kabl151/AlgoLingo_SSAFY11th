T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bus_stops = [0] * 5001
    for i in range(N):
        A, B = map(int,input().split())
        for j in range(A, B + 1):
            
            bus_stops[j] += 1
    

    P = int(input())
    result = []
    for i in range(P):
        C = int(input())
        result.append(bus_stops[C]) 

    # 출력
    print(f'#{tc}', *result)
