import sys
input = sys.stdin.readline

king, stone, N = map(str, input().split())
king_x, king_y = king[0], king[1]
stone_x, stone_y = stone[0], stone[1]

en_str = '0ABCDEFGH'

king_x = int(en_str.index(king_x))
king_y = int(king_y)
stone_x = int(en_str.index(stone_x))
stone_y = int(stone_y)

for i in range(int(N)):
    info = str(input().rstrip())
    if info == 'R' and king_x < 8:              # 오른쪽
        king_x += 1
    elif info == 'L' and king_x > 1:            # 왼쪽
        king_x -= 1
    elif info == 'B' and king_y > 1:            # 아래
        king_y -= 1
    elif info == 'T' and king_y < 8:            # 위
        king_y += 1
    elif info == 'RT' and king_x < 8 and king_y < 8:
        king_x += 1
        king_y += 1
    elif info == 'LT' and king_x > 1 and king_y < 8:
        king_x -= 1
        king_y += 1
    elif info == 'RB' and king_x < 8 and king_y > 1:
        king_x += 1
        king_y -= 1
    elif info == 'LB' and king_x > 1 and king_y > 1:
        king_x -= 1
        king_y -= 1
    if king_x == stone_x and king_y == stone_y:
        if info == 'R':  # 오른쪽
            stone_x += 1
        elif info == 'L':  # 왼쪽
            stone_x -= 1
        elif info == 'B':  # 아래
            stone_y -= 1
        elif info == 'T':  # 위
            stone_y += 1
        elif info == 'RT':
            stone_x += 1
            stone_y += 1
        elif info == 'LT':
            stone_x -= 1
            stone_y += 1
        elif info == 'RB':
            stone_x += 1
            stone_y -= 1
        elif info == 'LB':
            stone_x -= 1
            stone_y -= 1
    if stone_x == 0 or stone_x == 9 or stone_y == 0 or stone_y == 9:
        if info == 'R':  # 오른쪽
            king_x -= 1
        elif info == 'L':  # 왼쪽
            king_x += 1
        elif info == 'B':  # 아래
            king_y += 1
        elif info == 'T':  # 위
            king_y -= 1
        elif info == 'RT':
            king_x -= 1
            king_y -= 1
        elif info == 'LT':
            king_x += 1
            king_y -= 1
        elif info == 'RB':
            king_x -= 1
            king_y += 1
        elif info == 'LB':
            king_x += 1
            king_y += 1
        if info == 'R':  # 오른쪽
            stone_x -= 1
        elif info == 'L':  # 왼쪽
            stone_x += 1
        elif info == 'B':  # 아래
            stone_y += 1
        elif info == 'T':  # 위
            stone_y -= 1
        elif info == 'RT':
            stone_x -= 1
            stone_y -= 1
        elif info == 'LT':
            stone_x += 1
            stone_y -= 1
        elif info == 'RB':
            stone_x -= 1
            stone_y += 1
        elif info == 'LB':
            stone_x += 1
            stone_y += 1
print(en_str[king_x],king_y, sep = '')
print(en_str[stone_x],stone_y, sep = '')