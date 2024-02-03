# K, N, M = list(map(int, input().split()))
# M_lst= list(map(int, input().split()))

# def second_step(K, N):
#     min_num = N // K
#     if N % K == 0:
#         min_num -= 1
#     else:
#         pass
#     result = min_num
#     return result

# def first_step(K, N, M, M_lst):
#     result = 1
#     for i in range(0, M-1):
#         if K < M_lst[i + 1] - M_lst[i]:
#             result = 0
#         else:
#             pass
#     if result == 1:
#         return second_step(K, N)
#     else:
#         return 0

# print(first_step(K, N, M, M_lst))


T = int(input()) # 노선수
for tc in range(1, T + 1):
    #입력
    K, N, M = map(int, input().split())

    stations = [0] * N
    charges = list(map(int, input().split()))

    for charge in charges:
        stations[charge] = 1

    # 그리디 알고리즘 : 매번 최선의 선택을 반복하면 
    #                  그것이 최종적으로 최선의 정답으로 결과가 나오는 것
    
    # 최선의 선택 : 현 버스 위치에서 갈 수 있는 가장 먼곳의 충전소를 들른다.
    # 단, 다음 장소로 이동해야하기 때문에, 갈수있는 충전소를 방문하는 것이 중요하다.
    # 버스의 현재 위치 position
    pos = 0
    # 충전 횟수
    cnt = 0

    # 현재 위치에서 K 거리까지 갔을 때 N위치를- 넘게되는 경우까지 반복
    while pos + K < N:
        # K 거리 내에서 가장 먼 충전소를 찾아 위치 이동.
        # pos + K, pos + K - 1, pos + K-2 ... pos + 1
        for nxt in range(pos + K, pos, -1):
            # 다음 위치는 nxt
            # 다음 위치 nxt 에서 충전소가 있다면 이동
            if stations[nxt] == 1:
                # 이동! (충전횟수 1 증가)
                pos = nxt
                cnt += 1
                break
        #이동을 해야되었음에도 불구하고 이동하지 않았따면
        else:
            cnt = 0
            break
    print(f'#{tc}', cnt)
