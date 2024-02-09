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


# num_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# lst = [5]
# for _ in range(5):
#     print(*num_lst)

# def MenOfPassion(A,n):
#     sum = 0
#     for i in range(1, n-1):
#         for j in range(i, n):
#             sum += A[i]*A[j]
#     return sum
# A = [[1,1],[1,1]]
# n = int(input())
# print(MenOfPassion(A,n))

# def MenOfPassion(A,n):
#     sum = 0
#     for i in range(1, n-2):
#         for j in range(i+1, n-1):
#             for k in range(j+1, n):
#                 sum += A[i]*A[j]*A[k]
#     return sum
# A = [[1,1],[1,1]]
n = int(input())
# print(MenOfPassion(A,n))
n = int(input())
print((n-2)*(n-1)*n // 2 // 3)
print(3)