# 비어있는 dictionary 생성
dict_test_a = {}
dict_test_b = {}
print(type(dict_test_a)) # <class 'dict'>
print(type(dict_test_b)) # <class 'dict'>

# 비어있는 dictionary 없이 바로 틀만 지키면 할당 가능하다.
dict_test_a = {'a':'apple', 'b':'banana', 'c':'cake'}
print(dict_test_a) # {'a': 'apple', 'b': 'banana', 'c': 'cake'}
dict_test_b = {'d':'dollar', 'e':'egg', 'dict_in_list':[2024, 1, 2]}
print(dict_test_b) # {'d': 'dollar', 'e': 'egg', 'dict_in_list': [2024, 1, 2]}

# dict()를 통한 생성. 위의 형태랑 다르기 때문에 잘 구분해줘야 한다.
dict_test_c = dict(f = 'free', g = 'garden', h = 'high')
print(type(dict_test_c)) # <class 'dict'>
print(dict_test_c) # {'f': 'free', 'g': 'garden', 'h': 'high'}

# key를 통해 value 값을 가져오는 딕셔너리의 사용
my_dict = {'생일':'6월 24일','현재 년도':1996 , '지역':['서울', '구미', 291]}
print(my_dict) #{'생일':'6월 24일','현재 년도':1996 , '지역':['서울', '구미', 291]}
print(my_dict['생일']) # 6월 24일
print(my_dict['현재 년도']) # 1996
print(my_dict['지역']) # ['서울', '구미', 291]
# 또한 value 값을 변경할 수 있다. dict[key] = value
my_dict['현재 년도'] = 2024
print(my_dict) # {'생일': '6월 24일', '현재 년도': 2024, '지역': ['서울', '구미', 291]}
# key 안의 value의 list에 접근하기
print(my_dict['지역'][1]) # 구미
# key 안의 value의 list의 값을 변경할 수 있다.
my_dict['지역'][1] = '대구'
print(my_dict) # {'생일': '6월 24일', '현재 년도': 2024, '지역': ['서울', '대구', 291]}

# dictionary에 key 중복이 들어간다면?
my_dict = {'a':'a', 'b':'b', 'a':'내가 진짜', 'c':'b'}
print(my_dict) # {'a': '내가 진짜', 'b': 'b', 'c': 'b'} value는 중복이어도 상관없다.
# 그럼 key 중복중 random으로 value가 튀어나올까?
my_dict = {'a':'a', 'b':'b', 'a':'내가 진짜', 'c':'b', 'a':'아니야 내가 진짜야'}
print(my_dict) # {'a': '아니야 내가 진짜야', 'b': 'b', 'c': 'b'} 마지막 요소 기준으로 출력된다.
 