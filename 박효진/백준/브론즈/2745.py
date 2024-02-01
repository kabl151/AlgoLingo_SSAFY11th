arr = input().split()
n = arr[0]
b = int(arr[1])
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

num = []
for i in n:
    num += [lst.index(i)+1]

total_num = 0
for j in range(len(num),1,-1):
    total_num += b**j

print(total_num)
