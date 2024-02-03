N = int(input())
lst_1 = []
lst_2 = []
for i in range(1, N+1):
    lst_1.append((" " * (2*(N-1)))+ ('*' * (2*N-1)) + (" " * (2*(N-1))))
    print(*lst_1)

# for j in range(N):
#     lst_2 += " "+ ('*' * (2*N-1)) + " "
#     print(*lst_2)