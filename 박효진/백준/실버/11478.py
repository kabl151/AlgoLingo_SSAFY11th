import sys
input = sys.stdin.readline

word = input().rstrip()
word_lst = []
for i in range(len(word)):
    for j in range(len(word)-i):
        word_lst.append(word[i]+word[i+1:j+1+i])
print(len(set(word_lst)))