# 테스트케이스 수
# 인원수 N 과 다음줄에 N명이 고른 카드가 번호순으로.
T = int(input())
for tc in range(1, T+1):
    #입력
    #인원의 수N
    N = int(input())
    #인원들이 뽑은 카드 번호들 cards
    cards = list(map(int,input().split()))
    #로직
    #해당 인원들을 절반씩 자르면서 토너먼트 형태로 경기를 진행
    # 분할정복 (divide-conquer) 기법
    def tournament(i, j): # 시작점 i, 끝점 j
        # 기저조건 : 단 한명만 남을 때 까지
        if i == j: # 양쪽 끝이 같다. 단 한명이 남을경우
            return i
        # 해당 인원을 절반씩 자르는 '분할' 과정..
        winner1 = tournament(i, (i+j)//2)     # 왼쪽그룹
        winner2 = tournament((i+j)//2 + 1, j) # 오른쪽그룹

        #가위바위보 게임을 시킨다 '정복'
        winner = play(winner1, winner2)
        return winner
    
    # 사람 a와 사람b에 대한 가위바위보 진행
    def play(a, b):
        card_a = cards[a]
        card_b = cards[b]

        # 가위 1, 바위 2, 보 3
        
        # 가위 vs 가위 or 바위 vs 바위 or 보 vs 보
        if card_a == card_b: # 이 경우 번호 작은사람이 이긴다 = a 승리
            return a
        # a가 이긴경우 가위 vs 보, 바위 vs 가위, 보 vs 바위
        elif (card_a == 1 and card_b == 3) or \
            (card_a == 2 and card_b == 1) or \
            (card_a == 3 and card_b == 2):
            return a
        # 나머지 b가 이긴경우
        # 가위 vs 바위
        # 바위 vs 보
        # 보 vs 가위
        else:
            return b

    
    result = tournament(0, N-1) + 1
    # 출력
    print(f'#{tc} {result}')