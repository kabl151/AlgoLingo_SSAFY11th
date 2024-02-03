# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     print(max(lst)-min(lst))

#---------------------------------------
# max, min 이 막힌다면?? bubble sort

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     for i in range(len(lst)-1,0,-1):
#         for j in range(0, i):
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#     print(lst[len(lst)-1] - lst[0])


#--------------------------------------

def Counting_Sort(arr, temp, cnt):
    # arr : 입력 리스트
    # temp : 흩뿌려지기 전 temp
    # cnt : 카운트 리스트
    for i in range(len(temp)):
        cnt[arr[i]] += 1
    for j in range(1, len(cnt)):
        cnt[j] += cnt[j-1]
    for k in range(len(arr)-1, -1, -1):
        temp[cnt[arr[k]]-1] = arr[k]
        cnt[arr[k]] -= 1
    return temp # 흩뿌려진 후 temp

arr = [1, 2, 0, 2, 3, 2, 4, 4, 1]
temp = [0] * len(arr)
k = [0] * (max(arr)+1)

print(Counting_Sort(arr, temp, k))

