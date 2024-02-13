# import sys
# sys.stdin = open('test_input.txt', 'r')

for i in range(1, 11):
    num = int(input())
    word = str(input())
    sentence = str(input())
    new_sentence = sentence.replace(word, '')
    minus_word = len(sentence) - len(new_sentence)
    result = minus_word // len(word)
    print(f'#{num} {result}')