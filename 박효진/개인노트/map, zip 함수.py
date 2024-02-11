
# map(function, iterable) = map(함수, 시퀸스)
# input data : 1 2 3 4 5 를 정수로 넣으려면
arr = input().split()
arr_1 = int(arr[0])
arr_2 = int(arr[1])
arr_3 = int(arr[2])
arr_4 = int(arr[3])
arr_5 = int(arr[4])
print(arr)          # ['1', '2', '3', '4', '5']
print(type(arr))    # <class 'list'>

arr = map(int, input().split())
print(type(arr))    # <class 'map'>
print(arr)          # <map object at 0x0000020D548D1FA0>

arr = list(arr)     # list로 변환
print(type(arr))    # <class 'list'>
print(arr)          # [1, 2, 3, 4, 5]
print(type(arr[0])) # <class 'int'>

# 주로 쓰는 input 형식
arr = list(map(int, input().split()))
# 공백으로 나누어진 데이터를 map 함수를 통해 int로 모두 형변환한 map 데이터를 list로 만든다.

# zip(*iterables) = zip(가변인자 시퀸스)
boys = ['hyeon', 'yeop']
girls = ['yeon', 'ria']
pair = zip(boys, girls)

print(pair)             # <zip object at 0x0000022E4A2C4680> 예상했겠지만 변환이 한번 더 필요하다
pair = list(pair)       # 리스트 형변환
print(pair)             # [('hyeon', 'yeon'), ('yeop', 'ria')] 
print(type(pair[0]))    # <class 'tuple'> 튜플로 묶여있는 모습
