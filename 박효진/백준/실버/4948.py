import sys
input = sys.stdin.readline

result = []
judge = [True] * 250001
judge[0] = False
judge[1] = False
for i in range(2, 250001):
    if judge[i] == True:
        result.append(i)
        for j in range(i, 250001, i):
            judge[j] = False

while True:
    N = int(input())
    if N == 0:
        break
    else:
        num_lst = []
        for i in result:
            if N < i <= 2 * N:
                num_lst.append(i)
        print(len(num_lst))
