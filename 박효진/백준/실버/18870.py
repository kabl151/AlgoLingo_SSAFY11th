import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
sorted_lst = sorted(list(set(lst)))
new_dct = {}
result = []
for i in range(len(sorted_lst)):
    dct = dict([(sorted_lst[i], i)])
    new_dct.update(dct)
for j in lst:
    result.append(new_dct[j])
print(*result)