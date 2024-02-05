arr = []
N = int(input())

for i in range(1002):
    arr.append((2*i**2 - 2*i + 1))
for i in range(len(arr)):
    if N >= arr[i] and N <= arr[i+1]:
        result = i
print(result)
print(arr[result])


for i in range(1, 1000):
    for j in range(1, 1000):
        arr.append[i][j]