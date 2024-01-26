# test case N개 선언
N = int(input())
word_list = []
# 반복문을 통해 N개의 단어받아서 list 나열
for i in range(N):
    word = input()
    word_list += [word]
# 만들어진 리스트 정렬 후 출력
word_set = set(word_list)
new_word_list = list(word_set)

new_word_list.sort(key=lambda x: (len(x), x), reverse=False)
for j in new_word_list:
    print(j)