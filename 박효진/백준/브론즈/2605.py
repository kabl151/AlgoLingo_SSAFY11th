import sys
input = sys.stdin.readline

N = int(input())
turn = list(map(int, input().split()))
sequence = []

for i in range(N):
    sequence.append(i+1)
    for j in range(turn[i]):
        sequence[-j-2], sequence[-j-1] = sequence[-j-1], sequence[-j-2]
print(*sequence)