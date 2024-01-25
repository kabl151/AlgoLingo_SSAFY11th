import sys
N, L = list(map(int,sys.stdin.readline().rstrip().split()))
lst = list(map(int,sys.stdin.readline().rstrip().split()))

lst.sort()
for i in lst:
    if L >= i:
        L +=1
    else:
        pass
print(L)