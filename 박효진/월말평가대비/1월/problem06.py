############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_id_valid(user):
    pass
    # 여기에 코드를 작성합니다.
    # 마지막 글자가 숫자인지 판단하는 판단 
    # pop을 통해 반환받은 해당 글자가 숫자인지 알파벳인지 확인한다(isalpha)
    # 한글은 판단 못하므로 
    # isnumeric을 통해 판단해보자
    # index 위치는 -1로 한다
    # is 함수는 return 값이 있기 때문에 반환 받아서 확인해야한다
    word = user['id'][-1]
    number_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if word in number_lst:
        return True
    else:
        return False

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': 'jungssafy5',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data1)) # True

user_data2 = {
    'id': 'kimssafy!',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data2)) # False
#####################################################