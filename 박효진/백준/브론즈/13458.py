import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0
for i in range(N):
    if A[i] <= B:
        cnt += 1
    else:
        remain = A[i]-B
        cnt += 1
        if remain % C != 0:
            cnt += remain//C + 1
        elif remain % C == 0:
            cnt += remain//C
print(cnt)