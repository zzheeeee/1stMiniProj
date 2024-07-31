## 테스트를 위한 초기 변수 설정 (합칠 때 지우기)
import random

choice = [80, 20]
Loc = ['교무실', '양호실', '음악실', '매점', '도서실', '나무', '운동장']
pLoc = 1

hee = {'name':'쩡','level':4, 'kind':80, 'weight':0, 'skill':[1,2,5]}
cha = {'name':'수빈','level':4, 'kind':100, 'weight':0, 'skill':[3,4,6]}
playerList = [hee, cha]
pIdx = 0 #random.randint(0,1)
pName = playerList[pIdx]['name']
pLevel = playerList[pIdx]['level']
pKind = playerList[pIdx]['kind']
pWeight = playerList[pIdx]['weight']

# System : 쩡 스킬이 발동 성공하여 힌트를 얻습니다.	스킬	{쩡}, {수빈}
# System : 쩡 스킬이 발동 성공하여 스텝 카운트가 줄어듭니다.	스킬	{성공}, {실패}
# System : {장소} 입니다.	장소	{장소}
# System : 인성이 -10 되었습니다.	인성	-10
# System : 인성이 -10 되었습니다. (출력)	인성	-30
# System : key	계속-space bar	예-y	아니오-n
# System : 계속 하려면 space bar를 입력하세요.	레벨	{레벨}

#print(f"Player : {playerList[pIdx]}")
# conv : 대화 출력 / situ : 상황 출력 / sys : 시스템 출력
def skill_succ():
    pSkillTrue = random.randint(1, 100)
    if pSkillTrue >= 15:
        print("System : 쩡 스킬이 발동 성공하여 힌트를 얻습니다.") ##상황별 수정 필요!
        return True
    else:
        print("System : 20% 확률로 스킬 발동 실패했습니다.")
        return False
def conv(speaker, ment):
    print(f"{speaker}: {ment}")
def situ(ment):
    print('\n')
    print(ment)
def sys(ment):
    print('\n',ment)
def yesorno():
    while True:
        reply = input(f'\n>> 수락하려면 y를, 거절하려면 n을 입력하세요.\n입력 :')
        #print(reply, reply == 'y' , reply=='Y')
        if str(reply) == 'y' or str(reply) == 'Y':
            break
        elif str(reply) == 'n' or str(reply) == 'N':
            sys('인성이 -10 되었습니다.')
            continue
        else:
            continue

def phasing(num):
    while True:
        progress = input('>> 계속하시려면 "f"를 입력하세요.')
        if progress == 'f' or 'F':
            break
        else:
            continue
    print()
    return num

#############################################################################
####################################미션01###################################

while pLoc==1:
########미션01 시작 초기 변수 설정 ########
    print(f"System : {Loc[pLoc]} 입니다.")
    npc = "친구"
    ## 스킬 발현 ##
    if pLoc in playerList[pIdx]['skill']:
        pSkill = skill_succ  # True if (random.choices((0, 1), choice)) else False
    else:
        pSkill = False
    ## 증상 리스트, 처방 리스트, 랜덤 인덱스 ##
    sickList = ['두통', '속쓰림', '감기기운', '소화불량', '근육통']
    mediList = ['진통제', '위장약', '감기약', '소화제', '파스']
    sickIdx = random.randint(0, len(sickList) - 1)

########미션01-1 상황설명 ########
    conv(pName, "양호선생님이 부재중이시다.")
    input('>> 계속하려면 아무 키나 입력하세요.\n')
    situ(f"{npc}가 양호실에 들어왔다.")
    conv(npc,f"{pName}! 여기서 뭐하고 있어?")
    conv(pName, "약 받으러 왔는데 양호선생님이 안계셔서 그냥 가려고.")
    conv(npc, f"뭐? 난 지금 약이 꼭 필요한데.. {pName}아 너가 약 좀 찾아줄래?")
    yesorno()

########미션01-2 미션 수행 ########
    while True:
        print('='*50)
        conv(npc, f"나의 증상은 {sickList[sickIdx]}이야.")
        print(f'약품 리스트의 값은 다음과 같습니다. {mediList}')
        ms01 = input('증상에 맞는 약의 값을 구할 수 있도록 다음의 코드를 완성하세요.\ncode : mediList[?] : ')
        if sickIdx == int(ms01):
            print('='*50)
            conv(npc, f"나한테 딱 맞는 약이야. {pName}아, 정말 고마워!")
            print("System : 레벨이 1 올랐습니다.")
            pLevel += 1
            break
        elif sickIdx > int(ms01) or sickIdx < int(ms01):
            conv(npc, f"음... 이건 나의 증상에 맞지 않은 약인 것 같은데?")
            continue
########미션01 이동 전 독백 ########
    print()
    print()
    conv(pName, "이제 다른 곳으로 이동 하자.")
    input('>> 계속하려면 아무 키나 입력하세요.\n')
    sys("양호실에서 나왔습니다.")
    print()
    situ("♪~~♩~♬")
    conv(pName, "이건 어디서 들리는 음악소리지? 음악실인것 같은데 가볼까?")
    input('>> 계속하려면 아무 키나 입력하세요.\n')
########미션01 종료 ########
    pLoc = 2

#############################################################################
#############################################################################

