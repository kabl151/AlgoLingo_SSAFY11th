arr = [list(map(int, input().split())) for _ in range(9)]

max_num = arr[0][0]
for i in range(9):
    for j in range(9):
        if arr[i][j] >= max_num:
            max_num = arr[i][j]
            max_i = i
            max_j = j

print(max_num)
print(max_i + 1, max_j + 1)