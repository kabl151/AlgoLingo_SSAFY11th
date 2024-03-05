import sys
input = sys.stdin.readline

N = int(input())
deque = []
for _ in range(N):
    keyword = input().split()
    if len(keyword) == 1:
        command = keyword[0]
        if command == 'pop_front':
            if len(deque) != 0:
                result = deque.pop(0)
                print(result)
            else:
                print(-1)
        if command == 'pop_back':
            if len(deque) != 0:
                result = deque.pop()
                print(result)
            else:
                print(-1)
        elif command == 'size':
            print(len(deque))
        elif command == 'empty':
            if len(deque) == 0:
                print(1)
            else:
                print(0)
        elif command == 'front':
            if len(deque) != 0:
                print(deque[0])
            else:
                print(-1)
        elif command == 'back':
            if len(deque) != 0:
                print(deque[-1])
            else:
                print(-1)
    else:
        command = keyword[0]
        num = keyword[1]
        if command == 'push_front':
            deque.insert(0, num)
        elif command == 'push_back':
            deque.append(num)