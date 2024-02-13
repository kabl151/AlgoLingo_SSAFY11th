T = int(input())
for tc in range(1, T+1):
    word = list(map(str, input().strip()))
    re_word = word[::-1]
    cnt = 0
    for i in range(len(word)):
        if word[i] == re_word[i]:
            cnt += 1
    if cnt == len(word):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


#----------------------------------------------------회문

def is_palindrome(word):
    if word == word[::-1]:
        return 1
    else:
        return 0

word = input()
result = is_palindrome(word)
print(result)