# arr = [list(map(str, input())) for _ in range(5)]

# for i in range(15):
#     for j in range(15):
#         print(arr[j][i], end='')


#         -------------------------------
# empty_arr = [[['']*15] for _ in range(5)]
# arr = [list(map(str, input())) for _ in range(5)]
# empty_arr = arr
# max_len = 0
# for i in range(5):
#     if max_len <= len(arr[i]):
#         max_len = len(arr[i])

# for j in range(max_len):
#     for i in range(5):
#         empty_arr[j][i] = arr[i][j]

# print(empty_arr)

#         -------------------------------
# 전치행렬 될까?.. 빈공백있으면 실행안되는듯..
arr = [list(map(str, input())) for _ in range(5)]

max_len = 0
for i in range(5):
    if max_len <= len(arr[i]):
        max_len = len(arr[i])

empty_arr = [['']*max_len for _ in range(5)]

for i in range(5):
    for j in range(max_len):
        empty_arr[i][j] = arr[j][i]
print(empty_arr)