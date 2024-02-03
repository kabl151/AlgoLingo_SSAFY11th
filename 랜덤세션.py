#세션 랜덤으로 생성하는 코드
import random
import math
from datetime import datetime

nowTimeStamp = datetime.now()
memberList = []
newMemberList = []
n = 0
print("----------------------------------------------------------------------------")
print(" ")
memberNum = int(input("스터디 전체 멤버수를 입력하세요. ▶  "))
sessionNumber = int(input("나눌 세션의 수를 입력하세요. ▶  "))

print("----------------------------------------------------------------------------")
print(" ")
#멤버 이름 입력받고 리스트에 저장.
for t in range(memberNum):
    
    
    print(" ")
    a = str(input(f'{t+1} 번째 멤버 ▶ '))
    memberList.append(a)
    print(f'현재 입력된 멤버는 {memberList} 입니다.')
    
#멤버 랜덤 셔플
random.shuffle(memberList)

#새로운 세션 생성과정.
#n 값은 한 세션에 몇 명씩 배정하는지 결정하는 인자임. 
#n 값에 따라서 나누는 방식이 달라짐. 
n = int(math.ceil(memberNum/sessionNumber))# n값 초기 설정

for s in range(sessionNumber):
    n = int(math.ceil(memberNum/sessionNumber))
    newMemberList.append(memberList[:n])
    del memberList[:n]
    if n % 2 != 0: # 모든 세션이 동등한 인원수로 구성할 수 없을 때. 예를 들어, 3-3-2 명 같은 구성임.
        try:
            n = int(math.ceil((memberNum-n)/(sessionNumber-(s)))) # n값 갱신
            memberNum = memberNum - n #나머지 멤버수 갱신
        except:
            pass
    elif n % 2 == 0 or n % 3 == 0 :
        pass

#출력
print(" ")
print(f'----------------------결과 출력 일시 : {nowTimeStamp}-----------------------')
print(" ")
for s in range(sessionNumber):
    print(f'# {s+1} 세션의 멤버의 구성원은 {newMemberList[s]} 입니다.')
    leader = random.choice(newMemberList[s]) #리더 랜덤으로 선정
    leaderIndex = newMemberList[s].index(leader) #리더 인덱스 구하기.
    del newMemberList[s][leaderIndex] #리더와 발표자 겁치지 않도록 리더 제외.
    PR_member = random.choice(newMemberList[s]) #이렇게 하면 리더와 발표자가 겹치지 않는다.
    print(f' ■ 세션 리더는 "{leader}"님 이고, 메인 발표자는 "{PR_member}"님 입니다. ■')
    print(" ")
print('-----------------------프로그램 실행 완료------------------------------------------------')