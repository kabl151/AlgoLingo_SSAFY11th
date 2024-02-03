# 과일의 개수 N, 뱀새의 초기길이 L 할당
N, L = list(map(int, input().split()))

# 먹이가 있는 높이 리스트를 할당
high_lst = list(map(int, input().split()))

# 먹이의 높이를 정렬
high_lst.sort()
# if 문을 통해 뱀새의 길이 보다 작은 높이에 먹이가 있다면 왼쪽부터 먹이 리스트를 제거, 뱀새의 길이 +1
# else로 더이상 해당하는 요소가 없다면 break로 빠져나온다
for i in range(len(high_lst)):
    if high_lst[0] <= L:
        high_lst.pop(0)
        L += 1
    else:
        break
# 늘어난 뱀새의 길이를 출력
print(L)
