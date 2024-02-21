'''
2 5 3 6 4
'''
# 이진트리의 왼쪽하단부터 채워나가는 것 그리고 while문을 통해 위치를 찾아가는것
# 최대 힙
def enq(n):
    global last
    last += 1       # 마지막 노드 추가(완전이진트리 유지)
    h[last] = n     # 마지막 노드에 데이터 삽입
    c = last        # 부모 > 자식 비교를 위해
    p = c // 2      # 부모노드번호 계산
    while p >= 1 and h[p] < h[c]: # 부모가 존재하고 부모보다 더 작으면 교환해서 올라가
        h[p], h[c] = h[c], h[p]   # 데이터 교환
        c = p
        p = c //2
N = 10              # 필요한 노드 수
h = [0]*(N+1)       # 최대 힙
last = 0            # 힙의 마지막 노드 번호


def deq():
    global last
    tmp = h[1]   # 루트의 키값 임시 보관
    h[1] = h[last]
    last -= 1
    p = 1           # 새로 옮긴 루트
    c = p*2         # 자식 노드 계산
    while c <= last: # 자식이 있으면의 의미
        if c + 1 <= last and h[c] < h[c+1]:   #오른쪽 자식도 있고, 오른쪽 자식이 더 크다면
            c += 1  # 오른쪽과 비교하기 위해 c에 +1 해준다
        if h[p] < h[c]:
            h[p], h[c] = h[c], h[p]
            p = c
            c = p*2
        else:
            break
    return tmp


enq(2)
enq(5)
enq(3)
enq(6)
enq(4)

while(last>0):
    print(deq())