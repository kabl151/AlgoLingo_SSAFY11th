import sys
input = sys.stdin.readline

N = int(input())

lst = []
for i in range(1, N+1):
    test_i = i
    num = 0
    while test_i != 0:
        num += test_i % 10
        test_i = test_i // 10
    result = num + i
    if result == N:
        lst.append(i)
if len(lst) != 0:
    print(min(lst))
else:
    print(0)