import sys
input = sys.stdin.readline

arr = []
N = int(input())
for _ in range(N):
    m = int(input())
    arr.append(m)
arr.sort()
for i in range(N):
    print(arr[i])