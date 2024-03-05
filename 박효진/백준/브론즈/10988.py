word = list(map(str, input()))
re_word = word[::-1]
if word == re_word:
    result = True
else:
    result = False
print(int(result))