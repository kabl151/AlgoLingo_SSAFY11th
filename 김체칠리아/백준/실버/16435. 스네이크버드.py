'''
# 16435. 스네이크버드
#1

3 10
10 11 13             #12

#2

9 1
9 5 8 1 3 2 7 6 4    #10
'''

fruits_cnt_and_snakebird_len= list(map(int, input().split()))
num = list(map(int, input().split()))

fruits_cnt = int(fruits_cnt_and_snakebird_len[0])
snakebird_len = int(fruits_cnt_and_snakebird_len[1])
num.sort()                                        # input받아와 가공한 정수 리스트를 정렬함 #[10, 11, 13]
# print(num)   #[10, 11, 13]

for i in range(len(num)):  # num을 순회하면서 밑의 코드를 계속 돌림
    if num[i] <= snakebird_len:  # snakebird_len보다 적거나 같은(이하)수가 나오면,
        snakebird_len += (num[i] - snakebird_len + 1) # 'snakebird_len + (num[i] - snakebird_len + 1)'를 snakebird_len에 업데이트(벌새의 길이 이하의 과일 하나 먹을 때마다 벌새의 길이가 +1)
print(snakebird_len)    # 그렇게 성장한 벌새의 길이를 출력


#(read.me)
# 오류 msg : input값 입력했는데,   File "<stdin>", line 1 뜨는 경우 → (컨트롤 + z) 누른 후 다시 실행

