import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
lst = list(map(int, input().split()))
for i in range(len(lst)-1,0,-1):
    for j in range(0, i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            cnt += 1
        else:
            pass
print(cnt)