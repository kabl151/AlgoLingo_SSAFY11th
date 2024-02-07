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
A, B, V = map(int, input().split())

result = (V - A) / (A - B) + 1
if result == int(result):
    print(int(result))
else:
    print(int(result + 1))