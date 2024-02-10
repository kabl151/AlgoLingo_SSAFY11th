import sys
input = sys.stdin.readline

cursor_lft = list(input().strip())
cursor_rght = []
T = int(input())
for i in range(T):
    keyword = input().split()
    if keyword[0] == 'L' and cursor_lft:
        word = cursor_lft.pop()
        cursor_rght.insert(0,word)
    elif keyword[0] == 'D' and cursor_rght:
        word = cursor_rght.pop(0)
        cursor_lft.append(word)

    elif keyword[0] == 'B' and cursor_lft:
        cursor_lft.pop()

    elif keyword[0] == 'P':
        cursor_lft.append(keyword[1])

result = cursor_lft + cursor_rght
print(*result, sep='')