# 스네이크 버드
# 과일+1 --> 길이+1

# 과일의 개수 N
# 길이 L
# 과일의 높이 height

# 자신보다 작거나 같은 높이에 있는 과일들만 먹을 수 있음
# 스네이크 버드 최대길이는?

N, L = map(int, input().split())
height = list(map(int, input().split()))

# 높이가 낮은 과일 순으로 먹어야 최대길이를 구할 수 있으므로 정렬 
height_arr = sorted(height)


# 높이가 낮은 과일부터 순차적으로 순회하면서 과일 먹음
# 과일 먹는다 = 길이 + 1 된다.
# 따라서 길이 L이 높이 i보다 같거나 클 경우, 길이 +1 해줌

for i in height_arr :           
    if L >= i :
        L += 1
print(L)
