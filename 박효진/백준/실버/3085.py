import sys
input = sys.stdin.readline

def check():
    global max_cnt
    for i in range(N):
        for j in range(N):
            for k in range(2):
                cnt = 0
                for l in range(N):
                    nx = i+da[k]*l
                    ny = j+db[k]*l
                    if 0<= nx <N and 0<= ny < N and arr[nx][ny] == arr[i][j]:
                        cnt += 1
                    elif 0<= nx <N and 0<= ny < N and arr[nx][ny] != arr[i][j]:
                        break
                if max_cnt <= cnt:
                    max_cnt = cnt

N = int(input())
arr = [list(map(str, input())) for _ in range(N)]
# 가지치기 오른쪽 / 아래로 가능할 듯
dx = [0, 1]
dy = [1, 0]
da = [0, 1]
db = [1, 0]
max_cnt = 0
check()

for i in range(N):
    for j in range(N):
        info = arr[i][j]
        for k in range(2):
            na = i+dx[k]
            nb = j+dy[k]
            if 0 <= na < N and 0 <= nb < N and arr[i][j] != arr[na][nb]:
                arr[i][j], arr[na][nb] = arr[na][nb], arr[i][j]
                check()
                arr[i][j], arr[na][nb] = arr[na][nb], arr[i][j]

print(max_cnt)