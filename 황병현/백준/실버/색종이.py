# 행렬 만들기
w = [[0 for i in range(100)]for j in range(100)]

# 좌표에 해당되는 범위 1로 채우기
n = int(input())
for _ in range(n):
    x, y = list(map(int,input().split()))
    for x_idx in range(x, x+10):
        for y_idx in range(y, y+10):
            w[x_idx][y_idx] = 1

# 1의 갯수 합
c = 0
for i in range(100):
    c += w[i].count(1)
    
print(c)