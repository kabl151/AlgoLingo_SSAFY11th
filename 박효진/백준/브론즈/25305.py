# 변수 응시자 수, 상받는 사람 수 = N, k를 array로 선언
arr = input().split()
N = int(arr[0])
k = int(arr[1])
# 학생들 점수들 x의 score_list 선언
score_list = list(map(int, input().split()))

# score_list를 성적순으로 정렬
score_list.sort()
# 성적순으로 나열한 score_list를 역순으로 변경
score_list.reverse()

# 내림차순으로 정렬한 score_list를 상받는 커트라인 프린트
print(score_list[k-1])