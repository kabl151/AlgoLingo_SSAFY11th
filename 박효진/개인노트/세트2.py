
set_A = {1, 3, 2, 4, 10}
set_B = {5, 6, 7, 1, 10}

# set_A - set_B : 차집합
result_1 = set_A.difference(set_B)
print(result_1) # {2, 3, 4}

# set_A & set_B : 교집합
result_2 = set_A.intersection(set_B)
print(result_2) # {1, 10}

# set_A | set_B : 합집합
result_3 = set_A.union(set_B)
print(result_3) # {1, 2, 3, 4, 5, 6, 7, 10}


set_C = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_D = {5, 6, 7, 1, 10}

# set_C <= set_D : 포함관계 boolean 값 반환
result_4 = set_C.issubset(set_D)
print(result_4) # False

# set_C >= set_D : 포함관계 boolean 값 반환
result_5 = set_C.issuperset(set_D)
print(result_5) # True


