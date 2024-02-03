num_list = []
for i in range(5):
    n = int(input())
    num_list += [n]

result_1 = sum(num_list) / 5
print(int(result_1))
num_list.sort()
print(num_list[2])