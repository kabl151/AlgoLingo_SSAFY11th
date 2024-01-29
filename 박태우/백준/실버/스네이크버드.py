N, L = map(int,input().split()) #과일의 갯수 n,스네이크버드 초기길이정수 l설정

high = list(map(int,input().split())) #과일의 높이 
high.sort() #과일의 높이를 오름차순으로 정렬
for i in range(N):  #과일의 갯수만큼 반복문
    if high[i] <= L: #과일을 하나 먹을때마다 길이 1증가 시키기
        L += 1
    else:
        break
print(L)