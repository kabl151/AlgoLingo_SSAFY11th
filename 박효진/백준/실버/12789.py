import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
space = []
ok_lst = []
for i in arr:
    if i == 1:
        ok_lst.append(i)
        for _ in range(len(space)):
            if len(space) !=0 and space[-1] == len(ok_lst) + 1:
                num = space.pop()
                ok_lst.append(num)
    elif i == len(ok_lst) + 1:
        ok_lst.append(i)
        for _ in range(len(space)):
            if len(space) !=0 and space[-1] == len(ok_lst) + 1:
                num = space.pop()
                ok_lst.append(num)
    elif i != len(ok_lst) + 1:
        space.append(i)

if space:
    print('Sad')
else:
    print('Nice')