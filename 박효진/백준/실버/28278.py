import sys
input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N):
    keyword = list(map(int, input().split()))
    if keyword[0] == 1:
        stack.append(keyword[1])
    elif keyword[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif keyword[0] == 3:
        print(len(stack))
    elif keyword[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif keyword[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)