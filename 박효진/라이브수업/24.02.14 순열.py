# 순열 생성
# 미리 P 에 1, 2, 3 을 담은 상태에서 시작
# P[0] 1은 그대로 놔둔다 = 1은 1과 자리를 바꾼다
# P[1] 2역시 그대로 둔다
# P[2] 3역시 그대로 둔다 > 완성 너 P[3]과 자리 바꿔볼래 없네?
# 다시 한단계P[1]로 올라가서 너 P[2]랑 자리바꿔봐
# 그럼 P[1]은 값을 받고, 다시 P[2]를 결정하자
# P[2]는 또 자기 자신이랑만 바꾸네

def f(i, k):
    if i==k:
        print(*P)
    else:
        for j in range(i, k):    # P[i] 자리에 올 원소 P[j] 결정
            P[i], P[j] = P[j], P[i] # 자리 교환
            f(i+1, k)
            P[i], P[j] = P[j], P[i] # 위의 교환한 것 이후 다시 복구
            
N = 3
P = [0,1,2]
f(0, N) # 0번부터 시작하고 총 개수는 3개다
# # -----------------------------------------
# def f(i, k):
#     global min_v
#     global cnt
#     cnt += 1
#     if i==k:
#         s = 0       #선택한 원소의 합. 아래 for문은 합을 구하는 과정
#         for j in range(k):      # j 행에 대해   
#             s += arr[j][P[j]]   # j 행에서 P[j]열을 고른 경우
#         if min_v > s:
#             min_v = s
#     else:
#         for j in  range(i, k):
#             P[i], P[j] = P[j], P[i] # 자리 교환
#             f(i+1, k)
#             P[i], P[j] = P[j], P[i]

# N = int(input())
# arr = [list(map(int, input().split()))for _ in range(N)]
# P = [x for x in range(N)]
# cnt = 0
# min_v = 100
# f(0, N)
# print(min_v, cnt)

# # -----------------------------------------

# def f(i, k, s):
#     global cnt
#     global min_v
#     cnt += 1
#     if i==k:
#         if min_v > s:
#             min_v = s
#     elif s >= min_v:
#         return
#     else:
#         for j in  range(i, k):
#             P[i], P[j] = P[j], P[i] # 자리 교환
#             f(i+1, k, s+arr[i][P[i]])
#             P[i], P[j] = P[j], P[i]

# N = int(input())
# arr = [list(map(int, input().split()))for _ in range(N)]
# P = [x for x in range(N)]
# min_v = 100
# cnt = 0
# f(0, N, 0)
# print(min_v, cnt)




