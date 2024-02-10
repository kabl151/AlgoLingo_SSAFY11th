import sys
input = sys.stdin.readline

N = int(input())
que = []
for _ in range(N):
    keyword = input().split()
    if len(keyword) == 1:
        if keyword[0] == 'pop':
            if len(que) != 0:
                result = que.pop(0)
                print(result)
            else:
                print(-1)
        elif keyword[0] == 'size':
            print(len(que))
        elif keyword[0] == 'empty':
            if len(que) == 0:
                print(1)
            else:
                print(0)
        elif keyword[0] == 'front':
            if len(que) != 0:
                print(que[0])
            else:
                print(-1)
        elif keyword[0] == 'back':
            if len(que) != 0:
                print(que[-1])
            else:
                print(-1)
    else:
        num = keyword[1]
        que.append(num)