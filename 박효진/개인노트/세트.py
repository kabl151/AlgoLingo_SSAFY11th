# 잘못된 빈 set를 생성하는 법
set_test = {}
print(set_test) # {}
print(type(set_test)) # <class 'dict'> dict의 생성 방법과 같기 때문에 잘못된 생성 방법
# 제대로 된 빈 set를 생성하는 법
set_test = set() # 반드시 set()를 통해 비어있는 set 할당
print(set_test) # set()
print(type(set_test)) # <class 'set'> 제대로 된 set가 생성되었음을 알 수 있음

# {}을 통해 set를 생성하는 법
set_test = {1, 3, '나는 집합'}
print(set_test) # {1, 3, '나는 집합'}
print(type(set_test)) # <class 'set'>

# set을 통해 두 list의 중복된 요소를 제거하는 방법
list_a = [1, 2, 'a', 3, 2, 5, 4, 6]
list_b = [100, 5, 'a', 9, 10, 11, 3]
plus_list = list_a + list_b
new_set = set(plus_list)
new_list = list(new_set)
# 이때, a와 b리스트의 중복을 b에서 지우고, 숫자열이 먼저 이후 문자열이 나열되는 규칙은 있다.
print(new_list) # [1, 2, 3, 4, 5, 6, 100, 9, 10, 11, 'a']