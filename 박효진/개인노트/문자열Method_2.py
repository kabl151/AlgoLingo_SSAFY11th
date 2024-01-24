# 바꿀 대상 글자(old)를 새로운 글자(new)로 대체후 반환
# s.replace(old, new[, count])
word = 'Coding neVer eNding stOry'
new_word_1 = word.replace('e', 'a') # e를 a로 대체 반환
new_word_2 = word.replace('ing', 'er') # ing를 er로 대체 반환
new_word_3 = word.replace('e', 'a', 1) # e를 a로 대체 반환, count 1회
print(word) # Coding neVer eNding stOry 반환값이 있기때문에 원본 변환 x
print(new_word_1) # Coding naVar aNding stOry -> e 모두 a로 바꾸고 반환
print(new_word_2) # Coder neVer eNder stOry -> ing 모두 er로 바꾸고 반환
print(new_word_3) # Coding naVer eNding stOry -> count값 횟수만큼 왼쪽에서 바꾸고 반환


# 문자열 시작과 끝 양쪽의 공백이나 특정 문자 제거
# s.strip([chars])
other_word = '   Method is Too HARD   '
new_word_4 = other_word.strip(' DRM') # 반드시 양쪽 끝의 요소들이 들어가야함 오른쪽 공백,D,R / 왼쪽 M 제거
print(other_word) #    Method is Too HARD -> 반환값이 있기 때문에 원본 변환x
print(new_word_4) # ethod is Too HA -> 공백, M, R, D 삭제 후 반환


# 문자열 사이 공백이나 특정 문자를 기준으로 분리
# s.split(sep = None, maxsplit = -1)
other_word_2 = '2024.01.22-월요일 저녁 9시 30분'
new_word_5 = other_word_2.split()
print(other_word_2) # 2024.01.22-월요일 저녁 9시 30분 반환값이 있기 때문에 원본 변환x
print(new_word_5) # ['2024.01.22-월요일', '저녁', '9시', '30분'] -> 공백을 기준으로 나누어 반환

new_word_6 = other_word_2.split(sep=".", maxsplit = 1) # .을 기준으로 자르며, 1회만 자른다
print(other_word_2) # 2024.01.22-월요일 저녁 9시 30분 반환값이 있기 때문에 원본 변환x
print(new_word_6) # ['2024', '01.22-월요일 저녁 9시 30분'] -> 문자열.으로 나누는데, maxsplit이 1이기 때문에 한번만 나눔


# iterable한 데이터에 separator 요소를 첨가
# 'separator'.join( [ iterable ] )
other_word_3 = ['2024', '01', '22', '월요일']
new_word_7 = ' '.join(other_word_3) # 요소 사이에 공백을 추가하여 반환한다
print(other_word_3) # ['2024', '01', '22', '월요일'] -> 반환값이 있기 때문에 원본 변환x
print(new_word_7) # 2024 01 22 월요일 -> 요소 사이에 공백을 추가하여 반환


# 문자열 가장 첫번째 글자를 대문자로 변환
# s.capitalize()
other_word_4 = 'codiNg lArVa'
new_word_8 = other_word_4.capitalize()
print(other_word_4) # codiNg lArVa -> 반환값이 있기 때문에 원본 변환x
print(new_word_8) # Coding larva -> 첫글자를 대문자로 만들고 나머지 글자는 소문자로 반환

# 문자열 내 띄어쓰기 기준으로 단어의 첫 글자는 모두 대문자로, 나머지는 소문자로 변환
# s.title()
new_word_9 = other_word_4.title()
print(other_word_4) # codiNg lArVa -> 반환값이 있기 때문에 원본 변환x
print(new_word_9) # Coding Larva -> 공백을 기준으로 글자를 나누고 해당 글자들의 첫 글자를 대문자, 나머지 글자는 소문자로 반환

# 문자열의 모든 알파벳을 대문자로 변경
# s.upper()
other_word_5 = 'cOdInG WorlD1996'
new_word_10 = other_word_5.upper()
print(other_word_5) # cOdInG WorlD1996 -> 반환값이 있기 때문에 원본 변환x
print(new_word_10) # CODING WORLD1996 -> 모든 알파벳을 대문자로 반환

# 문자열의 모든 알파벳을 소문자로 변경
# s.lower()
new_word_11 = other_word_5.lower()
print(other_word_5) # cOdInG WorlD1996 -> 반환값이 있기 때문에 원본 변환x
print(new_word_11) # coding world1996 -> 모든 알파벳을 소문자로 반환

# 문자열안의 모든 알파벳 대문자/소문자를 서로 변경
# s.swapcase()
new_word_12 =  other_word_5.swapcase()
print(other_word_5) # cOdInG WorlD1996 -> 반환값이 있기 때문에 원본 변환x
print(new_word_12) # CoDiNg wORLd1996 -> 알파벳의 대/소문자가 스왑하여 반환