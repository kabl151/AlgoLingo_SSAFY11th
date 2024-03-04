import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
stack = []
result = [-1]
lst.reverse()
stack.append(lst[0])
for i in range(N-1):
    if lst[i] > lst[i+1]:
        result.append(stack[0])
        print(stack)
    elif lst[i] < lst[i+1] and lst[i+1] <= stack[0]:
        result.append(stack[0])
        stack.pop()
        stack.append(lst[i+1])
    elif lst[i] < lst[i+1] and lst[i+1] > stack[0]:
        result.append(-1)
        stack.pop()
        stack.append(lst[i+1])
result.reverse()
print(*result)
'''
stack 4
321234
'''