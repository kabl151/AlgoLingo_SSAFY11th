n,m=map(int,input().split())   # n: 입력받을 정수의 개수, m: 연속된 구간의 크기 (10, 5)
arr=list(map(int,input().split()))

Max,sum=0,0

for i in range(m): # 처음 m개의 구간 (0번 인덱스부터 4번인덱스)의 합 구하기
    sum+=arr[i]

for i in range(n-m+1): 
    if sum>Max:
        Max=sum
    if i==n-m: break
    sum+=arr[i+m] # i+m: 5~10
    sum-=arr[i]   # i: 0~5

print(Max)