import sys
input = sys.stdin.readline

N, M = map(int, input().split())
wd_lst = []
tst_lst = []
cnt = 0
for _ in range(N):
    wd = input()
    wd_lst.append(wd)
for _ in range(M):
    tst = input()
    tst_lst.append(tst)
for i in tst_lst:
    if i in wd_lst:
        cnt += 1
print(cnt)