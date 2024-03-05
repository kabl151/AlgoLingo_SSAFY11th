def recursion(N):
    global result
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4
    return recursion(N-3) + recursion(N-2) + recursion(N-1)

T = int(input())
for tc in range(T):
    result = 0
    N = int(input())
    print(recursion(N))