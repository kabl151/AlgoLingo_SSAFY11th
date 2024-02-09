# arr = []
# N = int(input())
# for i in range(20):
#     arr.append(i**2 + (i+1)**2)
# # for i in arr:
# #     if 
# print(arr)

arr = [[0]*22 for _ in range(22)]

arr[1][1] = 1
arr[1][2] = 2
arr[2][1] = 3
dx = [0, 1, 1, -1]  #우 하대각 하 상대각
dy = [1, -1, 0, 1]
for i in range(1,10000001):
    pass