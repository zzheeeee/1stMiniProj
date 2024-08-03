

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
pLoc=5


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

################################## ▼ 미션05 ▼ ###################################
while True:
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
    round = 1
    rise = False
    animalList = ['chicken', 'pig', 'lion', 'chick', 'ox', 'dog', 'cat', 'fox', 'mouse', 'bird', 'bear', 'tiger']
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
    conv(npc, f"야옹~~")
    conv(pName, f"나무에 올라 {npc}를 구하자!")
    pKind -= yesorno()

    # 미션05-2 미션 수행

    while True:
        print()
        sys(f'나무를 오르기 위해 다음 퍼즐에서 동물 단어 5가지를 찾아서 입력하세요.\n한 단어씩 다섯 번 입력하세요.')
        print('┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
        print('┃ t  y  i  s  t  a  n  p  c  t ┃')
        print('┃ d  o  g  a  j  k  f  y  i  i ┃')
        print('┃ v  o  c  a  u  d  n  o  b  g ┃')
        print('┃ q  t  z  h  z  o  c  h  o  e ┃')
        print('┃ e  s  a  e  i  h  a  x  u  r ┃')
        print('┃ f  y  n  l  y  c  b  e  r  d ┃')
        print('┃ o  q  v  r  t  q  k  b  i  x ┃')
        print('┃ x  t  e  m  o  u  s  e  q  e ┃')
        print('┃ j  g  a  p  e  o  b  a  n  c ┃')
        print('┃ m  b  i  r  d  m  n  r  c  a ┃')
        print('┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')

        while True:
            ms51 = input(f'동물 단어 입력 {round}: ')
            if ms51 in animalList:
                print("정답입니다.")
                round +=1
                if round ==6:
                    rise = True
                    break
                else: continue
            else:
                print("오답입니다.")
                continue
        situ("나무를 다 올라왔습니다.")
        situ(f"{npc}가 {pName}을 경계하고 있습니다. {npc}가 다가올 수 있도록 구애의 춤을 추세요.")
        while rise:
            input('>> 미션을 시작하려면 아무 키나 입력하세요.\n')
            lv = 0
            print('=' * 50)
            print('-' * 50)
            print(f'↑: w / ←: a / ↓: s / →: d')
            print(f'별도의 구분없이 연속으로 입력하세요. (예시) ↓ ↑ ↓ → : swsd')
            print('-' * 50)
            while True:
                rise = input(f'\n{riseList[lv]}: ')
                if rise == answerList[lv]:
                    if lv == 0 or lv == 1:
                        situ(f"{npc}가 관심을 보입니다.")
                        lv += 1
                        continue
                    elif lv == 2 or lv == 3:
                        situ(f"{npc}가 조금씩 다가옵니다.")
                        lv += 1
                        continue
                    elif lv == 4:
                        situ("춘식이를 품에 안고 나무를 내려갑니다.")
                        print()
                        conv(pName, f"{npc}를 구했다!")
                        conv(npc, f"야옹♥ (고맙다는 뜻)")
                        break
                else:
                    conv(npc, f"야옹!!!!!!")
            break
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
