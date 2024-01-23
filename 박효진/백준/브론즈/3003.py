# split()으로 리스트 선언
piece = input().split()
# 각 피스에 해당하는 종류와 갯수 분류
my_king = int(piece[0])
my_queen = int(piece[1])
my_look = int(piece[2])
my_bishop = int(piece[3])
my_knight = int(piece[4])
my_pone = int(piece[5])

original_king = 1
original_queen = 1
original_look = 2
original_bishop =2
original_knight = 2
original_pone = 8

print(original_king - my_king, end = " ")
print(original_queen - my_queen, end = " ")
print(original_look - my_look, end = " ")
print(original_bishop - my_bishop, end = " ")
print(original_knight - my_knight, end = " ")
print(original_pone - my_pone, end = " ")