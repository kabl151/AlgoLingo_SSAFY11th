# import sys
# input = sys.stdin.readline

# N = int(input())
# lst = []
# r_lst = []
# result_lst = []
# cnt = 0
# for _ in range(N):
#     lst.append(int(input()))
# while cnt != lst[-1]:
#     cnt += 1
#     r_lst = [i for i in range(lst[0], lst[-1]+1, cnt)]
#     if set(lst) & set(r_lst) == set(lst):
#         result_lst.append(len(set(r_lst)) - len(set(lst)))
# print(min(result_lst))


import sys
input = sys.stdin.readline
import math

N = int(input())
st = set()
a = int(input())
for _ in range(N-1):
    b = int(input())
    st.add(b-a)
    a = b

result = math.gcd(*st)

solve = [x for x in range(min(st), max(st)+1, result)]
print(len(solve)-N)