N = int(input())
arr = list(map(int, input().split()))
cor_lst = []
cnt = 0
for i in arr:
    lst = []
    for j in range(1, i+1):
        if i % j == 0:
            lst.append(j)
    if len(lst) == 2:
        cnt += 1

print(cnt)