# 리스트에 데이터 추가 (오른쪽부터) [반환값 X]
# L.append(x)
test_list = [1, 3, 2, 5, 7, 6]  # 정수로 이루어진 리스트 할당
test_list.append(100)   # 정수 100 데이터를 리스트에 추가
test_list.append(100, 10)   # TypeError: list.append() takes exactly one argument (2 given)
test_list.append("10")  # 문자열 10 데이터를 리스트에 추가
test_list.append([300, 400])    # 리스트 [300, 400] 데이터를 리스트에 추가
test_list.append((1, 2,))   # 튜플 (1, 2,) 데이터를 리스트에 추가
test_list.append({'a' : 'apple'})   # dict {'a' : 'apple'} 데이터를 리스트에 추가. 다만 key값만.
print(test_list)    # [1, 3, 2, 5, 7, 6, 100, '10', [300, 400], (1, 2), {'a': 'apple'}]


# 리스트에 한번에 많은 데이터 추가 (오른쪽부터)
# L.extend(iterable)
test_list_2 = [1, 'a']  # 정수와 문자열이 들어간 리스트 할당
test_list_2.extend([(100, 10), [1, 2]])   # 리스트 안에 튜플/리스트 추가
test_list_2.extend(('1', '2', 3,))  # 리스트 안에 튜플 추가
test_list_2.extend({'b' : 'banana'})    # 리스트 안에 dict 추가
print(test_list_2)  # [1, 'a', 100, 10, [1, 2], '1', '2', 3, 'b']


# 리스트의 인덱스[i]에 데이터 x를 삽입
# L.insert(i, x)
test_list_3 = [1, 3, 23, 'a', 'aab', 30]
return_value = test_list_3.insert(1, 100)   # 인덱스[1]에 100 삽입
print(return_value) # None insert메서드는 삽입되어 데이터가 바뀌지만 return값은 없다
test_list_3.insert(3, 'c')  # 인덱스[3]에 문자열 'c' 삽입
test_list_3.insert(2, [3, 4, 5])    # 인덱스[2]에 리스트 [3, 4, 5] 삽입
print(test_list_3)  #[1, 100, [3, 4, 5], 3, 'c', 23, 'a', 'aab', 30]


# 리스트의 가장 왼쪽에 있는 데이터 x를 제거, 데이터가 존재하지 않는다면 'ValueError'
# L.remove(x)
test_list_4 = ['aabc', 3, 10, 2, 3, 3, 'zvc']
test_list_4.remove('a') # ValueError: list.remove(x): x not in list
value_2 = test_list_4.remove('zvc')   # 가장 왼쪽부터 나열된 것 중 해당하는 문자열'zvc'을 삭제한다
print(value_2)  # None return 값은 없다
test_list_4.remove(3)   # 가장 왼쪽부터 나열된 것 중 해당하는 숫자 3을 삭제한다
print(test_list_4)  #['aabc', 10, 2, 3, 3]


# 리스트의 가장 오른쪽에 있는마지막 데이터를 반환 후 제거한다.
# L.pop()
test_list_5 = [3, 2, 'ab', 40, 2, 'gif']
value_3 = test_list_5.pop() # 반환이 있다면 할당될 것이다.
print(value_3)  # gif 반환하는 데이터 gif 가 할당 되어있다.
print(test_list_5)  # [3, 2, 'ab', 40, 2] gif가 사라진 리스트가 되어있다.
empty_list = [] #비어있는 리스트를 할당하여 테스트
# empty_list.pop()    # IndexError: pop from empty list


# 리스트의 인덱스[i]에 있는 데이터를 반환 후 제거한다.
# L.pop(i)
test_list_5 = [3, 2, 'ab', 40, 2, 'gif']
value_4 = test_list_5.pop(3)    # 인덱스[3]의 위치에 있는 데이터를 반환한다
print(value_4)  # 40
print(test_list_5) # [3, 2, 'ab', 2, 'gif']


# 리스트의 모든 데이터를 삭제 후 빈 리스트로 만든다.
# L.clear()
value_5 = test_list_5.clear()   # return 값이 있는지 확인
print(value_5)  # None return은 없다.
print(test_list_5) # [] 모든 데이터를 삭제하니 빈 리스트만 남았다.