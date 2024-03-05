# 5줄에 걸쳐 최대 15글자의 문자열을 받는 리스트를 리스트컨프리헨션을 통해 선언

arr = [list(input()) for _ in range(5)]
len_lst = []                    #가장 긴 문자열을 탐색하기 위해 빈 리스트 선언
for i in range(5):              # 5개의 행을 탐색
    len_lst.append(len(arr[i])) # 행의 길이를 빈 리스트에 넣어준뒤
max_len = max(len_lst)          # max함수를 통해 최대 길이를 확인

# 가장 길이가 긴 행에 모자라는 빈 데이터를 채워주기 위해 비어있는 공백 문자열을 삽입한다

for i in range(5):
    if len(arr[i]) < max_len:   # 행을 돌면서 가장 긴 문자열의 길이보다 짧다면 append로 추가
        for j in range(max_len-len(arr[i])):
            arr[i].append('')

# 전치를 진행해서 세로읽기를 진행한다
new_arr = list(map(list, zip(*arr)))

# 한줄에 이어서 출력할 것이기 때문에 *언패킹과 사이에 공백제거, 출력후 공백제거를 넣어준다
for i in range(max_len):
    print(*new_arr[i], sep='', end='')
