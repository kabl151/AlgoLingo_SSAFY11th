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

N = 10              # 필요한 노드 수
h = [0]*(N+1)       # 최대 힙
last = 0  


while(last>0):
    print(deq())
