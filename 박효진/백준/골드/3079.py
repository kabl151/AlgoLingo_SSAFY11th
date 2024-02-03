import sys

N, M = map(int, sys.stdin.readline().split())
lst = []
for i in range(N):
    Tk = int(sys.stdin.readline())
    lst.append(Tk)
cnt = 0
second = 0

while M+N != cnt:
    for j in lst:
        if second % j == 0:
            cnt += 1
        if M+N == cnt:
            break
    second +=1
print(second-1)


# ---------------------------------

import sys

N, M = map(int, sys.stdin.readline().split())
lst = []
for i in range(N):
    Tk = int(sys.stdin.readline())
    lst.append(Tk)
cnt = 0
second = 0

for time in range(10**18):
    for j in lst:
        if second % j == 0:
            cnt += 1
        if M+N == cnt:
            break
    if M+N == cnt:
        break    
    second +=1
print(second)
