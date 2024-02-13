#24.02.03
# import sys
# input = sys.stdin.readline

# arr = []
# N = int(input())
# for _ in range(N):
#     m = int(input())
#     arr.append(m)
# temp = [0] * len(arr)
# cnt = [0] * (max(arr)+1)

# for i in range(len(temp)):
#     cnt[arr[i]] += 1
# for j in range(1, len(cnt)):
#     cnt[j] += cnt[j-1]
# for k in range(len(arr)-1, -1, -1):
#     temp[cnt[arr[k]]-1] = arr[k]
#     cnt[arr[k]] -= 1

# for l in range(len(temp)):
#     print(temp[l])
# -------------------------------------------
import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * (10001)
num_lst = [ x for x in range(10001)]
for _ in range(N):
    num = int(input())
    arr[num] += 1

idx = 0
for i in arr:
    if i ==0:
        idx += 1
        continue
    else:
        for _ in range(i):
            print(num_lst[idx])
        idx += 1