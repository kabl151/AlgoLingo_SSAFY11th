import sys
input = sys.stdin.readline

def bingo():
    bingo_cnt = 0
    global result
    for i in range(5):
        for j in range(5):
            if block[i][j] == 1:
                for k in range(4):
                    num_cnt = 0
                    for l in range(5):
                        nx = i+dx[k]*l
                        ny = j+dy[k]*l
                        if 0 <= nx < 5 and 0 <= ny < 5 and block[nx][ny] == 1:
                            num_cnt += 1
                    if num_cnt == 5:
                        bingo_cnt += 1
    if bingo_cnt >= 3:
        result = True

arr = [list(map(int, input().split())) for _ in range(5)]
call = []
result = False
cnt = 0
dx = [0, 1, 1, 1]
dy = [1, 1, 0, -1]
block = [[0]* 5 for _ in range(5)]
for i in range(5):
    call += list(map(int,input().split()))

for k in range(25):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == call[k] and result == False:
                block[i][j] = 1
                cnt += 1
                bingo()
print(cnt)