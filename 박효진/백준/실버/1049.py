import sys
input = sys.stdin.readline

N, M = map(int, input().split())
set_item_lst = []
solo_item_lst = []
for i in range(M):
    set_item, solo_item = map(int, input().split())
    set_item_lst.append(set_item)
    solo_item_lst.append(solo_item)

set_num = N // 6
solo_plus = N % 6
if solo_plus != 0:
    set_num += 1

compare_num_1 = min(set_item_lst) * set_num
compare_num_2 = min(solo_item_lst) * N
if solo_plus != 0:
    compare_num_3 = solo_plus * min(solo_item_lst) + (set_num - 1) * min(set_item_lst)
else:
    compare_num_3 = solo_plus * min(solo_item_lst) + (set_num) * min(set_item_lst)

print(min(compare_num_1, compare_num_2, compare_num_3))