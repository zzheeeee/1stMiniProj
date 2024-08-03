# 합 작업 파일 (07/31 15:43 인트로, 미션1, 미션6 완료 버전)
## 합 작업 파일 (07/31 19:30 인트로, 미션1~미션6 완료 버전)

################################## ▼ 초기값 ▼ ###################################
import random
import time
#미션 번호 0 // 미션 1 ~ 7
Loc = ['교무실', '양호실', '음악실', '매점', '도서실', '운동장 가는 길', '운동장','교무실']
# 이름, 레벨, 인성, 체중, 스킬발동레벨
hee = {'name':'쩡','level':4, 'kind':80, 'weight':0, 'skill':[6,7]}
cha = {'name':'수빈','level':4, 'kind':100, 'weight':0, 'skill':[2,5]}
playerList = [hee, cha]
pIdx = 0 #random.randint(0,1)
pName = playerList[pIdx]['name']
pLevel = playerList[pIdx]['level']
pKind = playerList[pIdx]['kind']
pWeight = playerList[pIdx]['weight']
################################## ▲ 초기값 ▲ ##################################

################################## ▼  함수  ▼ ##################################
##### 스킬 성공
def skill_succ():
    pSkillTrue = random.randint(1, 100)
    if pSkillTrue >= 15:
        if pLoc == 2 or pLoc == 5:
            print(f"{pName}의 스킬이 발동했습니다! 운동신경을 100% 발휘하여 카운트 하나를 감소합니다.")
        elif pLoc == 6 or pLoc == 7:
            print(f"{pName}의 스킬이 발동했습니다! 추리력을 100% 발휘하여 상대방을 꿰뚫어 볼 수 있습니다.")
        return True
    else:
        print("System : 스킬 발동에 실패했습니다.")
        return False

##### conv : 대화 출력
def conv(speaker, ment):
    print(f"{speaker}: {ment}")

##### situ : 상황 출력
def situ(ment):
    print('\n')
    print(ment)

##### sys : 시스템 출력
def sys(ment):
    print('\n',ment)

##### yes or no 선택
def yesorno():
    nkind = 0
    while True:
        reply = input(f'\n>> 수락하려면 y를, 거절하려면 n을 입력하세요.\n입력 :')
        if str(reply) == 'y' or str(reply) == 'Y':
            return nkind
            break
        elif str(reply) == 'n' or str(reply) == 'N':
            sys('인성이 -10 되었습니다.')
            nkind += 10
            continue
        else:
            continue

##### 야구 문제
def mis_baseball(name):
    # 1round - 9round
    for r in range(0, 9):
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
        # 문자가 원소인 리스트를 int형 리스트로 형 변환하기
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
        if r + 1 == 9 :
            if strike_cnt != 3 :
                sys("미션 실패하였습니다.")
                conv(name,"오이 오이 제대로 머리를 쓰라구 다시 해봐")
                return mis_baseball()
################################## ▲  함수  ▲ ##################################

################################ ▼ 게임 시작 화면 ▼ #################################
# 도트아트 추가하기
input('>> 시작하려면 아무 키나 입력하세요.\n')
################################ ▲ 게임 시작 화면 ▲ #################################

################################ ▼ 개발몬 선택 ▼ #################################
print("**************************개발몬**************************")
print("선택 1. 쩡 [추리반 부장]")
print(" - 개발 레벨 : 레벨 4")
print(" - 개발 스킬 : 추리 능력 (야구/ 가위바위보 미션 시 스킬사용가능)")
print(" - 인성 : 80")
print("********************************************************")
print("선택 2. 수빈 [운동부 부장]")
print(" - 개발 레벨 : 레벨 4")
print(" - 개발 스킬 : 운동 능력 (댄스배틀/ 고양이 구출 미션 시 스킬사용가능)")
print(" - 인성 : 95")
print("********************************************************")
while True:
    choice = input("게임을 진행할 개발몬의 번호를 입력하세요.")
    print(choice)
    if int(choice) == 1:
        pName = playerList[0]['name']
        conv(pName, "요로시쿠네~~~><")
        break
    elif int(choice) == 2:
        pName = playerList[1]['name']
        conv(pName, "잘부탁한다구!~~!~!~!~!")
        break
    else: continue
################################ ▲ 개발몬 선택 ▲ #################################
pLoc = 0
################################## ▼ 인트로 ▼ ###################################
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

    #인트로 종료
    pLoc = 1
################################## ▲ 인트로 ▲ ###################################

################################## ▼ 미션01 ▼ ###################################
while pLoc==1:
    #시작 초기 변수 설정
    print(f"System : {Loc[pLoc]} 입니다.")
    npc = "종이인형 황광희"

    # 스킬 발현
    if pLoc in playerList[pIdx]['skill']:
        pSkill = skill_succ  # True if (random.choices((0, 1), choice)) else False
        offset = 1 if pSkill else 0
    else:
        pSkill = False
        offset = 0

    ## 증상 리스트, 처방 리스트, 랜덤 인덱스 ##
    sickList = ['두통', '속쓰림', '감기기운', '소화불량', '근육통']
    mediList = ['진통제', '위장약', '감기약', '소화제', '파스']
    sickIdx = random.randint(0, len(sickList) - 1)

    #미션01-1 상황설명 ########
    conv(pName, "양호선생님이 부재중이시다.")
    situ(f">> {npc}가 양호실에 들어왔다.\n")
    input('>> 계속하려면 아무 키나 입력하세요.\n')
    conv(npc,f"{pName}! 여기서 뭐하고 있어?")
    conv(pName, "약 받으러 왔는데 양호선생님이 안계셔서 그냥 가려고.")
    conv(npc, f"뭐? 난 지금 약이 꼭 필요한데.. {pName}아 너가 약 좀 찾아줄래?")
    yesorno()

    #미션01-2 미션 수행 ########
    while True:
        print('='*50)
        conv(npc, f"나의 증상은 {sickList[sickIdx]}이야.")
        print(f'약품 리스트의 값은 다음과 같습니다. {mediList}')
        ms01 = input('증상에 맞는 약의 값을 구할 수 있도록 다음의 코드를 완성하세요.\ncode : mediList[?] : ')
        if sickIdx == int(ms01):
            print('='*50)
            conv(npc, f"나한테 딱 맞는 약이야. {pName}아, 정말 고마워!")
            sys("레벨이 1 올랐습니다.")
            pLevel += 1
            break
        elif sickIdx > int(ms01) or sickIdx < int(ms01):
            conv(npc, f"음... 이건 나의 증상에 맞지 않은 약인 것 같은데?")
            continue
    #미션01 이동 전 독백 ########
    print()
    print()
    conv(pName, "이제 다른 곳으로 이동 하자.")
    input('>> 계속하려면 아무 키나 입력하세요.\n')
    sys("양호실에서 나왔습니다.")
    print()
    situ("♪~~♩~♬")
    conv(pName, "이건 어디서 들리는 음악소리지? 음악실인것 같은데 가볼까?")
    input('>> 계속하려면 아무 키나 입력하세요.\n')

    #미션01 종료
    pLoc = 2
################################## ▲ 미션01 ▲ ###################################

################################## ▼ 미션02 ▼ ###################################
while pLoc == 2:
    # 시작 초기 변수 설정
    print(f"System : {Loc[pLoc]} 입니다.")
    npc = "뉴진스 민지"

    # 스킬 발현
    if pLoc in playerList[pIdx]['skill']:
        pSkill = skill_succ  # True if (random.choices((0, 1), choice)) else False
        offset = 1 if pSkill else 0
    else:
        pSkill = False
        offset = 0

    #미션02만의 변수 설정
    danceList = []
    answerList = []
    for i in range(1, 11):
        answer = ''
        dance = ''
        for j in range(0,(i//2)+3-offset):
            rd = random.randint(0,3)
            if rd == 0:
                dance = dance+'↑ '
                answer = answer+'w'
            elif rd == 1:
                dance = dance+'← '
                answer = answer + 'a'
            elif rd == 2:
                dance = dance+'↓ '
                answer = answer + 's'
            elif rd == 3:
                dance = dance+'→ '
                answer = answer + 'd'
        danceList.append(dance)
        answerList.append(answer)

    #미션02-1 상황설명
    input('>> 계속하려면 아무 키나 입력하세요.\n')
    situ(f'{npc}가 춤을 추고 있다.')
    conv(pName, f"{npc}야 지금 뭐해?")
    conv(npc, f"{pName}! 나 춤 연습 하고 있어. 마침 혼자 춤 추기 외로웠는데 너도 같이 추자! 댄스 배틀 레쓰고~~!")
    pKind -= yesorno()

    #미션02-2 미션 수행
    while True:
        input('>> 미션을 시작하려면 아무 키나 입력하세요.\n')
        lv = 0
        print('=' * 50)
        print('-' * 50)
        print(f'↑: w / ←: a / ↓: s / →: d')
        print(f'별도의 구분없이 연속으로 입력하세요. (예시) ↓ ↑ ↓ → : swsd')
        print('-' * 50)
        conv(npc, f"내 움직임을 따라해봐.")
        while True:
            dance = input(f'\n{danceList[lv]}: ')
            if dance == answerList[lv]:
                if lv == len(answerList)-1:
                    conv(npc, f"춤 좀 추는데?")
                    break
                else:
                    lv += 1
                    continue
            else:
                conv(npc, f"이런, 스텝이 꼬였구나. 몸 좀 풀고 다시 도전해봐.")
        break

    sys("레벨이 1 올랐습니다.")
    pLevel += 1

    #미션02-3 이동 전 독백
    conv(pName, f"아, 춤을 췄더니 배가 너무 고프네.")
    conv(pName, f"매점에 가볼까?")
    input('>> 계속하려면 아무 키나 입력하세요.\n')
    sys("양호실에서 나왔습니다.")

    #미션02 종료
    pLoc = 3
################################## ▲ 미션02 ▲ ###################################

################################## ▼ 미션03 ▼ ###################################
while pLoc == 3:
    # 스킬발현
    if pLoc in playerList[pIdx]['skill']:
        pSkill = skill_succ  # True if (random.choices((0, 1), choice)) else False
        offset = 1 if pSkill else 0
    else:
        pSkill = False
        offset = 0

    # 미션03 시작 초기 변수 설정
    sys(f"{Loc[pLoc]} 입니다.")
    npc = "혜자로우신 매점 아주머니"

    # 미션03-1 상황설명
    conv(pName, "너무 열심히 췄더니 배고프다 (꼬르륵 꼬르륵)")
    input('>> 계속하려면 아무 키나 입력하세요.\n')
    conv(pName, "사장님 크림빵이랑 딸기우유 주세요")
    conv(npc, "잠깐 기다려 주겠니? 빵 정리를 못 끝내서 ")
    situ(f"{npc}가 곤란하신 상황인거 같다.")
    situ(f"{npc}를 도와주자")
    pKind - yesorno()

    # 미션03-2 미션 수행
    situ(f"매점 선반에는 15칸으로 이루어져있습니다.")
    conv(npc, "빵이 왜 칸에 맞게 안들어가는거지?? ")
    situ(f"매점 아주머니께 올바른 질문을 찾아주세요.")
    while True:
        que = int(input("(1) 선반에 들어갈 빵이 총 몇개 인가요? \n(2) 백종원님을 불러올까요? \n(3) 빵이 총 얼마인가요?\n\n"))
        if que == 1:
            conv(npc, "16개란다.")
            conv(pName,"흠... 선반 칸과 맞지 않은걸 선반 칸을 늘려 드려야겠다.")
            break
        elif que != 1:
            conv(npc, "질문을 다시 해주겠니?")
            continue
    while True:
        situ(f"선반에 빵을 알맞게 넣기 위해 선반범위가 알맞은것을 고르시오.")
        que = int(input("(1) range(1,15,1)\n(2) range(0,15,1)\n(3) range(14,0,-1)\n(4) range(0,16,1)\n\n"))
        if que == 4:
            conv(npc, f"{pName}이는 리스트 범위를 잘 이해하고 있구나. 똑똑한 개발몬이 되겠어~")
            print("System : 레벨이 1 올랐습니다.")
            pLevel += 1
            break
        else:
            conv(npc, f"{pName}이는 리스트 범위를 이해하지 못했지만 다시한번 맞춰보렴")
            continue

    # 미션02-3 이동 전 독백
    print()
    print()
    conv(pName, "이제 다른 곳으로 이동 하자.")
    input('>> 계속하려면 아무 키나 입력하세요.\n')
    sys("매점에서 나왔습니다.")
    print()

    # 미션03 종료
    pLoc = 4
################################## ▲ 미션03 ▲ ###################################

################################## ▼ 미션04 ▼ ###################################
while pLoc == 4:
    # 스킬발현
    if pLoc in playerList[pIdx]['skill']:
        pSkill = skill_succ  # True if (random.choices((0, 1), choice)) else False
        offset = 1 if pSkill else 0
    else:
        pSkill = False
        offset = 0
    # 미션04만의 변수 설정
    date=["07-31","07-15","07-02","06-27","06-11"]
    name = ["뉴진스 다니엘","아이브 유진","르세라핌 채원","에스파 닝닝","아이브 원영"]
    book=["엑셀X파이썬","혼자공부하는 머신러닝+딥러닝","오렌지3 with 파이썬","비전공자를 위한 이해할 수 있는 파이썬","파이썬 머신러닝 판다스 데이터 분석"]
    born_book = ["길벗","한빛미디어","생능북스","티더블유아이지","정보문화사"]
    write=["정성일","박해선","김현철","최원영","오승환"]
    npc = "내친구 차은우"
    num = random.randint(0, 4)

    # 미션04-1 상황설명
    conv(pName, "이제 배를 채웠으니 마음의 양식을 쌓으러 가볼까?")
    input('>> 계속하려면 아무 키나 입력하세요.\n')
    sys(f"{Loc[pLoc]} 입니다.")
    conv(npc, f"{pName}아 {name[num]}가 빌린 책을 나도 보고싶은데....")
    conv(npc, "대출목록 종이가 찢어져 있어서 못찾겠어 찾는걸 도와줄래??")
    pKind -= yesorno()

    # 미션04-2 미션 수행
    situ("찢어진 대출목록 이다.")
    # 비전공자를 위한 이해할 수 있는 파이썬

    st = book[num].replace(book[num], "//////////")
    book[num] = st
    print(book[num])
    print("num>",num)
    for i in range(0,5):
        book_lst = [date[i],name[i],book[i],born_book[i],write[i]]
        print(book_lst)
    while True:
        situ(f"{name[num]}가 빌린 책을 찾으려면 인덱스 몇을 입력하면 보여줄까?")
        res_book = int(input("입력 : "))
        if res_book == num:
            conv(npc, f"{pName}이 {name[num]}이가 빌린 책을 알게됐어~ ")
            conv(npc, f"{pName}아 너무 고마워 ")
            print("System : 레벨이 1 올랐습니다.")
            pLevel += 1
            break
        else:
            sys("미션 실패 했습니다. 차은우를 도와주세요.")
            continue

    # 미션04-3 이동 전 독백
    conv(pName, "아까 먹은 빵 소화가 안되네. 운동장 한바퀴 걷고 올까?")
    pWeight -= yesorno()
    situ(f"{Loc[pLoc]}에서 나왔습니다.")
    input('>> 계속하려면 아무 키나 입력하세요.\n')
    situ("야옹 야오오옹 (무섭다냥)")
    conv(pName, "이게 무슨 소리지???")
    situ("소리가 나는 쪽으로 달려간다. (우다다다다다)")
    situ("나무위에 춘식이를 발견했습니다.")
    # 미션04 종료
    pLoc = 5
################################## ▲ 미션04 ▲ ##################################

################################## ▼ 미션05 ▼ ###################################
while pLoc==5:
    # 시작 초기 변수 설정
    print(f"System : {Loc[pLoc]} 입니다.")
    npc = "귀여운 춘식이"

    # 스킬 발현
    if pLoc in playerList[pIdx]['skill']:
        pSkill = skill_succ  # True if (random.choices((0, 1), choice)) else False
        offset = 1 if pSkill else 0
    else:
        pSkill = False
        offset = 0

    # 미션05만의 변수 설정
    riseList = []
    answerList = []
    for i in range(0, 5):
        answer = ''
        rise = ''
        for j in range(0, 5-offset):
            rd = random.randint(0, 3)
            if rd == 0:
                rise = rise + '↑ '
                answer = answer + 'w'
            elif rd == 1:
                rise = rise + '← '
                answer = answer + 'a'
            elif rd == 2:
                rise = rise + '↓ '
                answer = answer + 's'
            elif rd == 3:
                rise = rise + '→ '
                answer = answer + 'd'
        riseList.append(rise)
        answerList.append(answer)



    # 미션05-1 상황설명
    input('>> 계속하려면 아무 키나 입력하세요.\n')
    conv(pName,f"{npc}가 무서워하고있어! 얼른 구해주자!")
    pKind -= yesorno()

    # 미션05-2 미션 수행
    while True:
        input('>> 미션을 시작하려면 아무 키나 입력하세요.\n')
        lv = 0
        print('=' * 50)
        print('-' * 50)
        print(f'↑: w / ←: a / ↓: s / →: d')
        print(f'별도의 구분없이 연속으로 입력하세요. (예시) ↓ ↑ ↓ → : swsd')
        print('-' * 50)
        conv(npc, f"야옹~~ (나를 구해 줘 라는 뜻)")
        conv(pName, f"나무에 올라 {npc}를 구하자!")
        while True:
            rise = input(f'\n{riseList[lv]}: ')
            if rise == answerList[lv]:
                if lv == 0 or lv == 1 or lv == 2 :
                    situ("나무를 조금 올랐습니다.")
                    lv += 1
                    continue
                elif lv == 3:
                    situ("거의 다 올랐습니다.")
                    lv += 1
                    continue
                elif lv == 4:
                    situ("나무를 다 올랐습니다.")
                    print( )
                    conv(pName, f"{npc}를 구했다!")
                    conv(npc, f"야옹♥ (고맙다는 뜻)")
                    break
            else:
                conv(npc, f"야옹!!!!!! (힘을 내달라는 뜻)")
        break
    print("System : 레벨이 1 올랐습니다.")
    pLevel += 1
    break

    # 미션05-3 이동 전 독백
    conv(pName, f"춘식이는 땅에 내려놓자마자 어디론가 도망가버렸다.")
    conv(pName, f"운동장으로 계속 가볼까?")
    input('>> 계속하려면 아무 키나 입력하세요.\n')

    # 미션05 종료
    pLoc = 6
################################### ▲ 미션05 ▲ ###################################

################################### ▼ 미션06 ▼ ###################################
while pLoc == 6:
    # 미션01 시작 초기 변수 설정
    sys(f"{Loc[pLoc]} 입니다.")
    npc = "내 친구 기아 양현종"
    # 야구게임 정답
    num_lst = []
    # 중복체크
    for i in range(0, 3):
        num_lst.append(random.randint(1, 9))

    for i in range(0, 3):
        for j in range(0, 3):
            if i != j:
                if num_lst[i] == num_lst[j]:
                    # print(num_lst[i],num_lst[j])
                    num_lst[j] = random.randint(1, 9)
    # 스킬 발현
    if pLoc in playerList[pIdx]['skill']:
        pSkill = skill_succ  # True if (random.choices((0, 1), choice)) else False
    else:
        pSkill = False

    # 미션06-1 상황설명
    conv(pName, "소화시키러 운동장으로 가볼까~ 룰루 ")
    input('>> 계속하려면 아무 키나 입력하세요.\n')
    situ(f"{npc}가 말을 걸었다.")
    conv(npc, f"{pName}! 여기서 뭐하고 있어?")
    conv(pName, "소화 시킬 겸 산책하려고")
    conv(npc, f"소화 시킬 겸 머리쓰는 야구 게임 해볼래?")
    pKind -= yesorno()

    #미션06-2 미션 수행
    print('=' * 50)
    conv(npc, f"기대해 이제부터 야구 게임을 시작하지.")  # 현종이대사
    if pSkill:
        print("* Hint : 첫번째 자리 숫자 >>", num_lst[0])

    #미션 06 수행 함수 선언
    mis_baseball(npc)
    sys("미션 성공입니다.")
    print("System : 레벨이 1 올랐습니다.")
    pLevel += 1
    print()
    print(f"{npc}: 너 야구부에 들어 오지 않을래?")
    print(f"{pName}: 아니 나는 졸업해서 개발자가 될꺼야")

    #미션06 이동 전 독백
    print()
    print()
    conv(pName, "이제 다른 곳으로 이동 하자.")
    input('>> 계속하려면 아무 키나 입력하세요.\n')
    sys("운동장에서 나왔습니다.")
    print()
    conv(pName, "개발레벨이 10이 된거 같은데 교무실로 이동하자")
    input('>> 계속하려면 아무 키나 입력하세요.\n')

    print("미션 교무실로 이동 ")

    #미션 06 종료
    pLoc = 7
################################### ▲ 미션06 ▲ ###################################

################################### ▼ 미션07 ▼ ###################################
while pLoc ==7:
    # 시작 초기 변수 설정
    print(f"System : {Loc[pLoc]} 입니다.")
    npc = "이하문 교수님"

    # 스킬 발현
    if pLoc in playerList[pIdx]['skill']:
        pSkill = skill_succ  # True if (random.choices((0, 1), choice)) else False
        offset = 1 if pSkill else 0
    else:
        pSkill = False
        offset = 0

    # 미션07-1 변수 설정

    teacher = []
    rsp = ['가위', '바위', '보']

    for i in range(3):
        teacher.append(random.choice(rsp))
    print(teacher)

    # 미션 07-2 상황설명

    # 미션 07-3 미션 수행

    # 미션 07-4 수행 함수 선언
    round = 1

    while True:
        while round <= 3:
            player = input(f"[Round {round}] 가위, 바위, 보 중 하나를 입력하세요 :")
            print(player)
            if player == '가위' or player == '바위' or player == '보':
                i = round - 1
                print(teacher[i], player)
                if teacher[i] == '가위' and player == '가위':
                    print('teacher: 비김')
                    print("⠀⠀⠀⡴⠒⢦⠀⠀⢰⠒⢲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠠⡞⠉⢦⠀⠀⡴⠋⢳⠀")
                    print("⠀⠀⠀⢻⠀⠘⡆⢀⡏⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠘⡆⢰⠇⠀⡾⠀")
                    print("⠀⠀⠀⠘⡇⠀⢹⣼⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⡆⠀⢻⡞⠀⢰⠇⠀")
                    print("⢀⣀⣴⠋⢻⡦⠤⠧⣤⣼⡇⠀⠀⠀⠀⠀⠀⠀⣀⣤⣞⠉⣻⠶⠶⠶⠤⣾⡀⠀")
                    print("⢿⠀⠹⣆⠘⣦⣤⡄⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⢧⠀⢹⣄⠙⣶⣦⠀⠀⠀⢳⠀")
                    print("⠘⣧⠴⠟⠛⠉⡟⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠸⣷⠞⠋⠉⠁⠏⠀⠀⠀⡼⠀")
                    print("⠀⠙⢦⣀⣀⣀⣀⣀⣀⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣄⣀⣀⣀⣀⡤⠞⠁⠀")
                elif teacher[i] == '가위' and player == '보':
                    print('teacher: 내가 이겼단다')
                    print("⠀⠀⠀⢀⣀⡀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⢯⠀⢹⡄⠀⣼⠁⢸⡇⠀⠀⠀⠀⠀⠀⢠⡚⢢⠀⡇⢸⠀⢰⠛⡆⠀⠀")
                    print("⠀⠀⠀⠸⡄⠀⢧⢠⠇⠀⣼⠀⠀⠀⠀⠀⢀⣀⠀⡇⠘⡄⡇⢸⠀⡇⢰⠁⠀⠀")
                    print("⠀⠀⢀⣤⣷⠀⠘⡟⠀⢀⡇⠀⠀⠀⠀⠀⠸⡀⢣⣿⠀⢷⠇⠸⡿⠀⡎⠀⣀⡀")
                    print("⣰⠒⢿⡀⢸⡋⠉⠙⠛⠻⣇⠀⠀⠀⠀⠀⠀⠱⡀⠙⠀⠀⠀⠀⠀⢰⡷⠊⢁⡇")
                    print("⢹⡄⠈⣷⣤⡿⣻⠃⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⢀⠔⠋⠀⠀⡰⠋⠀")
                    print("⠀⢿⡉⠁⠀⠀⠋⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠈⠀⠀⠀⡰⠁⠀⠀")
                    print("⠀⠀⠙⠲⠶⠖⠶⠶⠒⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠒⠒⠒⠊⠀⠀⠀⠀")

                elif teacher[i] == '가위' and player == '바위':
                    print('teacher: 네가 이겼단다')
                    print("⠀⠀⠀⣴⠒⢦⠀⠀⢠⠖⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⣀⡀⠀⠀")
                    print("⠀⠀⠀⢹⡀⠘⡇⠀⡞⠀⢸⠃⠀⠀⠀⠀⠀⢀⡴⠦⡞⠉⢹⡇⠀⣿⠁⢹⡆⠀")
                    print("⠀⠀⠀⠈⣇⠀⢹⣸⠃⠀⡾⠀⠀⠀⠀⠀⠀⢸⠀⠀⡇⠀⢸⡇⢀⣿⡀⢸⣧⠀")
                    print("⠀⣀⣰⠚⢻⣤⣤⣯⣤⣰⡇⠀⠀⠀⠀⠀⠀⠸⣦⡤⠿⢶⡟⠉⠉⠉⠉⠙⠻⡇")
                    print("⢾⠉⠹⣆⠘⣦⣤⡀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠙⢲⡶⠀⠀⠀⢸⠃")
                    print("⠈⣧⡤⠟⠒⠋⣾⠀⠀⠀⢨⠇⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⠈⠁⠀⠀⣠⠏⠀")
                    print("⠀⠘⢦⣀⠀⠀⠀⠀⣀⡠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠒⠒⠒⠒⠒⠋⠁⠀⠀")
                    print("⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                elif teacher[i] == '바위' and player == '바위':
                    print('teacher: 비김')
                    print("⠀⣀⣀⡤⠶⣴⠚⠓⡶⠒⢢⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⠶⢦⡞⠛⢶⠒⠲⡄⠀")
                    print("⣾⠀⢸⡇⠀⢸⠀⠀⡇⠀⢸⡀⠀⠀⠀⠀⠀⢰⠃⠈⡇⠀⢸⡇⠀⢸⠀⠀⣇⠀")
                    print("⣿⠀⢸⣇⣠⠾⠶⠶⠷⠦⢼⣷⠀⠀⠀⠀⠀⢸⡄⢀⣧⣀⡼⠷⠶⠾⠶⢴⡿⡄")
                    print("⢸⠉⠉⠀⠹⣄⣀⣀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⡏⠉⠀⠈⢧⣀⣀⠀⠀⠀⢀⡇")
                    print("⠈⣇⠀⠀⠀⠀⠸⠁⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠰⠇⠀⠀⠀⡼⠀")
                    print("⠀⠘⢦⣀⣀⣀⣀⣀⣀⡤⠊⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⣀⣀⣀⣀⣀⡤⠞⠁⠀")
                elif teacher[i] == '바위' and player == '가위':
                    print('teacher: 내가 이겼단다')
                    print("⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡖⠙⢦⠀⠀⣴⠚⢲⠀")
                    print("⠀⣀⣀⡤⠶⣴⠚⠓⡶⠒⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠘⡆⢠⠇⠀⡼⠀")
                    print("⣾⠀⢸⡇⠀⢸⠀⠀⡇⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⢻⡾⠀⢠⡇⠀")
                    print("⣿⠀⢸⣇⣠⠾⠶⠶⠷⠦⢼⣷⠀⠀⠀⠀⠀⠀⢀⣠⡞⠉⣻⠶⠶⠤⠤⣼⡀⠀")
                    print("⢸⠉⠉⠀⠹⣄⣀⣀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⢯⠀⢹⡄⠙⣦⣤⠀⠀⠈⢳⠀")
                    print("⠈⣇⠀⠀⠀⠀⠸⠁⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⠸⣦⠴⠛⠛⠁⡏⠀⠀⠀⣸⠀")
                    print("⠀⠘⢦⣀⣀⣀⣀⣀⣀⡤⠊⠀⠀⠀⠀⠀⠀⠀⠀⠙⢤⣀⣀⣀⣀⣀⣠⠔⠁⠀")
                elif teacher[i] == '바위' and player == '보':
                    print('teacher: 네가 이겼단다')
                    print("⠀⠀⠀⠀⠀⠀      ⠀⠀⠀⠀⠀⠀⠀⠀⡤⣄⠀⡎⢱⠀⢀⠤⡄⠀⠀")
                    print("⠀⣀⣀⡤⠶⣴⠚⠓⡶⠒⢢⠀⠀⠀⠀⠀⠀⠀⠈⡇⢸⠀⡇⢸⠀⡜⢀⠇⠀⠀")
                    print("⣾⠀⢸⡇⠀⢸⠀⠀⡇⠀⢸⡀⠀⠀⠀⠀⢸⠙⢆⢣⠀⣇⡇⢸⣤⠁⡸⠀⠀⠀")
                    print("⣿⠀⢸⣇⣠⠾⠶⠶⠷⠦⢼⣷⠀⠀⠀⠀⠈⢣⠈⠾⠀⠈⠁⠀⠉⢀⣇⠴⠊⡦")
                    print("⢸⠉⠉⠀⠹⣄⣀⣀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⣠⠤⠈⠁⢀⠔⠁")
                    print("⠈⣇⠀⠀⠀⠀⠸⠁⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠸⠁⠀⠀⢠⠇⠀⠀")
                    print("⠀⠘⢦⣀⣀⣀⣀⣀⣀⡤⠊⠀⠀⠀⠀⠀⠀⠀⠀⠘⠦⠤⠤⢤⣤⠴⠋⠀⠀⠀")
                elif teacher[i] == '보' and player == '보':
                    print('teacher: 비김')
                    print("⠀⠀⠀⡤⢤⠀⡜⠉⡆⠀⡤⢤⠀⠀⠀⠀⠀⠀⠀⡤⢤⠀⡜⠉⡆⠀⡤⢤⠀⠀")
                    print("⠀⠀⠀⢱⠀⡇⣇⠀⡇⢰⠁⡞⠀⠀⠀⠀⠀⠀⠀⢱⠀⡇⣇⠀⡇⢰⠁⡞⠀⠀")
                    print("⠰⡍⠱⣸⡄⢸⣿⠀⣇⡇⢰⠃⠀⠀⠀⠀⠰⡍⠱⣸⡄⢸⣿⠀⣇⡇⢰⠃⠀⠀")
                    print("⠀⠹⡄⠹⠇⠀⠁⠀⠉⠀⣾⡤⠚⢳⠀⠀⠀⠹⡄⠹⠇⠀⠁⠀⠉⠀⣾⡤⠚⢳")
                    print("⠀⠀⠙⡄⠀⠀⠀⣠⠴⠂⠉⢀⡴⠁⠀⠀⠀⠀⠙⡄⠀⠀⠀⣠⠴⠂⠉⢀⡴⠁")
                    print("⠀⠀⠀⢳⠀⠀⠐⠃⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠐⠃⠀⠀⢀⡞⠀⠀")
                    print("⠀⠀⠀⠀⠓⠤⠤⠤⠤⠤⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠤⠤⠤⠤⠤⠊⠀⠀⠀")

                elif teacher[i] == '보' and player == '바위':
                    print('teacher: 내가 이겼단다')
                    print("⠀⠀⠀⣀⡀⠀⡤⠢⡀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⣀⡀⠀⠀")
                    print("⠀⠀⠀⡇⢸⠀⡇⠀⡇⢸⠀⡇⠀⠀⠀⠀⠀⢀⡴⠦⡞⠉⢹⡇⠀⣿⠁⢹⡆⠀")
                    print("⢠⠒⣄⢱⠀⣇⡇⠀⣇⠇⢰⠁⠀⠀⠀⠀⠀⢸⠀⠀⡇⠀⢸⡇⢀⣿⡀⢸⣧⠀")
                    print("⠈⢆⠘⣾⡄⠘⠃⠀⠛⠀⡎⣀⠤⢄⠀⠀⠀⠸⣦⡤⠿⢶⡟⠉⠉⠉⠉⠙⠻⡇")
                    print("⠀⠈⢆⠀⠀⠀⠀⢀⣀⠐⠛⠁⡠⠃⠀⠀⠀⠀⣇⠀⠀⠀⠙⢲⡶⠀⠀⠀⢸⠃")
                    print("⠀⠀⠈⡆⠀⠀⢰⠋⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⠈⠁⠀⠀⣠⠏⠀")
                    print("⠀⠀⠀⠘⢄⣀⣀⣀⣀⣠⠜⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠒⠒⠒⠒⠒⠋⠁⠀⠀")
                elif teacher[i] == '보' and player == '가위':
                    print('teacher: 네가 이겼단다')
                    print("⠀⠀⠀⢀⣀⠀⢰⠒⡄⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡖⠒⢦⠀⠀⣰⠒⢢⠀")
                    print("⠀⠀⠀⢣⠈⡆⢸⠀⡇⢠⠃⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠸⡄⢠⡇⠀⣼⠀")
                    print("⢠⡖⢦⢸⡀⢱⣾⠀⡇⡞⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⢳⡼⠀⢠⡇⠀")
                    print("⠀⢣⡀⢻⡇⠈⠋⠀⠛⠁⣸⢀⠤⢦⠀⠀⠀⠀⢀⣀⡖⠛⣷⠤⠬⣥⣤⣼⠀⠀")
                    print("⠀⠀⢳⡀⠀⠀⠀⠀⣀⡀⠛⠁⣠⠞⠀⠀⠀⠀⣏⠈⢻⡀⠻⣤⣤⠀⠀⠈⢧⠀")
                    print("⠀⠀⠀⢧⠀⠀⠀⠎⠁⠀⠀⡰⠁⠀⠀⠀⠀⠀⠸⣦⠼⠛⠚⠉⡟⠀⠀⠀⣸⠀")
                    print("⠀⠀⠀⠈⢦⣀⣀⣀⣀⣀⠴⠁⠀⠀⠀⠀⠀⠀⠀⠳⣄⣀⢀⣀⡀⢀⣀⠴⠃⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠀⠀⠀⠀")
                round = round + 1
            else:
                continue
        break

    # 미션 07-5 이동 전 독백

    # 미션 07-6 종료
    pLoc = 9
################################### ▲ 미션07 ▲ ####################################
print('마지막부분')