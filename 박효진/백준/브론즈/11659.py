import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))


for i in range(M):
    sum_num = 0
    x, y = map(int, input().split())
    for j in range(y-x+1):
        sum_num += arr[x-1]
        if x == y:
            print(sum_num)
