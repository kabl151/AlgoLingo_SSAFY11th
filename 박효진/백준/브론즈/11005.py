n, b = map(int, input().split())
num_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lst = []
result_lst = []
while True:
    result = n % b
    lst.append(result)
    if n >= b:
        n = n // b
    else:
        break
lst = lst[::-1]

for i in lst:
    result_lst.append(num_lst[i])

print(*result_lst, sep='')