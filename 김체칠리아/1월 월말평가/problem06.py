matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
# 아래애 코드를 작성하시오.
#1
matrix_len = 0
for i in matrix:
    matrix_len += 1
print(matrix_len)    

# 2
for i in matrix:
    temporary_len =0
    for number in i:
        temporary_len += 1
    print(f'{i} 리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.')    

#3
for i in range(len(matrix)):
    
    for j in range(len(matrix[i])):
        print(f'matrix의 {i}, {j} 번째 요소의 값은 {matrix[i][j]}입니다.')

















# #2
# for j in matrix:
#     matrix_len_ += 1
# print(matrix_len)