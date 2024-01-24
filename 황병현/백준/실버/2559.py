import sys
input = sys.stdin.readline
n, k = map(int,input().split())
l = list(map(int,input().split()))

slc = sum(l[:k])
result = slc

for i in range(n-k):
    slc += l[i+k] - l[i]
    result = max(result,slc)
    
print(result)