# 오늘의 테스트 워드
word = 'codiNg larVa'
other_word = 'PA RK'

# 문자열 a의 첫번째 위치를 찾아서 반환한다
# s.find()
spell_find = word.find('a')

print(word)			 # codiNg larvA 원본 변화 x
print(spell_find)		 # index 값인 8을 반환
spell_find = word.find('b')	 # 원본에 없는 문자열 'b'
print(spell_find)		 # 원본에 없으므로 -1 반환


# 문자열 g의 첫번째 위치를 찾아서 반환한다
# s.index()
spell_index = word.index('g')

print(word)			 # codiNg larvA 원본 변화 x
print(spell_index)		 # index 값인 5를 반환
# spell_index = word.index('z')	 # 원본에 없는 문자열 'z'
print(spell_index)		 # ValueError: substring not found


# 문자열이 알파벳으로만 이루어져 있는가
# s.isalpha()
result_1 = word.isalpha()

print(word)			 # codiNg larvA 원본 변화 x
print(result_1)			 # False word[6]에 공백 존재. 공백을 지운다면 True 반환


# 문자열이 알파벳 문자의 대문자만 있는지
# s.isupper()
result_2 = other_word.isupper()

print(other_word)		 # PA RK 원본 변화 x
print(result_2)			 # True 대문자만 있음, 공백은 제외한다


# 문자열이 알파벳 문자의 소문자만 있는지
# s.islower()
result_3 = other_word.islower()

print(other_word)		 # PA RK 원본 변화 x
print(result_3)			 # False 대문자만 있음, 공백은 제외한다