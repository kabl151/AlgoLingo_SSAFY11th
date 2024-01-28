lst = [1,2,3,-4,20,6,7,8,9,10,12,8,7,6,5,4,3,2,1]

# min() 내장함수
def min_Number():
    minNum = lst[0]     # 리스트 첫째 값을 '기준 값'으로 설정
    for i in lst:       # lst 첫 번째 수부터 마지막 수 까지 순차적으로 이동.
        if i <= minNum: #lst 해당 요소가 minNum보다 같거나 작으면
            minNum = i  #해당 요소가 minNum으로 갱신
    return minNum       #리턴

def MAX_Number():
    maxNum = lst[0]     # 리스트 첫째 값을 '기준 값'으로 설정
    for i in lst:       # lst 첫 번째 수부터 마지막 수 까지 순차적으로 이동.
        if i >= maxNum: #lst 해당 요소가 maxNum보다 같거나 크면
            maxNum = i  #해당 요소가 maxNum으로 갱신
    return maxNum       #리턴

def lenght_Of_Iterable():
    cnt = 0         # count변수 cnt를 선언
    for i in lst:   # lst 첫 번째 수부터 마지막 수 까지 순차적으로 이동.
        cnt += 1    # count변수 cnt에 1씩 더해줌.
    return cnt      #리턴

def sum_Of_Commponets():
    tot = 0         # total 변수 tot를 0으로 선언.
    for i in lst:   # lst 첫 번째 수부터 마지막 수 까지 순차적으로 이동.
        tot += i    #순차적으로 오는 요소들(i)를 tot에 더해줌
    return tot      #리턴

def count_The_Target(target):
    cnt = 0             # count변수 cnt를 0으로 선언
    for i in lst:       # lst 첫 번째 수부터 마지막 수 까지 순차적으로 이동.
        if i == target: # 인자로 받은 target인자와 lst요소인 i가 같다면
            cnt += 1    # count변수 cnt에 1씩 더해줌
    return cnt          #리턴

def index_The_Target(target):
    cnt = -1
    for i in lst:
        cnt += 1
        if i == target:
            break #맨 왼쪽 부터 서치해서 처음 등장하는 대상의 인덱스 반환이기 때문에 'break'가 핵심임.
    return cnt

print(min_Number())
print(MAX_Number())
print(lenght_Of_Iterable())
print(sum_Of_Commponets())
print(count_The_Target(20))
print(index_The_Target(20))