'''
3
21 Junkyu
21 Dohyun
20 Sunyoung
'''

# N = int(input())

# arr = [list(map(str, input().split())) for _ in range(N)]

# for i in range(len(arr)-1, 0, -1):
#     for j in range(i):
#         if int(arr[j][0]) > int(arr[j+1][0]):
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# for i in range(len(arr)):
#     result = arr[i]
#     print(*result)

N = int(input())
arr = []
for i in range(N):
    num, name = map(str,input().split())
    num = int(num)
    lst = [num, name]
    arr += [lst]

arr.sort()
for i in range(N):
    result = arr[i]
    print(*result)