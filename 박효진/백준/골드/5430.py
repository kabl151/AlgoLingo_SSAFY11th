import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for tc in range(1,T+1):
    try:
        oper = input()
        n = int(input())
        arr = str(input())
        lst = deque()
        for i in arr:
            if i.isdigit():
                lst.append(int(i))
        cnt = 0
        for i in oper:
            if i == 'R':
                cnt += 1
            elif i == 'D':
                if cnt % 2 == 0:
                    lst.popleft()
                    cnt = 0
                else:
                    lst.pop()
                    cnt = 0
        if lst == deque():
            print('error')
        else:
            if cnt % 2 == 0:
                print('[', end = '')
                print(*lst, sep = ',', end = '')
                print(']')
            else:
                lst.reverse()
                print('[', end = '')
                print(*lst, sep = ',', end = '')
                print(']')
    except IndexError:
        print('error')