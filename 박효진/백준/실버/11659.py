# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# arr = list(map(int, input().split()))


# for i in range(M):
#     sum_num = 0
#     x, y = map(int, input().split())
#     for j in range(y-x+1):
#         sum_num += arr[x-1]
#         if x == y:
#             print(sum_num)

#------------------------------------
            
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# arr = list(map(int, input().split()))

# for i in range(M):
#     x, y = map(int, input().split())
#     print(sum(arr[x-1:y]))

#------------------------------------
            
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_lst = [0] * 100001
sum_lst[0] = arr[0]
for i in range(1, N):
    sum_lst[i] = arr[i] + sum_lst[i-1]

for i in range(M):
    x, y = map(int, input().split())
    if x == 1:
        print(sum_lst[y-1])
    elif x == y:
        print(arr[x-1])
    else:
        print(sum_lst[y-1]-sum_lst[x-2])