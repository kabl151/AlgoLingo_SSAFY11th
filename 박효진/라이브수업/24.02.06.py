# Brute Force
def brute_force(p,t): #while문
    '''
    :retrun: 찾은 위치의 첫번째 인덱스를 반환
            없는경우에는 -1 반환
    
    '''
    i = 0 # 문자열의(t) 인덱스 i
    j = 0 # 패턴의(p) 인덱스 j
    while i < N and j < M:
        # 서로 같지 않을 때
        if t[i] != p[j]:
            i = i - j + 1 # 한칸 밀기
            j = 0       # 초기화
        # 서로 같은 값을 가졌을 때 (문자가 서로 일치할 때)
        # 각 인덱스를 += 1
        else: 
            i = i + 1
            j = j + 1
    # 검색에 성공했는지 경우..
    if j == M:
        return i - M    #패턴 탐색 성공한 인덱스 반환
    else:
        return -1       #실패 경우

def brute_force(p,t):   # 2중 for 문
    '''
    :retrun: 찾은 위치의 첫번째 인덱스를 반환
            없는경우에는 -1 반환
    
    '''
    for i in range(N - M + 1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
        else:
            return i    #검색 성공
    return -1   #검색 실패
    

t = 'this is a book~' # 텍스트
p = 'is'    #패턴
N = len(t)
M = len(p)
brute_force(p, t)

# KMP 알고리즘
def kmp(t, p):
    N = len(t)
    M = len(p)
    # 1. 전처리 과정
    lps = [0] * (M + 1) # next 배열 *M+1인 이유는 배열 탐색 1칸을 넘길 수 있어서
    lps[0] = -1 # ***첫 단어에 비교가 실패한 경우...
    # 일치한 개수를 카운트하는 인덱스 j가 필요
    j = 0 # 일치한 개수 == 비교할 패턴 위치 라면 카운트를 올릴예정(누적합 개념)
    # 반복문을 통해서 배열을 순회.
    # 접두사 == 접미사가 같은 곳에 대해서 카운트를 넣기.
    for i in range(1, M):
        lps[i] = j
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    # 2. 탐색 과정
    i = 0 # 문자열의(t) 인덱스 i
    j = 0 # 패턴의(p) 인덱스 j
    while i < N and j <= M:     # 등호를 넣는 이유는 패턴이 여러개인 경우. 빼도 무관?
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1    
    
    
    
    
    
t = 'zzzabcdabcdabcefabcd'
p = 'abcdabcef'
kmp(t, p)