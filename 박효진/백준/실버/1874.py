# import sys
# input = sys.stdin.readline
# num_lst = []
# real_lst = []
# ans_lst = []
# N = int(input())
# idx = 0 # 커서의 위치
# lst = [x for x in range(N + 1)]
# result = 1
# for i in range(N):
#     num = int(input())
#     num_lst.append(num)
#     real_lst.append(num)
# max_num_idx = num_lst.index(N)
# num_lst = num_lst[max_num_idx::]
# for i in range(len(num_lst)-1):
#     if num_lst[i] > num_lst[i+1]:
#         continue
#     else:
#         result = 0
# if result == 1:
#     for i in real_lst:
#         while True:
#             if i > lst[idx]:
#                 ans_lst.append('+')
#                 idx += 1
#             elif i == lst[idx]:
#                 ans_lst.append('-')
#                 lst.pop(idx)
#                 idx -= 1
#                 break
#             elif i < lst[idx]:
#                 ans_lst.append('-')
#                 idx -= 1
#     for i in range(len(ans_lst)):
#         print(ans_lst[i])
# else:
#     print('NO')

# -----------------------------------------------------
N = int(input())
stack = []
ans_lst = []
cnt = 1
result = 1
for _ in range(N):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        ans_lst.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        ans_lst.append('-')
    else:
        result = 0
if result == 0:
    print('NO')
else:
    for i in range(len(ans_lst)):
        print((ans_lst[i]))