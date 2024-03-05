import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = sorted(A)
A = A[::-1]
B = sorted(B)
lst = []
for i in range(N):
    lst.append(A[i]*B[i])
print(sum(lst))