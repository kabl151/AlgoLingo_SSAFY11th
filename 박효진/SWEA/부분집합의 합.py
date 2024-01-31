# 테스트 케이스 수 T
T = int(input())
for tc in range(1, T + 1):
    # 입력
    N, K = map(int, input().split())
    # 로직
    A = [i for i in range(1, 13)]
    cnt = 0
    # 1부터 12까지를 가지는 A 원소 부분집합을 만드는 코드
    for i in range (1 << 12):
        #해당 i의 j 번째 비트가 1인지 확인
        subset = [] # 부분집합의 임시 리스트
        for j in range(12):
            if i & (1 << j):
                #해당 i 의 j 번째 비트가 1이라면.. > 부분집합의 요소
                subset.append(A[j])
        # 부분집합의 요소의 갯수가 N개라면 and 부분집합의 요소의 합이 K라면
        if len(subset) == N and sum(subset) == K:
            # 카운트를 해준다
            cnt += 1
    # 출력
    # 만든 카운트 출력
    print(f'#{tc} {cnt}')