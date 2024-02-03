# 비교 연산자를 통한 결과는 True / False를 리턴한다
print(3 > 6) # False 3은 6보다 작기 때문에 False

print(10 <= 10) # True 10은 10보다 작거나 같기 때문에 True

print(1 == '1') # False 숫자데이터 1과 문자데이터 1은 같지 않다 False

print(11.0 == 11) # True float의 11.0과 integer의 11은 같기 때문에 Ture

print(12.0 != 12) # False 12와 12는 같기때문에 False

print(11.0 is 11) # False 위에선 같다면서요! 라고해도 float와 integer까지 비교하여 Flase

print(int(True)) # 1
print(int(True) == 1) # True
print(int(False)) # 0
print(int(False) == 1) # False

# 논리 연산자 (and)
print(True and True)#True
print(True and False)#False
print(False and True)#False
print(False and False)#False

# 논리 연산자 (or)
print(True or True)#True
print(True or False)#True
print(False or True)#True
print(False or False)#False

# 논리 연산자 사용 예시
# 키가 170 미만이고 몸무게가 '과체중'일 경우 비만일까?
height = 168
weight = '과체중'
print(height <= 170 and weight == '과체중') # True

# 키가 170이 미만이지만 몸무게가 '정상'일 경우 비만일까?
print(height < 170 and weight == '정상') # False

# 키가 170 이상이지만 몸무게가 '초 과체중'이라면 비만일까?
height = 180
weight = '초 과체중'
print(height <= 170 or weight == '초 과체중') # True
print(height <= 170 or weight == '정상') # False

# Falsy 조건을 이용한 논리 연산자
print(not False) # True
print(not 3) # False
print(not 'Helo') # False
print(((not True) and False) or (not False)) # True

# 단축평가
print(1 and 2) # 2
print(1 and 0) # 0
print(0 and 1) # 0
print(0 and 0) # 0

print(1 or 2) # 1
print(2 or 0) # 2
print(0 or 3) # 3
print(0 or 0) # 0

# None 너는 뭐하는 놈이냐.
alpha_list = ['c', 'b', 'f', 'a']
result = alpha_list.sort() # sort()는 주어진 list를 정렬하는 함수이다
print(result) # None
print(alpha_list) # ['a', 'b', 'c', 'f']

print(type(result))