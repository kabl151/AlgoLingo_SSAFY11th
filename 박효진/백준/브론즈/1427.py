# input N 선언
N = input()
# list로 변경
num_list = list(N)
# 문자열 오름차순 정렬
num_list.sort()
# 문자열 내림차순 정렬
num_list.reverse()
# join 함수를 통해 문자열 공백 없이 출력
result = ''.join(num_list)

print(result)