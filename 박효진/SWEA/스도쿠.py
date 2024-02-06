# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    dx = [0, 0, 1, 1, 1, 0, -1, -1, -1]
    dy = [0, 1, 1, 0, -1, -1, -1, 0, 1]
    result = 1
    for j in range(9):
        if len(set(arr[j])) != 9:
            result = 0
        else:
            pass
    for x in range(1,10,3):
        for y in range(1,10,3):
            lst = []
            for z in range(9):
                lst.append(arr[x+dx[z]][y+dy[z]])
            if len(set(lst)) != 9:
                result = 0

    re_arr = list(map(list, zip(*arr)))
    for k in range(9):
        if len(set(re_arr[k])) != 9:
            result = 0
        else:
            pass
    print(f'#{tc} {result}')
