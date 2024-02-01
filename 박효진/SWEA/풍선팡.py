# T = int(input())
# for t in range(1,T+1):
N,K = map(int,input().split())
arr = [[0]*(K+2)]*(N+2)
cnt = 0 
for i in range(1,N+1):
    n = list(map(int,input().split()))
    arr[i] = [0]+ n +[0]
max_num = 0
for i in range(1, N):
    for j in range(1, K):
        pass
    