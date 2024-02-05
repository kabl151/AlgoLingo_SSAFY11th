# # 형변환

# [1, 2, 3, 4, 5]
# [123456789]
# 1395324
# ['1', '3', '10']

# # lambda 함수


# try:
#     num = input('숫자입력 :')
#     print(int(num))

# except BaseException:
#     print('숫자가 입력되지 않았습니다.')





# # 1차원 배열의 선언
# arr_1 = list()
# arr_2 = []
# arr_3 = [2024, 1, 31]
# arr_4 = [0]* 10

# print(arr_1) # []
# print(arr_2) # []
# print(arr_3) # [2024, 1, 31]
# print(arr_4) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


#문자 -> 숫자
def atoi(s):
    i = 0
    for x in s:
        i = i * 10 + ord(x) - ord('0')
    return i

s = '123'
print(atoi(s))
print(type(atoi(s)))    #<class 'int'>

#숫자 -> 문자
def itoa(a):
    s = ''
    while a > 0:
        s = chr(a % 10 + ord('0')) + s
        a //= 10
    return s

a = 123
print(itoa(a))
print(type(itoa(a)))    #<class 'str'>