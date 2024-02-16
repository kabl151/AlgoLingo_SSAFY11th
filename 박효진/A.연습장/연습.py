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

N = int(input())
arr = [x for x in range(1, N+1)]
lst = []
for i in arr:
    if '3' in str(i):
        i = str(i).replace('3','-')
    if '6' in str(i):
        i = str(i).replace('6','-')
    if '9' in str(i):
        i = str(i).replace('9','-')
    if '-' in str(i):
        num = str(i).count('-')
        print('-'*num, end = ' ')
    else:
        print(i, end = ' ')
