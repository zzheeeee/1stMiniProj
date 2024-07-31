## 테스트를 위한 초기 변수 설정 (합칠 때 지우기)
import random
import os

Loc = ['교무실', '양호실', '음악실', '매점', '도서실', '나무', '운동장']
pLoc = -1

hee = {'name': '쩡', 'level': 4, 'kind': 75, 'weight': 0, 'skill': [1, 2, 5]}
cha = {'name': '수빈', 'level': 4, 'kind': 90, 'weight': 0, 'skill': [3, 4, 6]}
playerList = [hee, cha]
pIdx = 0  # random.randint(0,1)
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

# print(f"Player : {playerList[pIdx]}")
# conv : 대화 출력 / situ : 상황 출력 / sys : 시스템 출력

#######################################################################################################

def skill_succ():
    pSkillTrue = random.randint(1, 100)
    if pSkillTrue >= 15:
        if pName == '쩡':
            print("System : {} 스킬이 발동 성공하여 힌트를 얻습니다.")  ##상황별 수정 필요!
        else:
            print("System : {} 스킬이 발동 성공하여 힌트를 얻습니다.")  ##상황별 수정 필요!
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
    print('\n[System] ', ment)


def yesorno():
    nkind = 0
    while True:
        reply = input(f'\n>> 수락하려면 y를, 거절하려면 n을 입력하세요.\n입력 :')
        # print(reply, reply == 'y' , reply=='Y')
        if str(reply) == 'y' or str(reply) == 'Y':
            return nkind
            break
        elif str(reply) == 'n' or str(reply) == 'N':
            sys('인성이 -10 되었습니다.')
            nkind += 10
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


#####################################시작 > 개발몬 선택하기########################################

start = input("System : 게임을 시작하려면 'f'를 입력하세요.")

if start == "f" or start == "F":
    print()
print("-------------------캐릭터 선택화면----------------------")
print("선택 1. 쩡 [추리반 부장]")
print("- 개발 레벨 : 레벨 4")
print("- 개발 스킬 : 추리 능력 (야구/ 가위바위보 미션 시 스킬사용가능")
print("- 인성 : 80")
print("******************************************************")
print(" 선택 2. 수빈 [운동부 부장]")
print("- 개발 레벨 : 레벨 4")
print("- 개발 스킬 : 운동 능력 (댄스배틀/ 고양이 구출 미션 시 스킬사용가능")
print("- 인성 : 95")
print("******************************************************")

choice_num = int(input("개발몬을 선택하세요."))
##숫자(1~2일때만)##
playerList[choice_num]['name']
print(f"System : {pName} 개발몬 선택 ")
########미션01 종료 ########
pLoc = 6

####################################미션00###################################
while pLoc == 0:
    sys(f"{Loc[pLoc]} 입니다.")
    npc = "이하복 교수님"

    conv(pName, "교수님 졸업 시켜주세요.")
    conv(npc, " 너 레벨이 몇이니?")
    conv(pName, f"{pLevel} 입니다.")

    if pLevel < 10:
        conv(npc, "졸업하기엔 개발 레벨이 낮구나.")
        conv(npc, "미션을 줄테니 레벨 10이되면 다시 찾아오거라.")
    elif pLevel == 10:
        conv(npc, "졸업 축하한다.")

####################################미션01###################################

while pLoc == 1:
    ########미션01 시작 초기 변수 설정 ########
    sys(f"{Loc[pLoc]} 입니다.")
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
    conv(npc, f"{pName}! 여기서 뭐하고 있어?")
    conv(pName, "약 받으러 왔는데 양호선생님이 안계셔서 그냥 가려고.")
    conv(npc, f"뭐? 난 지금 약이 꼭 필요한데.. {pName}아 너가 약 좀 찾아줄래?")
    pKind - yesorno()

    ########미션01-2 미션 수행 ########
    while True:
        print('=' * 50)
        conv(npc, f"나의 증상은 {sickList[sickIdx]}이야.")
        print(f'약품 리스트의 값은 다음과 같습니다. {mediList}')
        ms01 = input('증상에 맞는 약의 값을 구할 수 있도록 다음의 코드를 완성하세요.\ncode : mediList[?] : ')
        if sickIdx == int(ms01):
            print('=' * 50)
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

#####################################미션05########################################
while pLoc == 5:
########미션05 종료 ########
    pLoc = 6

#####################################미션06########################################
while pLoc == 6:
    ########미션01 시작 초기 변수 설정 ########
    sys(f"{Loc[pLoc]} 입니다.")
    npc = "내 친구 기아 양현종"
    ##야구게임 정답##
    num_lst = []
    # 중복체크
    for i in range(0, 3):
        num_lst.append(random.randint(1, 9))  # random.randint 1부터 9까지 정수 중 하나를 무작위로 선택해 num_lst에 추가
    # print("처음 num_lst: ",num_lst)

    for i in range(0, 3):
        for j in range(0, 3):
            if i != j:
                if num_lst[i] == num_lst[j]:
                    # print(num_lst[i],num_lst[j])
                    num_lst[j] = random.randint(1, 9)
                # else:
    print("중복체크 else: ",num_lst)
    ## 스킬 발현 ##
    if pLoc in playerList[pIdx]['skill']:
        pSkill = skill_succ  # True if (random.choices((0, 1), choice)) else False
    else:
        pSkill = False

    ########미션06-1 상황설명 ########
    conv(pName, "양호선생님이 부재중이시다.")
    input('>> 계속하려면 아무 키나 입력하세요.\n')
    situ(f"{npc}가 양호실에 들어왔다.")
    conv(npc, f"{pName}! 여기서 뭐하고 있어?")
    conv(pName, "약 받으러 왔는데 양호선생님이 안계셔서 그냥 가려고.")
    conv(npc, f"뭐? 난 지금 약이 꼭 필요한데.. {pName}아 너가 약 좀 찾아줄래?")
    pKind - yesorno()

    ########미션06-2 미션 수행 ########

    print('=' * 50)
    conv(npc, f"나의 .")  # 현종이대사
    if pSkill:
        print("* Hint : 첫번째 자리 숫자 >>", num_lst[0])
    # 1round - 9round
    for r in range(0, 2):
        strike_cnt = 0
        ball_cnt = 0
        out_cnt = 0
        # round 1 출력
        print(f"[ {r + 1} Round ]")
        # 사용자 입력값 받기
        num1 = list(input("1 ~ 9까지 ,를 사용하여 입력하세요 :"))
        # 사용자 입력값 리스트
        user_num = []
        for i in range(0, len(num1)):
            if i % 2 == 0:
                user_num.append(num1[i])
        # 문자가 원소인 리스트 int형 리스트로 형 변환하기
        user_num = list(map(int, user_num))

        # 라운드 별 strike, ball, out 구분
        for i in range(0, 3):
            for j in range(0, 3):
                if num_lst[i] != int(user_num[j]):
                    out_cnt = out_cnt + 1
                elif i == j:
                    if num_lst[i] == user_num[j]:
                        strike_cnt = strike_cnt + 1
                else:
                    if num_lst[i] == user_num[j]:
                        ball_cnt = ball_cnt + 1
        if strike_cnt + ball_cnt == 0:
            print("out")
            print("---------------------------")
        # 9라운드 전에 정답을 맞힐경우
        elif strike_cnt == 3:
            print("정답입니다. 9라운드 되기전 맞춘 숫자 천재 ")
            # print(num_lst)
            break
        else:
            print("strike: ", strike_cnt)
            print("ball: ", ball_cnt)
            print("---------------------------")

        #######미션 성공 실패판단 부분 // + 실패시 재도전 만들기##########
        sys("미션 성공입니다.")
        print()
        print(f"{npc}: 너 야구부에 들어 올지 않을래?")
        print(f"{pName}: 아니 나는 졸업해서 개발자가 될꺼야")
        ################################################################

        ########미션06 이동 전 독백 ########
        print()
        print()
        conv(pName, "이제 다른 곳으로 이동 하자.")
        input('>> 계속하려면 아무 키나 입력하세요.\n')
        sys("양호실에서 나왔습니다.")
        print()
        situ("♪~~♩~♬")
        conv(pName, "이건 어디서 들리는 음악소리지? 음악실인것 같은데 가볼까?")
        input('>> 계속하려면 아무 키나 입력하세요.\n')

        print("미션  교무실로 이동 ")
        ########미션01 종료 ########
    pLoc = 7

#while pLoc == 7:
#    print('마지막 교무실')