N = int(input())

lst = [0]
num = 1
result = 0
for i in range(20000):
    num = num + 6 * i
    lst.append(num)
for j in range(20000):
    if lst[j] >= N:
        result += j
        break
print(result)