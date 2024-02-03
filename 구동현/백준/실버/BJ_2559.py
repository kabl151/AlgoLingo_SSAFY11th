import sys
N, K = tuple(map(int,sys.stdin.readline().split()))
lst = list(map(int,sys.stdin.readline().split()))

# in total N days, sum each k days temp
# how to sum k days temp?
# use double for => start day and term
sum1 = sum(lst[:K])
max_s = sum1
for i in range(K,N):
    sum1 = sum1 - lst[i-K] + lst[i]
    if max_s <= sum1:
        max_s = sum1
print(max_s)