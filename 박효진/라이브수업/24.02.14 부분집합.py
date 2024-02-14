def f(i, k, t):     # k개 원소를 가진 배열A에서 부분집합의 합이 t인 경우
    if i==k:    # 모든 원소에 대해 결정하면
        sum = 0 # 부분집합 원소의 합
        for j in range(k):
            if bit[j]:     # (= bit[i]가 존재한다면) = A[i]가 포함된 경우
                sum += A[j]
        if sum == t:
            for j in range(k):
                if bit[j]:
                    print(A[j], end = ' ')
            print()
    else:
        for j in range(1,-1,-1):
            bit[i] = j
            f(i+1, k, t)
        # bit[i] = 1  #<< 위와 같은식. for문으로 묶은경우와 아닌 경우를 나눈것
        # f(i+1, k, t)
        # bit[i] = 0
        # f(i+1, k, t)
N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0]*N     # bit[i]는 A[i]가 부분집합에 포함되는지
f(0, N, 10) # target = 10


# 추가 설명 : 뒤의 원소에 -원소가있다면 합을 찾을때 끝까지 가야함
# --------------------------------------------


# 이미 합이 초과된 상태에서 더이상 실행하지 않기위한 방법으로
# S라는 값을 같이 포함시켜 재귀하면서 넘어가는 순간 실행하지 않게

#def (i, N, s, t):    # s는 합을 구하는 것이기때문에 사용 t는 갯수를 찾을 때 사용

def f(i, k, s, t):     # k개 원소를 가진 배열A에서 부분집합의 합이 t인 경우
    global cnt
    cnt += 1
    if s==t:            # 목표값에 도착했으면
        for j in range(k):
            if bit[j]:
                print(A[j], end = ' ')
        print()
    elif i == k: # 모든 원소를 고려했으나 s != t 인 경우
        return
    elif s > t: # 고려한 원소의 합이 t보다 큰 경우
        return
    else:
        bit[i] = 1  #<< 위와 같은식. for문으로 묶은경우와 아닌 경우를 나눈것
        f(i+1, k, s+A[i], t)
        bit[i] = 0
        f(i+1, k, s, t)

N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0]*N     # bit[i]는 A[i]가 부분집합에 포함되는지
cnt = 0     # 호출횟수 카운트 변수
f(0, N, 0, 1) # target = 10
print(cnt)