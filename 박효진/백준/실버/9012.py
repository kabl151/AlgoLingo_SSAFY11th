import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(1, T+1):
    stack = []
    wd = input()
    for i in wd:
        if i == '(':
            stack.append(i)
        elif i == ')' and (len(stack) == 0 or stack[-1] != '('):
            stack.append(i)
        elif i == ')' and stack[-1] == '(':
            stack.pop()
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')