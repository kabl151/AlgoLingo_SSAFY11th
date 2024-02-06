T = int(input())                    #테스트 케이스
for tc in range(1, T+1):            
    str1 = input()                  # str1의 문자를 받아준다
    str2 = input()                  # str2의 문자를 받아준다
    lst_str1 = list(set(str1))      # set() 함수를 통해 중복을 거르고 list로 만든다
    cnt_lst = []                    # 카운트 받아줄 빈 리스트 생성
    for i in lst_str1:              # str1에 있는 문자를 반복문을 돌려 str2에 몇번 들어가 있는지 확인
        cnt = 0                     # cnt 초기화
        for j in range(len(str2)):  # 범위는 str2의 길이만큼 반복
            if i == str2[j]:        # lst_str1의 문자가 str2의 문자와 같다면
                cnt += 1            # 카운트 1 증가
        cnt_lst.append(cnt)         # str1의 문자 1개당 카운트 된 숫자를 cnt_lst에 추가    
    print(f'#{tc} {max(cnt_lst)}')  # cnt_lst에 추가된 cnt 횟수 중 최댓값 출력    

                                    # 예상되는 문제점, set 변환 이후 list하면 섞이지 않는가?
                                    # -> 카운트 정보만 가져오는 것이라서 크게 상관 없다.
                                    # 만약 어떠한 문자가 가장 많이 쓰였냐 라고하면 ???
                                    # -> max를 사용해 cnt_lst와 lst_str1의 인덱스를 맞추어 찾는다.

