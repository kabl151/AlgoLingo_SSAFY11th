import sys
input = sys.stdin.readline

N = int(input())
lst = []
r_lst = []
result_lst = []
cnt = 0
for _ in range(N):
    lst.append(int(input()))
while cnt != lst[-1]:
    cnt += 1
    r_lst = [i for i in range(lst[0], lst[-1]+1, cnt)]
    if set(lst) & set(r_lst) == set(lst):
        result_lst.append(len(set(r_lst)) - len(set(lst)))
print(min(result_lst))