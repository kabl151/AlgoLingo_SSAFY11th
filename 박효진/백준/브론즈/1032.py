N = int(input())
compare = input()
for i in range(N-1):
    word = input()
    for j in range(len(compare)):
        if compare[j] == word[j]:
            continue
        elif compare[j] != word[j]:
            word.replace(word[j],'?')
    compare = word
print(compare)