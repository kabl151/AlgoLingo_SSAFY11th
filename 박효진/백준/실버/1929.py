# 에라토스테네스의 체
# 주어진 범위의 숫자를 리스트화 시켜놓고 2의배수 3의배수 등등 다 지운다
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
lst = [x for x in range(1000001)]
final_lst = []
result_lst = [True]*1000001
result_lst[0] = False
result_lst[1] = False
for i in range(2, 1000001):
    if result_lst[i] == True:
        final_lst.append(lst[i])
        for j in range(i, 1000001,i):
            result_lst[j] = False
for k in final_lst:
    if M <= k <= N:
        print(k)