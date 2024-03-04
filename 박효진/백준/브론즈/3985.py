import sys
input = sys.stdin.readline

L = int(input())
N = int(input())
cake = [0]*(L + 1)
max_num = 0
expect_pp = 1
max_cnt = 0
pp_num = 0
for i in range(1, N + 1):
    start, end = map(int,input().split())
    cnt = 0
    if end - start > max_num:
        max_num = end - start
        expect_pp = i
    for j in range(start, end+1):
        if cake[j] == 0:
            cake[j] = i
            cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
        pp_num = i
print(expect_pp)
print(pp_num)
