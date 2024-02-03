N=int(input()) #치킨의 갯수
A,B=map(int,input().split())#콜라와 맥주갯수

def eat_chicken(chicken,colla,beer): #최소값을 반환하는 함수 
    return min(chicken,colla//2+beer)

print(eat_chicken(N,A,B))

