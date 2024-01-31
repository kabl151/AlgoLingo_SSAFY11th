'''
# 25191. 치킨 댄스를 추는 곰을 본 임스
#1

5
4 2    # 4


#2
3
4 2     # 3
'''

# input값을 리스트로 받기
chicken_lst = list(map(int, input().split()))
cola_and_beer_lst = list(map(int, input().split()))
chicken = int(chicken_lst[0])
cola = int(cola_and_beer_lst[0])
beer = int(cola_and_beer_lst[1])

if ((cola//2) + beer) <= chicken:   # (cola 나누기 2한 몫 + beer) 의 값이 chicken의 range 내에 있으면 그 숫자를 출력
    print(int(cola//2 + beer))
else:
    print(int(chicken))    # 아니라면 chicken의 값을 그대로 출력