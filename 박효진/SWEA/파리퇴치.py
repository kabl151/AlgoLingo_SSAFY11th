T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N 배열의 크기 / M 파리채의 크기
    my_matrix = [list(map(int, input().split())) for _ in range(N)]

    max = 0

    for row in range(N-M+1):

        pass