# import sys
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     A, B = map(int, input().split())
#     set_A = set()
#     set_B = set()
#     for i in range(1, A+1):
#         if A % i == 0:
#             set_A.add(i)
#     for j in range(1, B+1):
#         if B % j == 0:
#             set_B.add(j)
#     if len(set_A & set_B) == 1:
#         print(A*B)
#     else:
#         print(A*B//max(set_A & set_B))

