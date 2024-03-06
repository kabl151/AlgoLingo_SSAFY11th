import sys
input = sys.stdin.readline

def permutation(n):
    if len(result):
        return
    if n == 7:
        if sum(path) == 100:
            result.append(path[:])
        return
    for i in range(9):
        if used[i] == False:
            used[i] = True
            path.append(arr[i])
            permutation(n+1)
            path.pop()
            used[i] = False
arr = []
result = []
path = []
used = [False]*9
for i in range(9):
    arr.append(int(input()))

permutation(0)
result[0].sort()
for i in range(7):
    print(result[0][i])