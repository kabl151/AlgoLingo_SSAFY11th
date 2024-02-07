# # 1. 먼저 괄호 개수가 맞는지 확인
# # 2. 괄호의 순서가 맞는지 확인 (1소괄호 열고 중괄호 닫기 x, 2중괄호 열고 소괄호 닫기 x)

# T = int(input())
# for tc in range(1, T+1):
#     wd = list(map(str, input()))
#     mid_lst_lft = []
#     mid_lst_rght = []
#     small_lst_lft = []
#     small_lst_rght = []
#     result = 1
#     # 1차 관문
#     for i in range(len(wd)):
#         if '{' in wd:
#             wd_idx = wd.index('{')
#             mid_lst_lft.append(wd_idx)
#         if '}' in wd:
#             wd_idx = wd.index('}')
#             mid_lst_rght.append(wd_idx)
#         if '(' in wd:
#             wd_idx = wd.index('(')
#             small_lst_lft.append(wd_idx)
#         if ')' in wd:
#             wd_idx = wd.index(')')
#             small_lst_rght.append(wd_idx)
#     if mid_lst_lft != mid_lst_rght or small_lst_lft != small_lst_rght:
#         result = 0
#     if '{' in wd and '}' in wd:
#         mid_wd_lft_idx = wd.index('{')
#         mid_wd_rght_idx = wd.index('}')
#         if '(' in wd[mid_wd_lft_idx:mid_wd_rght_idx]:
#             result = 0
#     if '(' in wd and ')' in wd:
#         small_wd_lft_idx = wd.index('(')
#         small_wd_rght_idx = wd.index(')')
#         if '{' in wd[small_wd_lft_idx:small_wd_rght_idx]:
#             result = 0
#     print(f'#{tc} {result}')







#     -------------------------------------------------

# T = int(input())
# for tc in range(1, T+1):
#     wd = list(map(str, input()))
#     wd_1 = wd.copy()
#     mid_lst_lft = []
#     mid_lst_rght = []
#     small_lst_lft = []
#     small_lst_rght = []
#     result = 1
#     # 1차 관문
#     for i in range(len(wd_1)):
#         if '{' in wd_1:
#             wd_idx = wd_1.index('{')
#             mid_lst_lft.append(wd_idx)
#             wd_1.pop(wd_idx)
#         if '}' in wd_1:
#             wd_idx = wd_1.index('}')
#             mid_lst_rght.append(wd_idx)
#             wd_1.pop(wd_idx)
#         if '(' in wd_1:
#             wd_idx = wd_1.index('(')
#             small_lst_lft.append(wd_idx)
#             wd_1.pop(wd_idx)
#         if ')' in wd_1:
#             wd_idx = wd_1.index(')')
#             small_lst_rght.append(wd_idx)
#             wd_1.pop(wd_idx)
#     if len(mid_lst_lft) != len(mid_lst_rght) or len(small_lst_lft) != len(small_lst_rght):
#         result = 0
    
#     for i in range(len(wd)):
#         if '{' in wd and '}' in wd:
#             mid_wd_lft_idx = wd.index('{')
#             mid_wd_rght_idx = wd.index('}')
#             if ')' in wd[mid_wd_lft_idx:mid_wd_rght_idx]:
#                 result = 0
#             else:
#                 wd.pop(mid_wd_rght_idx)
#                 wd.pop(mid_wd_lft_idx)
#     for i in range(len(wd)):
#         if '(' in wd and ')' in wd:
#             small_wd_lft_idx = wd.index('(')
#             small_wd_rght_idx = wd.index(')')
#             if '}' in wd[small_wd_lft_idx:small_wd_rght_idx]:
#                 result = 0
#             else:
#                 wd.pop(small_wd_rght_idx)
#                 wd.pop(small_wd_lft_idx)
#     print(f'#{tc} {result}')

#     --------------------------------------------------------

# T= int(input())
# for tc in range(1, T +1):
#     word = list(input())
#     new_stack = []
#     for i in word:
#         if i in ['(', ')', '{', '}']:
#             if i == ')' and len(new_stack) > 0 and new_stack[-1] == '(':
#                 new_stack.pop()
#             elif i == '}' and len(new_stack) > 0 and new_stack[-1] == '{':
#                 new_stack.pop()
#             else:
#                 new_stack.append(i)
#     if len(new_stack) == 0:
#         print(f'#{tc}', 1)
#     else:
#         print(f'#{tc}', 0)
# -------------------------------------------------------------------------------
T = int(input())
 
for tc in range(1, T+1):
    s = input()
    stack = []
    for i in s:
        if i == "{" or i == "(":
            stack.append(i)
        elif stack != 0 and i == "}" and stack[-1] == "{":
            stack.pop()
        elif stack != 0 and i == ")" and stack[-1] == "(":
            stack.pop()
        elif stack == 0 and (i == "}" or i == ")"):
            stack.append(i)
 
    if stack:
        answer = 0
    else:
        answer = 1
 
    print(f"#{tc}", answer)

-----------------------------------------------------------------
T = int(input())
for tc in range(1, T+1):
    wd = input()
    stack_lst = []
    for i in wd:
        if '{' == i or '(' == i:
            stack_lst.append(i)
        elif len(stack_lst) != 0 and '}' == i and stack_lst[-1] == '{':
            stack_lst.pop()
        elif len(stack_lst) != 0 and ')' == i and stack_lst[-1] == '(':
            stack_lst.pop()
        elif i == '}' or i == ')':
            stack_lst.append(i)
    if len(stack_lst) == 0:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')