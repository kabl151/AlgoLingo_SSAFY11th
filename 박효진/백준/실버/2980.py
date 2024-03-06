import sys
input = sys.stdin.readline

N, L = map(int, input().split())
time = 0
wait = 0
sign = [0]
for i in range(N):
    arr = []
    D, R, G = map(int, input().split())
    for j in range(2000):
        for k in range(R):
            arr.append(False)
        for k in range(G):
            arr.append(True)
    sign.append(D)
    time += sign[-1] - sign[-2]
    while True:
        if arr[time] == True:
            break
        time += 1
        wait += 1
print(wait+L)