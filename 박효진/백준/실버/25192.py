import sys
input = sys.stdin.readline

N = int(input().rstrip())
lst = []
cnt = 0
for i in range(N):
    keyword = input().rstrip()
    if keyword != 'ENTER':
        lst.append(keyword)
    elif keyword == 'ENTER':
        cnt += len(set(lst))
        lst.clear()
cnt += len(set(lst))
print(cnt)