# test case N개 선언
N = int(input())
word_list = []
# 반복문을 통해 N개의 단어받아서 list 나열
for i in range(N):
    word = input()
    word_list += [word]
# 만들어진 리스트 정렬 후 출력
word_list.sort()
# # 반복문과 pop을 이용한 좌측 항목 반환 후 제거
# for k in range(len(word_list)):
#     pop_word = word_list.pop(0)
#     print(pop_word)

for j in range(len(word_list)):
    if word_list[j]