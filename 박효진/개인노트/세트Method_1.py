# set에 항목 x를 추가한다. set()를 통해 생성하거나 중괄호를 사용한다.
# s.add(x)
set_test = {1, 'a', 3, 'b', 5}
set_test.add(6) # 한번에 여러개의 요소를 넣을 수는 없다.
print(set_test) # {1, 3, 'b', 5, 6, 'a'} set는 출력때마다 순서가 달라짐
print(set_test) # {'a', 1, 3, 5, 6, 'b'} 하지만 정수데이터의 순서는 같다? To be continue..


# set의 모든 데이터를 제거
# s.clear()
set_test.clear()
print(set_test) # set() 빈 세트를 나타내는것은 set()이며 {}로 나타내지 않는다.(dict와 구분)


# set의 특정 데이터 제거
# s.remove(x)
set_test = {3, 1, 'z', 't', 10, 'code'}
set_test.remove('code')
print(set_test) # {'z', 1, 3, 10, 't'}
# set_test.remove('Larva') # KeyError: 'Larva' 없는 단어를 제거한다면 쿨하고도 짧은 오류를 리턴해준다


# set의 특정데이터 제거 (중복아님)
# s.discard(x)
set_test_1 = {5, 'k', 12, 'hungry', '11'}
set_test_1.discard('11')
print(set_test_1) # {5, 'hungry', 12, 'k'} 11이 제거됨을 알 수 있다.
set_test_1.discard('Larva')
print(set_test_1) # {5, 'hungry', 12, 'k'} 없는 단어를 제거하려 시도해도 오류가 생기지 않는다.


# set의 임의의 요소 반환 및 제거, list에서는 가장 오른쪽 요소 제거, 직접 지정도 가능
# s.pop()
set_test_2 = {1, 'a', 3, 'b', 5}
word_1 = set_test_2.pop()
print(word_1) # 1 // b
print(set_test_2) # {3, 5, 'b', 'a'} // {1, 3, 5, 'a'}
word_2 = set_test_2.pop()
print(word_2) # 3 // 1
print(set_test_2) # {5, 'b', 'a'} // {3, 5, 'a'}
word_3 = set_test_2.pop()
print(word_3) # 5 // 3
print(set_test_2) # {'b', 'a'} // {5, 'a'} 실행시마다 임의의 요소 반환을 확인할 수 있다.


# set 안에 다른 iterable한 데이터를 추가, 중복되는 데이터는 자동으로 추가되지않는다.
# s.update(iterable)
set_test_3 = {'a', 'b', 'c', 6, 7, 10}
set_test_3.update((6, 8))
print(set_test_3) # {'a', 'b', 6, 7, 8, 10, 'c'} 튜플로 넣어도, 리스트로 넣어도 들어간다.
set_test_3.update(['bc', 'abc', (100, 20)])
print(set_test_3) # {'b', 6, 7, 8, 10, 'abc', 'c', (100, 20), 'a', 'bc'}
