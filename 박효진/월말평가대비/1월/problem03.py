############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count() 를 사용시 감점
def menu_count(restorant_dict):
    pass
    # 여기에 코드를 작성합니다.
    # 1. dictionary의 key 값을 통해 접근 후 해당 리스트의 데이터 길이 측정
    return len(restorant_dict['menus'])

    # 민수 코드
    cnt = 0
    for i in restorant_dict['menus']:
        cnt += 1
    return cnt
    # 2. 만약 len까지 금지먹는다면?
    # while 을 통해 list가 빈 리스트가 될때까지 =False 조건? 

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
restorant1 = {
    "id": 11,
    "user_rating": 5.5,
    "name": "김밥나라",
    "menus": ["참치김밥", "치즈라면", "돈까스", "비빔밥"],
    "location": "서울특별시 강남구 역삼동 123-123"
}
print(menu_count(restorant1)) # 4
#####################################################