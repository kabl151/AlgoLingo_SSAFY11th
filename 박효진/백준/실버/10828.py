N = int(input())
stack = []
for _ in range(N):
    keyword = input().split()
    if len(keyword) == 1:
        command = keyword[0]
        if command == 'pop':
            if len(stack) != 0:
                result = stack.pop()
                print(result)
            else:
                print(-1)
        elif command == 'size':
            print(len(stack))
        elif command == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif command == 'top':
            if len(stack) != 0:
                print(stack[-1])
            else:
                print(-1)
    else:
        num = keyword[1]
        stack.append(num)