import math

lst = [x for x in range(10001)]
arr = []

for i in lst:
    cnt = 0
    for j in range(1, int(math.sqrt(i))+1):
        if i % j == 0:
            cnt += 1
    arr.append(cnt)

N = int(input())
print(sum(arr[:N:]))