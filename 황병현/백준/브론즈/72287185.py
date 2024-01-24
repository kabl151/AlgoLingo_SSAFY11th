import sys
input = sys.stdin.readline

n, l = map(int,input().split())
a = list(map(int,input().split()))

a.sort()

for i in range(n):
    if l >= a[i]:
        l += 1
    else:
        break

print(l)