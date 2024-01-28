# 치킨의 총 개수 N 할당
N = int(input())

# 콜라의 개수 A 와 맥주의 개수 B 할당
A, B = list(map(int, input().split()))

#접근
# 콜라를 2로 나눈 몫 만큼, 맥주의 개수 만큼 치킨을 먹을 수 있다.
# 1차적으로 콜라//2 + 맥주를 한 다음 2차적으로 치킨집의 개수를 파악
# 만약 1차적으로 구한 값이 치킨집의 치킨 개수보다 작다면 치킨 개수를 출력

# 2잔의 콜라와 1잔의 맥주로 먹을 수 있는 치킨 개수 할당
order_chicken = A // 2 + B
# if 문을 통해 치킨집의 개수를 확인 후 출력
if order_chicken >= N:
    print(N)
else:
    print(order_chicken)