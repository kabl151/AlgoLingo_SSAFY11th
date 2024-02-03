# 콜라2 -> 치킨1 or 맥주1 -> 치킨1 가능
# 즉, (보유콜라/2 의 몫) + (보유맥주/1의 몫) = 가능한 치킨 최대 수

N = int(input())    # 총 치킨 개수
lst = list(map(int, input().split()))

cola = lst[0] // 2
beer = lst[1]

chicken = cola + beer   # 가능한 치킨 최대 개수

# 총 개수 > 가능한 치킨 개수 -> 가능한 치킨 다 먹으면 됨 (chicken = chicken)
# 총 개수 < 가능한 치킨 개수 -> 총 개수까지만 먹을 수 있음 (ckicken = N)
if N < chicken :
    chicken = N
print(chicken)