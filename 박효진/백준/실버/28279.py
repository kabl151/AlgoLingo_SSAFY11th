import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
dq = deque()
for _ in range(N):
    keyword = input().split()
    if keyword[0] == '1':
        dq.appendleft(keyword[1])
    elif keyword[0] == '2':
        dq.append(keyword[1])
    elif keyword[0] == '3':
        if dq:
            num = dq.popleft()
            print(num)
        else:
            print(-1)
    elif keyword[0] == '4':
        if dq:
            num = dq.pop()
            print(num)
        else:
            print(-1)
    elif keyword[0] == '5':
        print(len(dq))
    elif keyword[0] == '6':
        if dq:
            print(0)
        else:
            print(1)
    elif keyword[0] == '7':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif keyword[0] == '8':
        if dq:
            print(dq[-1])
        else:
            print(-1)