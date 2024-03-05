N = int(input())
set_num = set(map(int, input().split()))
result = sorted(set_num)
print(*result)