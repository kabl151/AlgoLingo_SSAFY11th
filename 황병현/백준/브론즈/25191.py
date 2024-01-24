import sys
input = sys.stdin.readline
chick = int(input())
coka, mac = map(int,input().split())

c = int(coka/2) + mac 
while True:
    if c <= chick:
        break
    else:
        c -= 1

print(c)