############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_user_data_valid(user):
    pass
    # 여기에 코드를 작성합니다.
    # if else를 통해 경우 두개를 나누어 return 할 값을 정의한다
    if user['id'] == '' or user['password'] == '':
        return False
    else:
        return True
    
    # return을 한번만 써야한다면? 기존 판단 값을 True 로 해둔 다음 재할당한다
    result = True
    if user['id'] == '' or user['password'] == '':
        result = False
    else:
        pass
    return result
    

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': '',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data1)) # False 

user_data2 = {
    'id': 'jungssafy',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data2)) # True
#####################################################