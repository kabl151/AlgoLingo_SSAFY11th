import sys
input = sys.stdin.readline

N = int(input())
LH_lst = []
max_height = 0
max_idx = 0
width = 0
for i in range(N):
    L, H = map(int, input().split())
    LH_lst.append([L,H])
    if max_height < H:
        max_height = H
LH_lst.sort()
for i in range(N):
    if LH_lst[i][1] == max_height:
        max_idx = i
    
for i in range(max_idx):
    if LH_lst[1][1] >= LH_lst[0][1]:
        width += LH_lst[0][1]*(LH_lst[1][0] - LH_lst[0][0])
        LH_lst.pop(0)
    else:
        LH_lst.pop(1)
LH_lst.reverse()
for i in range(len(LH_lst)-1):
    if LH_lst[1][1] >= LH_lst[0][1]:
        width += LH_lst[0][1]*(LH_lst[0][0] - LH_lst[1][0])
        LH_lst.pop(0)
    else:
        LH_lst.pop(1)
print(width+max_height)