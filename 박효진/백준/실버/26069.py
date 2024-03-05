import sys
input = sys.stdin.readline
N = int(input())
dance_lst = []
for i in range(N):
    name_lst = input().split()
    if 'ChongChong' in name_lst:
        dance_lst.append(name_lst[0])
        dance_lst.append(name_lst[1])
    elif name_lst[0] in dance_lst or name_lst[1] in dance_lst:
        dance_lst.append(name_lst[0])
        dance_lst.append(name_lst[1])
dance_lst = set(dance_lst)
print(len(dance_lst))