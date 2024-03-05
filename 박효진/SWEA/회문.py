# 해당되는 word가 회문이라면 1, 아니라면 0...
def is_palindrome(word):
    # 회문 : 정방향 단어 == 역방향 단어
    if word == word[::-1]:
        return 1
    else:
        return 0


def solution(boards, N, M):
    # - 가로에 M 길이 만큼의 회문이 있는가 검사!
    for i in range(N):
        for j in range(N - M + 1):
            if is_palindrome(boards[i][j:j + M]):
                return ''.join(boards[i][j:j + M])
    # - 세로에 M 길이 만큼의 회문이 있는가 검사!
    # 전치행렬 행 <-> 열 뒤바꾸는 행렬!
    t_boards = list(map(list, zip(*boards)))
    for i in range(N):
        for j in range(N - M + 1):
            if is_palindrome(t_boards[i][j:j + M]):
                return ''.join(t_boards[i][j:j + M])


# import sys
#
# sys.stdin = open("sample_input.txt", 'r')

# 테스트케이스 수 T
T = int(input())
for tc in range(1, T + 1):
    # 입력
    # 글자판의 한변의 길이 N, 회문의 길이 M
    N, M = map(int, input().split())

    # 글자판 N * N를 이차원 배열 boards
    boards = [list(input()) for _ in range(N)]

    # 로직
    palindrome = solution(boards, N, M)

    # 출력
    print(f"#{tc} {palindrome}")