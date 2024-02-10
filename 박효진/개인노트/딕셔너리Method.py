# 딕셔너리의 데이터를 모두 제거한다
# D.clear()
info = {'name':'hyo', 'age':29, 'home':'seoul'}
result = info.clear()
print(info)     # {} 내부 데이터가 모두 사라진 것을 볼 수 있다
print(result)   # None 반환값은 없다

# 키와 연결된 값을 반환하고, 만약 키가 없다면 None을 반환한다
# D.get(key)
info = {'name':'hyo', '나이':29, 29 :'늙음'}
print(info.get('name'))     # hyo   key에 해당하는 value 출력
print(info.get('나이'))     # 29    한글 key 도 가능
print(info.get(29))         # 늙음  정수 key 도 가능
print(info.get('몸무게'))   # None  키가 없으면 None 출력

# 리턴값을 None이 아닌 다른 출력으로 컨트롤 하고싶다면?
# D.get(key,value)
info = {'name':'hyo', '나이':29, 29 :'늙음'}
print(info.get('몸무게', '없음'))    # 없음 '몸무게' 라는 key 가 딕셔너리에 없기 때문에 
print(info)     # {'name': 'hyo', '나이': 29, 29: '늙음'} 원본 데이터에는 변함 없다

# 딕셔너리의 키 데이터를 모두 반환
# D.keys()
info = {'name':'hyo', '나이':29, 29 :'늙음'}
print(info.keys())      # dict_keys(['name', '나이', 29])
for i in info.keys():   # 반복문을 통해 출력 가능
    print(i)
'''출력
name
나이
29
'''

# 딕셔너리의 값 데이터를 모두 반환
# D.values()
info = {'name':'hyo', '나이':29, 29 :'늙음'}
print(info.values())    # dict_values(['hyo', 29, '늙음'])
for i in info.values(): # 반복문을 통해 출력 가능
    print(i)
'''출력
hyo
29
늙음
'''

# 딕셔너리의 키와 값 데이터를 모두 반환
# D.items()
info = {'name':'hyo', '나이':29, 29 :'늙음'}
print(info.items())     # dict_items([('name', 'hyo'), ('나이', 29), (29, '늙음')])
for i in info.items():  # 특이한 점은 items 메서드는 리스트로 크게 묶고 한번 더 튜플로 묶었다
    print(i)            
    print(type(i))      # 데이터 타입 확인
'''
('name', 'hyo')
<class 'tuple'>
('나이', 29)
<class 'tuple'>
(29, '늙음')
<class 'tuple'>
'''
for x, y in info.items():   # 해당 방식으로 2차원 배열처럼 출력할 수 있다.
    print(x, y)
'''
나이 29
29 늙음
'''

# 키 데이터를 제거하고 연결되어있던 값을 반환한다. 만약 없다면 Error
# D.pop(key[,default])
info = {'name':'hyo', '나이':29, 29 :'늙음'}
print(info.pop(29))             # 늙음 리스트에서 쓰는 pop과 동일하다
print(info)                     # {'name': 'hyo', '나이': 29} 29 : '늙음' 데이터가 pop됨
print(info.pop('country', 'No')) # No 없는 키 데이터를 pop할 시 default 값 No를 반환한 것
# print(info.pop('country'))       # KeyError: 'country' default를 설정하지 않는다면 Error

# 키와 연결된 값을 반환. 키가 없다면 key-default 데이터를 딕셔너리에 추가하고 default 반환
# D.setdefault(key[,default])
info = {'name':'hyo', '나이':29, 29 :'늙음'}
print(info.setdefault('country', 'Korea'))  # Korea  ':' 또는 '='가 아닌 ','가 들어가니 조심
print(info) # {'name': 'hyo', '나이': 29, 29: '늙음', 'country': 'Korea'} 데이터가 추가됨

# other에서 제공하는 키-값 데이터를 기존 딕셔너리에 갱신한다. 기존의 키가 있다면 덮어쓴다
# D.update([other])
info = {}
my_info = {'name':'Jin', 'age':28, 'class_num':'1반'}
info.update(my_info)
print(info)     # {'name': 'Jin', 'age': 28, 'class_num': '1반'}
info.update(age = 29,class_num = '3반') # 추가할 때 형식을 잘 기억해야한다.
print(info)     # {'name': 'Jin', 'age': 29, 'class_num': '3반'} age와 class_num의 값 업데이트
info.update(gender = 'male')            # 없는 데이터는 그대로 추가된다.
print(info)     # {'name': 'Jin', 'age': 29, 'class_num': '3반', 'gender': 'male'}