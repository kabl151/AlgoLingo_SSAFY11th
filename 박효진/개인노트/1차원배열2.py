
# lst = [1, 2, 3]

# for i in range(1, 4):           # 잘못된 구현 예시
#     for j in range(1, 4):
#         for k in range(1, 4):
#             print(i, j, k)      # 해당 출력은 리스트 요소들의 중복을 포함해버린다 ex)1 1 1
# ----------------------------------------------------------------------------------------------------------------
# for i in range(1, 4):           # 제대로된 구현 예시
#     for j in range(1, 4):
#         if j != i:                    # 1번째, 2번째 데이터가 다르다는 조건을 걸어준다
#             for k in range(1,4):
#                 if k != i and k != j: # 1, 2, 3 번째 데이터가 다르다는 조건을 걸어준다
#                     print(i, j, k)

# # 1 2 3
# # 1 3 2
# # 2 1 3
# # 2 3 1
# # 3 1 2
# # 3 2 1

# num = 123123                # Baby Gin 확인할 6자리 수
# cnt_lst = [0] * 12          # 6자리 수로부터 각 자리를 카운트 하기 위한 빈 배열 생성(12개를 생성하는 이유는 하단에)
# for i in range(6):          # 해당 과정은 주어진 정수를 나누어 뿌려주기 위한 과정이며 오른쪽부터 뿌린다.
#     cnt_lst[num % 10] += 1  # 인덱스에 맞춰 카운트를 높여준다
#     num //= 10              # 10으로 나누어 자리수를 바꾸어준다

# k = 0                       # 반복문 while을 돌리기 위한 변수 설정
# tri = run = 0               # 초기 triple과 run 횟수를 0으로 설정

# # triple을 확인하기 위한 반복문 작성
# while k < 10:               # k가 10보다 작다면 계속 도는 반복문 조건 설정
#     if cnt_lst[k] == 6:     # 6개일 경우 tri += 2  <-3의 배수로 나누어 몫을 tri += 할당해도된다
#         cnt_lst[k] -= 6     
#         tri += 2
#     if cnt_lst[k] >= 3:     # 3개일 경우 tri +=1
#         cnt_lst[k] -= 3
#         tri += 1
#     k += 1                  # 구성된 데이터를 모두 돌면 탈출하기 위한 조건 k에 +1

# # run을 확인하기 위한 반복문 작성
# k = 0 # k를 초기화 해줘야 위의 반복문과 겹치지 않는다. 
# while k < 10:
#     if cnt_lst[k] == 2 and cnt_lst[k+1] == 2 and cnt_lst[k+2] == 2: # run의 조건을 확인 123123일 경우
#         cnt_lst[k] -= 2
#         cnt_lst[k+1] -= 2   # 아까 cnt_lst의 0 요소를 12개 추가해준 이유가 여기서 나오게된다
#         cnt_lst[k+2] -= 2   # 추가해주지 않는다면 out of range
#         run += 2            # 연속된 데이터가 2개씩 있을 경우 run += 2
#     if cnt_lst[k] == 1 and cnt_lst[k+1] == 1 and cnt_lst[k+2] == 1: # run의 조건을 확인
#         cnt_lst[k] -= 1
#         cnt_lst[k+1] -= 1
#         cnt_lst[k+2] -= 1
#         run += 1            # 연속된 데이터가 있을 경우 run += 1
#     k += 1

# if run + tri == 2: # Baby-gin을 확인
#     print("Baby Gin")
# else:
#     print("Lose")
