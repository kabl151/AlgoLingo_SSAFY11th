# N = int(input())
# lst_1 = []
# lst_2 = []
# for i in range(1, N+1):
#     lst_1.append((" " * (2*(N-1)))+ ('*' * (2*N-1)) + (" " * (2*(N-1))))
#     print(*lst_1)

# for j in range(N):
#     lst_2 += " "+ ('*' * (2*N-1)) + " "
#     print(*lst_2)

N = int(input())
for i in range(1, N+1):
    print(' '*abs(N-i), '*' * (2*i - 1), sep ='')
for j in range(N-1, -1, -1):
    print(' '*abs(N-j), '*' * (2*j - 1), sep ='')