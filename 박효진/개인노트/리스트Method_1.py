# 찾으려는 데이터의 인덱스 찾기
# L.index(데이터, start, end)
test_list = ['b', 3, 2, 4, 'a', 2, 5]
index_num_1 = test_list.index(2) # 데이터 2가 해당 리스트의 몇번 인덱스인지
index_num_2 = test_list.index(2,3,6) # 데이터 2가 해당 리스트 인덱스 3과 6사이중 몇번 인덱스인지

print(test_list)    # 원본은 놔두고 반환되기 때문에 변화 없음
print(index_num_1)   # 2 인덱스 [2]위치해 있는 것을 알 수 있다
print(index_num_2)   # 5 범위를 인덱스 [3]과 [6]사이로 제한했기 때문에 인덱스 [5] 에 있는 2의 위치 반환


# 문자열과 정수가 섞인 list를 뒤집기
# L.reverse()
new_list_2 = test_list.reverse()    #test_list의 순서를 뒤집기
print(new_list_2)   # None  *중요* reverse() 메서드는 반환값이 없다.
print(test_list)    # [5, 2, 'a', 4, 2, 3, 'b'] 문자열, 숫자 상관 없이 순서가 뒤집힌다.


# 정수가 섞여있는 list 정렬하기
# L.sort()
test_list_2 = [1, 3, 2, 4, 7, 2, 5] # 무작위로 되어있는 정수 리스트
new_list_3 = test_list_2.sort()
print(new_list_3)   # None  *중요* sort() 메서드는 반환값이 없다.
print(test_list_2)  # [1, 2, 2, 3, 4, 5, 7] 오름차순으로 정렬되었다.

# 문자열이 섞여있는 list 정렬하기
test_list_3 = ['d', 'e', 'p', 'l', 'i', 't']
test_list_3.sort()  # 문자열도 오름차순으로 정렬이 가능하다. (숫자 문자열)
print(test_list_3)  # ['d', 'e', 'i', 'l', 'p', 't']

# 문자열의 길이를 기준으로 정렬하기 : (key) 사용
test_list_4 = ["orange", "apple", "kiwi", "banana"]
test_list_4.sort(key = len) #key의 조건을 넣어 정렬할 수 있다.
print(test_list_4)  # ['kiwi', 'apple', 'banana', 'orange'] 글자 수가 적은 순서대로 나열 되었다.

# 혹시 문자열의 길이와 알파벳순을 한번에 해결할 순 없을까?
test_list_4.sort( reverse = False, key = len)
print(test_list_4)  # ['kiwi', 'apple', 'orange', 'banana'] 아쉽게도 정렬되지 않았다..

# 문자열과 정수가 섞여있다면? 
test_list = ['b', 3, 2, 4, 'a', 2, 5]
test_list.sort()   # 문자열과 정수 사이의 인스턴스엔 부등호를 지원하지 않는다.
print(test_list)    # TypeError: '<' not supported between instances of 'str' and 'int'


# 리스트에서 해당 데이터 x의 개수를 반환하기
# L.count(x)
test_list_5 = ['b', 2, 3, 'a', 6, 'a', 2, 5, 2]
return_value_1 = test_list_5.count('a') # 해당하는 문자열'a' 데이터 반환
print(return_value_1)   # 2 문자열 a가 들어간 것은 총 2개
return_value_2 = test_list_5.count(2)   # 해당하는 숫자 2 데이터 반환
print(return_value_2)   # 3 숫자 2이 들어간 것은 총 3개
print(test_list_5)  # ['b', 2, 3, 'a', 6, 'a', 2, 5, 2] 원본은 그대로

# 문자열이 반복된 경우에도 인식할까?
test_list_6 = ['abcabcabcbcabc']    # a 혹은 ab 혹은 abc가 반복되는 데이터
return_value_3 = test_list_6.count('abc')
print(return_value_3)   # 0 전체 문자열 한개로 인식한다.