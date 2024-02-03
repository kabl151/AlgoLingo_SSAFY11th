word = input()
word_list = list(word)
cnt_second = 0
ABC_list = ["A", "B", "C"]
DEF_list = ["D", "E", "F"]
GHI_list = ["G", "H", "I"]
JKL_list = ["J", "K", "L"]
MNO_list = ["M", "N", "O"]
PQRS_list = ["P", "Q", "R", "S"]
TUV_list = ["T", "U", "V"]
WXYZ_list = ["W", "X", "Y", "Z"]
for i in word_list:
  if i in ABC_list:
    cnt_second += 3
  if i in DEF_list:
    cnt_second += 4
  if i in GHI_list:
    cnt_second += 5
  if i in JKL_list:
    cnt_second += 6
  if i in MNO_list:
    cnt_second += 7
  if i in PQRS_list:
    cnt_second += 8
  if i in TUV_list:
    cnt_second += 9
  if i in WXYZ_list:
    cnt_second += 10

print(cnt_second)