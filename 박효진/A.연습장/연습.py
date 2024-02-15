# set = {'1', '2', '3'}
# for i in range(5):
#     print(set)
# arr = [1, 2, 3]
# max_num_idx = 1
# while len(arr) != 0:
#     arr = arr[max_num_idx::]
# print(arr)
# wd = list(map(str, input()))
# print(wd)

# for tc in range(2):
#     wd = input()
#     wd_lst = []
#     for i in wd:
#         if i == "(":
#             wd_lst.append(i)
#         elif len(wd_lst) != 0 and i == ")" and wd_lst[-1] == "(":
#             wd_lst.pop(-1)
#         elif i == ")":
#             wd_lst.append(i)
#     if len(wd_lst) == 0:
#         print(True)
#     else:
#         print(False)

# lst = [1,2] + [3]
# print(lst)

# print(lst[-2:-1:1])

# arr = input().split()
# print(arr[0])
# print(arr[1])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(str, input().split()))
    suf_lst = []
    if N % 2 == 0:
        for i in range(N//2):
            suf_lst.append(arr[i])
            suf_lst.append(arr[i+N//2])
    else:
        for i in range(N//2):
            suf_lst.append(arr[i])
            suf_lst.append(arr[i+N//2+1])
        suf_lst.append(arr[N//2])
    print(f'#{tc}', *suf_lst)

#-------------------------------------------

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(str, input().split()))