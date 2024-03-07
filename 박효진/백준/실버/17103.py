import sys
input = sys.stdin.readline

path = []
che = [True] * 1000001
che[0] = False
che[1] = False

for i in range(2,1000001):
    if che[i] == True:
        k = i
        i += k
        while i < 1000001:
            che[i] = False
            i += k

T = int(input())
for _ in range(T):
    N = int(input())
    result = 0
    sosu = []
    for i in range(2, N//2+1):
        if che[i] and che[N-i]:
            result += 1
    print(result)