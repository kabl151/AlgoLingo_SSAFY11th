# # T = int(input())
# # for _ in range(1, T + 1):
# N, K = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# poss_cnt = 0
# for i in range(N):
#     for j in range(N):
#         cnt_a = 0
#         cnt_b = 0
#         if arr[i][j] == 1:
#             for k in range(N-i):
#                 cnt_a += arr[i+k][j]
#             if cnt_a == 2:
#                 poss_cnt += 1
#             else:
#                 pass
#             for l in range(N-j):
#                 cnt_b += arr[i][j+l]
#             if cnt_b == 2:
#                 poss_cnt += 1
#             else:
#                 pass
# print(poss_cnt)
# ----------------------
T = int(input())
for t in range(1,T+1):
    N,K = map(int,input().split())
    matrix = [[0]*(N+2)]*(N+2)
    answer = [0] + [1]*K +[0]
    cnt = 0 
   
    for i in range(1,N+1):
        n = list(map(int,input().split()))
        matrix[i] = [0]+ n +[0]
 
    for i in range(N-K+4):
        for j in range(N-K+1):
            lst = []
            for k in range(K+2):
                lst.append(matrix[i][j+k])
            if lst == answer:
                cnt +=1
    
    for i in range(N-K+1):
        for j in range(N-K+4):
            lst = []
            for k in range(K+2):
                lst.append(matrix[i+k][j])
            if lst == answer:
                cnt +=1
	  
    print(f'#{t} {cnt}')