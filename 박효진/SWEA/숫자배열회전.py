# T = int(input())
# for tc in range(1, T + 1):
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr_1 = [[0]* N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

for k in range(N):
    for l in range(N):
        arr_1[k][l] = arr[k][N-1-l]

arr_2 = [[0]* N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i < j:
            arr_1[i][j], arr_1[j][i] = arr_1[j][i], arr_1[i][j]

for k in range(N):
    for l in range(N):
        arr_2[k][l] = arr_1[k][N-1-l]


arr_3 = [[0]* N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i < j:
            arr_2[i][j], arr_2[j][i] = arr_2[j][i], arr_2[i][j]

for k in range(N):
    for l in range(N):
        arr_3[k][l] = arr_2[k][N-1-l]

print(arr_1)
print(arr_2)
print(arr_3)

# for i in range(N):
    # print(''.join(map(str, arr_1[i])), ''.join(map(str, arr_2[i])), ''.join(map(str, arr_3[i])))
for i in range(N):
    for j in range(N):
        print(f'{arr_1[j][i]}', end = '')    
    print()