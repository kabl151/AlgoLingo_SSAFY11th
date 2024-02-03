############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# Python 내장함수 max() 사용 시 감점
def max_score(score_list):
    maxValue = score_list[0]
    for score in score_list:
        if score >= maxValue:
            maxValue = score
    return maxValue


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
scores1 = [30, 60, 90, 70]
print(max_score(scores1)) # 90
#####################################################