import sys
input = sys.stdin.readline
N = int(input())
lst_x = []
lst_y = []

for _ in range(N):
    x, y = map(int, input().split())
    lst_x.append(x)
    lst_y.append(y)

max_x = max(lst_x)
max_y = max(lst_y)
min_x = min(lst_x)
min_y = min(lst_y)

print((max_x - min_x)*(max_y - min_y))