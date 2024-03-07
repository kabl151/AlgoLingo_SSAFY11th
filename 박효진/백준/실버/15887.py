N = int(input())
lst = list(map(int, input().split()))
L_idx = 0
R_idx = 0
result = []
cnt = 0
for i in range(N):
    if lst[i] != i+1:
        L_idx = i
        for j in range(i+1, N):
            if lst[j] == j+1:
                R_idx = j
                cnt += 1
                result.append([i,j])
                break
print(cnt)
for i in range(len(result)):
    print(result[i])