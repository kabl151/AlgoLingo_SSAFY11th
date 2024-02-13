import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
d = deque()
for _ in range(N):
    keyword = input().split()
    if len(keyword) == 1:
        if keyword[0] == 'pop':
            if len(d) != 0:
                result = d.popleft()
                print(result)
            else:
                print(-1)
        elif keyword[0] == 'size':
            print(len(d))
        elif keyword[0] == 'empty':
            if len(d) == 0:
                print(1)
            else:
                print(0)
        elif keyword[0] == 'front':
            if len(d) != 0:
                print(d[0])
            else:
                print(-1)
        elif keyword[0] == 'back':
            if len(d) != 0:
                print(d[-1])
            else:
                print(-1)
    else:
        num = keyword[1]
        d.append(num)