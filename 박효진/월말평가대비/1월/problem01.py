############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# Python 내장함수 max() 사용 시 감점
def max_score(score_list):
    pass
    # 여기에 코드를 작성합니다.
    # score_list에 들어온 list들의 index 비교하여 
    # 마지막 데이터 하나가 남을 때까지 작은수는 pop으로 제거하고
    # 해당 데이터를 return해준다

    # 반복문 while을 통해 score_list 의 갯수가 한개 남을 때까지 돌린다 의미
    while len(score_list) != 1:
        if score_list[0] >= score_list[1]:
            score_list.pop(1)
        else:
            score_list.pop(0)
    return score_list[0]

def max_score(score_list):
    pass
    # 여기에 코드를 작성합니다.
    # 반복문 for을 통해 정해진 횟수 만큼 돌린다는 의미
    for i in range(len(score_list) - 1):
        if score_list[0] >= score_list[1]:
            score_list.pop(1)
        else:
            score_list.pop(0)
    return score_list[0]


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
scores1 = [30, 60, 90, 70]
print(max_score(scores1)) # 90
#####################################################