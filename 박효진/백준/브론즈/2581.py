M = int(input())
N = int(input())

lst = list(range(M, N+1))
num_lst = []
for i in lst:
    em_lst = []
    for j in range(1, i+1):
        if i % j == 0:
            em_lst.append(j)
    if len(em_lst) == 2:
        num_lst.append(i)
if num_lst == []:
    print(-1)
else:
    print(sum(num_lst))
    print(num_lst[0])