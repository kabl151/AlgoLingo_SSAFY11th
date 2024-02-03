import sys
input = sys.stdin.readline
result = True

while result != False:
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[2] == 0:
        break
    elif arr[2] >= arr[0] + arr[1]:
        print('Invalid')
    elif arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[0]:
        print('Equilateral')
    elif arr[0] == arr[1] or arr[1] == arr[2]:
        print('Isosceles')
    elif arr[0] != arr[1] and arr[1] != arr[2]:
        print('Scalene')
