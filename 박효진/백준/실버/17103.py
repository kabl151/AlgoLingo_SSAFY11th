import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    # judge = [True] * (N+1)
    # judge[0] = False
    # judge[1] = False
    # sosu = []
    # for i in range(2, N+1):
    #     if judge[i] == True:
    #         sosu.append(i)
    #         judge[i] = False
    #         for j in range(i, N+1, i):
    #             judge[j] = False
    sosu = []
    for i in range(2,N+1):
        if N % i == 0:
            sosu.append(i)
    result = []
    for i in range(len(sosu)):
        for j in range(i, len(sosu)):
            result.append(sosu[i] + sosu[j])
    print(result.count(N))