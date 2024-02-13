import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
arr.sort()

if arr[0] + arr[1] <= arr[2]:
    arr[2] = arr[1] + arr[0] - 1
else:
    pass

print(arr[0]+arr[1]+arr[2])