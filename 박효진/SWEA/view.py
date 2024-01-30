# 테스트케이스 순회
T = 10
for tc in range(1, T + 1):
    #입력
    # 건물의 개수N
    N = int(input())
    buildings = list(map(int, input().split()))
    #출력
    cnt = 0
    for i in range(2, N-2):
    # 나에 대한 인덱스를 임의로 i -> buildings[i]
    # - 왼쪽 두 건물 : buildings[i-2], buildings[i-1]
    # - 오른쪽 두 건물 : buildings[i+1], buildings[i+2]
        me_height = buildings[i]
        mx_other_height = max(
            buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
        # 나 (중앙에 있는 빌딩)과 비교한다.
        if me_height > mx_other_height:
            # 조망권이 확보가 되어있는 상태라면 그 차이를 조망권 세대수로 누적한다.
            # 현 건물에 대한 조망권 세대 수
            cnt += me_height - mx_other_height

    # 출력
    print(f'#{tc} {cnt}')