# 아래 함수를 수정하시오.
def even_elements(in_list):
    for i in range(len(in_list) - 1, -1, -1):
        if my_list[i] % 2 == 1:
            in_list.pop(i)
    result = in_list
    return result


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
