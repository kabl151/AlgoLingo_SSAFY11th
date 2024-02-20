import sys
input = sys.stdin.readline
N = int(input())
result = []
num = 2
while N != 1:
    if N % num == 0:
        result.append(num)
        N = N // num
    else:
        num += 1
for i in range(len(result)):
    print(result[i])