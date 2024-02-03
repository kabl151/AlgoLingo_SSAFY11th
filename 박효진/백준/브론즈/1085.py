arr = input().split()
x = int(arr[0])
y = int(arr[1])
w = int(arr[2])
h = int(arr[3])

line_list = [x, y, h-y, w-x]
print(min(line_list))