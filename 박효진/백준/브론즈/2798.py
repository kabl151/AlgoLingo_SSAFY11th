import sys
input = sys.stdin.readline

N, M = map(int, input().split())

card = list(map(int, input().split()))
num_lst = []
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1, N):
            num_lst.append(card[i] + card[j] + card[k])
num_lst.sort()
if len(num_lst) == 1:
    print(num_lst[0])
elif M in num_lst:
    print(M)
else:
    num_lst.append(M)
    num_lst.sort()
    idx = num_lst.index(M)
    print(num_lst[idx-1])