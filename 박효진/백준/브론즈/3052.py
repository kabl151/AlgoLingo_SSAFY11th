arr = []
for _ in range(10):
    n = int(input())
    last_num = n % 42
    arr.append(last_num)
set_arr = set(arr)
print(len(list(set_arr)))