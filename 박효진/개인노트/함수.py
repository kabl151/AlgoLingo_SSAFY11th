#위치인자 예시
def attendance(name, class_num):
    result = print(f'안녕하세요 {class_num}반 {name}님.')
    return result

attendance('CodingLarva', 3) # 안녕하세요 3반 CodingLarva님.
attendance('CodingLarva') # missing 1 required positional argument
attendance('CodingLarva', 3, '밥') # takes 2 positional arguments but 3 were given
attendance(3, 'CodingLarva') # 안녕하세요 CodingLarva반 3님.


#기본 인자 값 예시
# name, age=28, class_num로 넣게 된다면 non-default argument follows default argument 에러
def attendance(name, class_num, age=28):
    result = print(f'안녕하세요 {class_num}반 {age}살 {name}님.')
    return result

attendance('banana', 2, 25) # 안녕하세요 2반 25살 banana님.
attendance('CodingLarva', 3) # 안녕하세요 3반 28살 CodingLarva님.


# 키워드 인자 예시
def attendance(name, class_num, age):
    result = print(f'안녕하세요 {class_num}반 {age}살 {name}님.')
    return result

attendance(class_num = 2, age = 25, name = 'banana') # 안녕하세요 2반 25살 banana님.
attendance('CodingLarva',class_num = 3, 28) # positional argument follows keyword argument
attendance('cabin', 1, age = 29) # 안녕하세요 1반 29살 cabin님.


# 임의의 인자 목록 예시
def factor_sum(age, *args):
    print(type(args)) # <class 'tuple'> 타입을 확인해보니 튜플임을 알 수 있다.
    result = sum(args) # sum 내장함수를 사용하여 args의 요소를 합한 값을 result에 할당한다
    return print(f'{age}살 {result}개') # 28살 15개 출력 값을 볼 수 있다.

factor_sum(28, 3, 5, 7) # 위치인자와 임의의 인자를 섞어서 쓸 수 있다.

# 임의의 키워드 인자 목록
def print_info(age, **kwargs):
    print(type(kwargs)) # <class 'dict'> 타입을 확인해보니 dictionary 임을 알 수 있다.
    return print(age, kwargs) # 28 {'name': 'codingLarva', 'class_num': 3} 

print_info(name = 'codingLarva', age = 28, class_num = 3) # 키워드 인자와 임의의 키워드 인자


