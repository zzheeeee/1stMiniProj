# 합 작업 파일 (07/31 15:43 인트로, 미션1, 미션6 완료 버전)
## 합 작업 파일 (07/31 19:30 인트로, 미션1~미션6 완료 버전)
### 합 작업 파일 (08/01 11:50 인트로~미션7 완료 버전, 아웃트로, 맞춤법, 들여쓰기, 대화 관련 등등 미완료 버전)
### 합 작업 파일 (08/01 20:03 인트로~미션7 + 2 문제 추가 완료 버전, 대사 수정, 상황 조절, 간격 조절, 색깔, 삭제, 인트로/아웃트로(졸업장 등등 상황) 미완료 버전)
### 합 작업 파일 (08/02 17:55 인트로~미션7 + 2 문제 추가 완료 버전, 대사 수정, 상황 조절, 간격 조절, 색깔, 삭제, 인트로/아웃트로(졸업장 등등 상황) 완료  터미널 os clear 추가 버전)
#### 최종 ver (08/03)

################################## ▼ 초기값 ▼ ###################################
import random
from datetime import datetime
import os
#미션 번호 0 // 미션 1 ~ 7
Loc = ['교무실', '양호실', '음악실', '매점', '도서실', '운동장 가는 길', '운동장','교무실']
# 이름, 레벨, 인성, 체중, 스킬발동레벨
hee = {'name':'쩡','level':4, 'kind':80, 'weight':0, 'skill':[6,7]}
cha = {'name':'빈','level':4, 'kind':100, 'weight':0, 'skill':[2,5]}
playerList = [hee, cha]
pIdx = 0 #random.randint(0,1)


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
    #print(f"[{speaker}: {ment}]")
    print(f"\x1b[32m[{speaker}: {ment}]\x1b[0m ")

##### situ : 상황 출력
def situ(ment):
    #print('>> '+ment)
    print("\x1b[36m>>  "+ment +"\x1b[0m ")

##### sys : 시스템 출력
def sys(ment):
    #print('>> system: '+ment)
    print("\x1b[36m>> system: "+ment +"\x1b[0m ")

##### yes or no 선택
def yesorno():
    nkind = 0
    while True:
        reply = input(f'\x1b[31m>> 수락하려면 y를, 거절하려면 n을 입력하세요.\n입력 : \x1b[0m')
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
        while True:
            num1 = list(input("1 ~ 9까지 ,를 사용하여 입력하세요 : "))
            if num1 == "" or len(num1) < 5 or len(num1) > 5 or ',' not in num1:
                sys("다시 입력해주세요.")
                continue
            else:
                break
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
            print('-' * 110)
        # 9라운드 전에 정답을 맞힐경우
        elif strike_cnt == 3:
            print()
            conv(name, "정답이야  9라운드 되기전 맞춘 숫자 천재!")
            print()
            print('=' * 110)
            print()
            print()
            break
        else:
            print("strike: ", strike_cnt)
            print("ball: ", ball_cnt)
            print('-' * 110)
        if r + 1 == 9 :
            if strike_cnt != 3 :
                print()
                conv(name,"오이 오이 제대로 머리를 쓰라구 다시 해봐")
                print()
                return mis_baseball("에이스 양현종")
################################## ▲  함수  ▲ ##################################

################################ ▼ 게임 시작 화면 ▼ #################################
# 도트아트 추가하기
print()
print()
print()
print()
print()
print("""
░██████╗ ████████╗ ░█████╗░ ██████╗░ ████████╗
██╔════╝ ╚══██╔══╝ ██╔══██╗ ██╔══██╗ ╚══██╔══╝
╚█████╗░ ░░░██║░░░ ███████║ ██████╔╝ ░░░██║░░░
░╚═══██╗ ░░░██║░░░ ██╔══██║ ██╔══██╗ ░░░██║░░░
██████╔╝ ░░░██║░░░ ██║░░██║ ██║░░██║ ░░░██║░░░
╚═════╝░ ░░░╚═╝░░░ ╚═╝░░╚═╝ ╚═╝░░╚═╝ ░░░╚═╝░░░
""")
input('\x1b[31m>> 시작하려면 아무 키나 입력하세요.\x1b[0m')
os.system('clear')
################################ ▲ 게임 시작 화면 ▲ #################################

################################ ▼ 개발몬 선택 ▼ #################################
print()
print()
print()
print()
print()
print('*'*35+'\x1b[1m개발몬\x1b[0m'+'*'*35)
print("\x1b[1m  선택 1. 쩡 [추리반 부장]  \x1b[0m ")
print("\x1b[1m     - 개발 레벨 : 레벨 4                                      \x1b[0m")
print("\x1b[1m     - 개발 스킬 : 추리 능력 (야구/ 가위바위보 미션 시 스킬사용가능)    \x1b[0m")
print("\x1b[1m     - 인성 : 80                                             \x1b[0m")
print("-"*76)
print("\x1b[1m  선택 2. 빈 [운동부 부장]  \x1b[0m ")
print("\x1b[1m     - 개발 레벨 : 레벨 4                                      \x1b[0m")
print("\x1b[1m     - 개발 스킬 : 운동 능력 (댄스배틀/ 고양이 구출 미션 시 스킬사용가능)\x1b[0m")
print("\x1b[1m     - 인성 : 95                                             \x1b[0m")
print("*"*76)

while True:
    choice = input(">> 게임을 진행할 개발몬의 번호를 입력하세요 : ")
    if int(choice) == 1:
        pName = playerList[0]['name']
        pIdx = 0
        pName = playerList[pIdx]['name']
        pLevel = playerList[pIdx]['level']
        pKind = playerList[pIdx]['kind']
        pWeight = playerList[pIdx]['weight']
        sys('쩡을 선택하셨습니다.')
        print()
        conv(pName, "요로시쿠네~~~><")
        break
    elif int(choice) == 2:
        pName = playerList[1]['name']
        pIdx = 1
        pName = playerList[pIdx]['name']
        pLevel = playerList[pIdx]['level']
        pKind = playerList[pIdx]['kind']
        pWeight = playerList[pIdx]['weight']
        sys('수빈을 선택하셨습니다.')
        print()
        conv(pName, "잘부탁한다구!~~!~!~!~!")
        break
    else: continue
print()
print()
print()
print()
print()
input('\x1b[31m>> 계속하려면 아무 키나 입력하세요.\x1b[0m')
print()
print()
print()
print()
print()
pLoc = 0
################################ ▲ 개발몬 선택 ▲ #################################
################################## ▼ 인트로 ▼ ###################################
while pLoc == 0:
    # 시작 초기 변수 설정
    os.system('clear')
    print("            *   *   *   *   *   *   *   *            \n\n\n\n")
    print("""
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⢿⣿
    ⣿⣿⣿⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⠻⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⠀⠀⠀⢸⣿
    ⣿⣿⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⠀⠀⢹⣿⣿⣿⣿⣿⠀⠀⠀⣶⣶⣶⣶⣶⣶⡆⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⢸⣿⣿⣿⣿⣿⠀⠀⠀⢸⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠙⢿⣿⣿⣿⠀⠀⠀⢸⣿
    ⣿⣿⣿⣿⠛⠛⠛⣿⡟⠛⠛⢻⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⠀⠀⠀⠿⠿⠿⠿⠿⠿⠃⠀⠀⢸⣿⣿⣿⣿⠏⠀⠀⠀⣠⣄⠀⠀⠀⠙⣿⣿⠀⠀⠀⢸⣿
    ⣿⣿⣿⣿⠀⠀⠀⣿⡇⠀⠀⢸⣿⠀⠀⠀⣸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣅⠀⢀⣴⣿⣿⣿⣿⣦⣀⣠⣾⣿⠀⠀⠀⢸⣿
    ⣿⣿⣿⣿⠀⠀⠀⣿⡇⠀⠀⢸⣿⠀⠀⢀⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⡟⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⠻⣿⣿
    ⣿⣿⣿⣿⠀⠀⠀⣿⡇⠀⠀⢸⣿⣶⣶⣾⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⠀⠀⢸⣿
    ⣿⠛⠛⠛⠀⠀⠀⠛⠃⠀⠀⠘⠛⠛⠛⠛⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⢸⣿
    ⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣴⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠉⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡿⠋⠀⢤⣄⣀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⣿⣿⠀⠀⠀⣤⣬⢭⠙⠀⠠⠤⠤⠶⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠲⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢺⠀⠀⠀⠀⠀⠀⠔⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠟⠁⠘⡀⠀⠀⠀⢀⣤⡽⡷⣖⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠈⠍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡄⠀⠀⠈⠛⣛⠲⠖⠃⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡏⠀⠐⠀⠀⢀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣷⣤⣄⡄⠀⢀⣠⡆⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠻⣄⣀⠀⢠⠀⢠⣀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠿⠛⡟⢿⡄⠀⠀⠀⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠈⠀⠈⠁⠀⠃⠀⠀⠀⠛⠛⠛⠁⠀⠀⠀⣸⡧⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾⣀⡤⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣷⣤⣀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⡇⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣇⠄⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡂⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿
    """)
    sys(f"{Loc[pLoc]} 입니다.")
    input("\x1b[31m>> \x1b[0m")
    npc = "주먹왕 마선생님"
    # 인트로-1 상황설명 ########
    # 인트로-2 미션 수행 ########
    print()
    print()
    print()
    conv(pName, "선생님 저 이만 졸업하고 개발일을 하고 싶어요!")
    conv(npc,"졸업하기 위해서는 개발레벨이 10이되어야 하는데...")
    conv(npc, " 너 레벨이 10이니?")
    conv(pName,f"사실대로 말할까??")
    pKind -= yesorno()
    conv(pName, f"{pLevel}... {pLevel} 입니다.")
    if pLevel < 10:
        conv(npc, "졸업하기엔 개발 레벨이 낮구나.")
        conv(npc, "조금 더 공부하고 레벨 10이 되면 찾아오거라.")
    elif pLevel == 10:
        conv(npc, "졸업 축하한다.")
    # 인트로-3 이동 전 독백 ########

    print()
    print()
    print()
    conv(pName, "아 빨리 개발자가 되고 싶었는데...열심히 레벨을 올려보자!")
    input("\x1b[31m>> \x1b[0m")
    print()
    print()
    print()
    sys("교무실에서 나왔습니다.")
    os.system('clear')
    print()
    print()
    print()
    print()
    print()
    conv(pName, "막상 하려니 머리가 아프네에... 양호실에서 두통약을 먹어야 겠어")
    # 인트로 종료
    print()
    print()
    print()
    input("\x1b[31m>> 계속하려면 아무 키나 입력하세요. \x1b[0m")
    print()
    print()
    print()
    pLoc = 1
################################## ▲ 인트로 ▲ ###################################

################################## ▼ 미션01 ▼ ###################################
while pLoc==1:
    # 시작 초기 변수 설정
    os.system('clear')
    print("            *   *   *   *   *   *   *   *            \n\n\n\n")
    print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣄⣀⡀⠀⠀⠀⢻⣷⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠿⠟⠛⠉⠙⠛⠻⢿⣷⣤⡀⠈⢿⣷⣄⠀⠀⠀⠀⠙⢿⣿⣿⠃⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣆⠀⠙⠿⣿⣶⣶⣶⣾⡿⠛⠁⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣾⣿⣿⠙⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠙⢿⣷⣆⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠙⢿⣷⣄⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣆⠀⠀⠀⠀⠙⢿⣷⣄⠀⠀⠀⣸⣿⠁⠀⠀⠀⣠⣾⠿⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠙⢿⣷⣄⣰⣿⠃⠀⠀⣠⣾⡿⠋⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣿⣿⡿⠃⠀⣠⣾⡿⠋⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⢀⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠀⠀⠀⠀⢀⣾⡟⢀⣾⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣇⠘⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣦⡈⠉⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣶⣤⣀⣀⣀⣀⣤⣶⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')
    sys(f"{Loc[pLoc]} 입니다.")
    input("\x1b[31m>> \x1b[0m")
    os.system('clear')
    npc = "종이 인형 황광희"
    # 스킬 발현
    if pLoc in playerList[pIdx]['skill']:
        pSkill = skill_succ  # True if (random.choices((0, 1), choice)) else False
        offset = 1 if pSkill else 0
    else:
        pSkill = False
        offset = 0
    # 계보린 비밀번호 문제 #
    month = random.randint(1, 12)
    pw = ['', 'QZMFZIB', 'UVYIFZIB', 'NZIXS', 'ZKIRO', 'NZB', 'QFMV', 'QFOB', 'ZFTFHG', 'HVKGVNYVI', 'LXGLYVI',
          'MLEVNYVI', 'WVXVNYVI']
    question = pw[month][0:len(pw[month]) - 3].ljust(len(pw[month]), "_")
    answer = pw[month][len(pw[month]) - 3:]
    #print(f"{month}월: {question} 답: {answer} // {pw[month]}")
    err = 0
    pt1 = "★　보안　설정 ★"
    pt2 = "- 폴더 비밀번호 (월마다 교체 필수!!)"
    pt3 = "   8월 : Z F T F H G"
    pt4 = "   9월 : H V K G V N Y V I"
    pt5 = "   10월 : L X G L Y V I"
    pt6 = "   11월 : M L E V N Y V I"
    pt7 = "관리자: 계보린"
    aa = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    dd = f"{pt1:^35}"
    ff = f"{pt2:^35}"
    gg = f"{pt3:^70}"
    hh = f"{pt4:^70}"
    ii = f"{pt5:^70}"
    jj = f"{pt6:^70}"
    zz = f"{pt7:>35}"
    # 증상 리스트, 처방 리스트, 랜덤 인덱스 #
    sickList = ['두통', '감기기운', '소화불량', '근육통', '안구건조증', '실연의 아픔으로 상처난 마음']
    mediList = ['진통제', '감기약', '소화제', '파스', '안약', '후시딘']
    sickIdx = random.randint(0, len(sickList) - 1)
    # 미션 01-1 상황설명 ########
    print()
    print()
    print()
    print()
    print()
    conv(pName, "양호선생님이 안계신다.")
    input("\x1b[31m>> \x1b[0m")
    os.system('clear')
    print()
    print()
    conv(pName, "약품 보관함에 비밀번호를 입력할 수 있는 영어 키패드와 포스트잇이 붙어있다. 가까이 가서 읽어보자.")
    input("\x1b[31m>> \x1b[0m")
    print()
    print()
    print()
    print()
    print(aa + '\n' + dd + '\n' + ff + '\n' + pt3 + '\n' + pt4 + '\n' + pt5 + '\n' + pt6 + '\n' + zz + '\n' + aa)
    print()
    print('* Hint : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')
    print('* Hint : Z Y X W V U T S R Q P O N M L K J I H G F E D C B A')
    print(f'* Hint : ' + question)
    while True:
        upw = input(f'지금은 {month}월입니다. \n비밀번호 입력: ')
        print()
        if upw.upper() == answer:
            print()
            print()
            sys('약품 보관함을 열어 타이레놀을 꺼내 먹었습니다.')
            break
        else:
            sys('오답입니다.')
            continue
    input("\x1b[31m>> \x1b[0m")
    os.system('clear')
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    sys(f"{npc}가 양호실에 들어왔습니다.")
    input("\x1b[31m>> \x1b[0m")
    print()
    print()
    print()
    print()
    print()
    conv(npc, f"{pName}! 여기서 뭐하고 있어?")
    conv(pName, "양호 선생님이 안 계셔서 내가 찾아 먹었어.")
    conv(npc, f"나도 지금 약이 꼭 필요한데.. {pName}아 너가 내 약도 찾아줄래?")
    print()
    pKind - yesorno()
    print()
    print()
    print()
    print()
    os.system('clear')
    # 미션 01-2 미션 수행 ########
    print('=' * 50 + ' 미션 01 ' + '=' * 50)
    while True:
        print()
        print('-'*110)
        print()
        conv(npc, f"나의 증상은 {sickList[sickIdx]}이야.")
        print()
        print(f'* 약품 리스트의 값은 다음과 같습니다. {mediList}')
        ms01 = input('* 증상에 맞는 약의 값을 구할 수 있도록 다음 코드를 완성하세요.\n* <code : mediList[?]> : ')
        print()
        print('-' * 110)
        try:
            if sickIdx == int(ms01):
                print()
                conv(npc, f"나한테 딱 맞는 약이야. {pName}아, 정말 고마워!")
                print()
                print('=' * 110)
                print()
                print()
                sys("레벨이 1 올랐습니다.")
                print()
                print()
                print()
                print()
                print()
                pLevel += 1
                break
            elif sickIdx > int(ms01) or sickIdx < int(ms01):
                print()
                conv(npc, f"음... 이건 나의 증상에 맞지 않은 약인 것 같은데?")
                print()
                continue
        except ValueError:
            print()
            sys("숫자로 입력해주세요.")
            print()
            continue
    # 미션 01-3 이동 전 독백 ########
    input("\x1b[31m>> \x1b[0m")
    os.system('clear')
    print()
    print()
    print()
    print()
    print()
    conv(pName, "이제 다른 곳으로 이동 하자.")
    input("\x1b[31m>> \x1b[0m")
    print()
    print()
    print()
    print()
    print()
    sys("양호실에서 나왔습니다.")
    os.system('clear')
    print()
    print()
    print()
    print()
    print()
    print("♪~~♩~♬")
    print()
    print()
    conv(pName, "웬 음악소리지? 음악실인 것 같은데 가볼까?")
    #미션 01 종료
    print()
    print()
    print()
    print()
    print()
    input("\x1b[31m>> 계속하려면 아무 키나 입력하세요. \x1b[0m")
    print()
    print()
    print()
    print()
    print()
    pLoc = 2
################################## ▲ 미션01 ▲ ###################################

################################## ▼ 미션02 ▼ ###################################
while pLoc == 2:
    # 시작 초기 변수 설정
    os.system('clear')
    print("            *   *   *   *   *   *   *   *            \n\n\n\n")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠤⠔⠂⠒⢢⠀⠀⠀⣀⣠⡤⠤⠤⢤⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠞⠉⠀⠀⠀⠀⠀⠀⣎⡴⠚⠉⣁⣤⡴⢶⡆⢸⠁⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⣠⠴⠋⠁⢀⣤⡾⣝⢶⡹⠃⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⠀⠀⠀⠀⠀⡤⠚⠁⠀⢀⣴⡻⣎⠷⠙⠂⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⢠⠞⠁⢀⣠⢶⠻⠎⠓⣉⡤⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⣠⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠩⠴⣒⠚⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⠰⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠱⣂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⢸⠀⠚⠀⠀⠀⠀⠀⠀⢠⣴⠤⣔⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠘⡆⢀⣄⣀⠀⠀⠀⠀⢿⣿⡷⠘⡠⢒⡡⠄⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠳⣼⣿⣆⠵⣒⣅⠀⡈⠁⠀⠈⠐⠁⠀⠀⠀⠀⠀⠀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⢠⠇⠉⢩⠈⢉⣁⣠⡤⠋⠉⠀⠀⠀⠀⠀⢀⣠⡶⠯⠴⠒⠒⠒⠒⠦⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠐⠺⣢⠄⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣷⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠘⠀⠉⠒⠒⠤⠤⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠒⠒⠒⠦⠃⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⣠⡚⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠲⠤⣄⣀⡀⢀⡤⠤⣀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⢠⠯⠄⣌⠉⠓⠒⠒⠋⢠⠃⡀⠀⠀⣠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⢦⠀⠀⢣⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠸⣅⠀⠀⠀⠀⠀⠀⠀⠘⡆⠈⠙⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⡸⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠈⠑⠒⠦⠦⠤⠦⠴⠖⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡗⠔⠁⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⡀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⠙⠦⣤⣀⣀⣀⣀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⡄⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣆⡀⠀⠀⠀⠉⢉⣵⠻⡄⠀⠀⠀⠀⠀⢀⡰⠁⢮⣷⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠖⠫⠟⠋⠒⠒⠒⠚⠉⠀⡇⠙⠦⠦⠤⡤⠶⠛⢀⢮⡛⠋⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⣀⣀⣀⣀⡠⣤⡴⣶⢿⠀⠀⠀⠀⠀⠳⣀⣒⣵⣟⠇⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠯⣟⠿⠀⠉⠉⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")

    print()
    print()
    sys(f"{Loc[pLoc]} 입니다.")
    input("\x1b[31m>> \x1b[0m")
    os.system('clear')
    npc = "뉴진스 민지"
    # 스킬 발현
    if pLoc in playerList[pIdx]['skill']:
        pSkill = skill_succ  # True if (random.choices((0, 1), choice)) else False
        offset = 1 if pSkill else 0
    else:
        pSkill = False
        offset = 0
    # 정답 리스트 생성 및 저장 / 입력 리스트 생성
    danceList = []
    answerList = []
    for i in range(1, 7):
        answer = ''
        dance = ''
        for j in range(0,(i//2)+3-offset):
            rd = random.randint(0,3)
            if rd == 0:
                dance = dance+'  ↑  '
                answer = answer+'w'
            elif rd == 1:
                dance = dance+'  ←  '
                answer = answer + 'a'
            elif rd == 2:
                dance = dance+'  ↓  '
                answer = answer + 's'
            elif rd == 3:
                dance = dance+'  →  '
                answer = answer + 'd'
        danceList.append(dance)
        answerList.append(answer)
    #미션 02-1 상황설명
    print()
    print()
    print()
    print()
    print()
    conv(pName, f"{npc}가 춤을 추고 있다.")
    conv(npc,"둠칫 둠칫 두둠칫 칫 ♬♩♪")
    input("\x1b[31m>> \x1b[0m")
    print()
    print()
    print()
    print()
    print()
    conv(pName, f"{npc}야 지금 뭐해?")
    conv(npc, f"{pName}! 나 춤 연습 하고 있어. 마침 혼자 춤 추기 외로웠는데 너도 같이 추자! 댄스 배틀 레쓰고~~!")
    print()
    pKind - yesorno()
    print()
    print()
    print()
    print()
    os.system('clear')
    #미션 02-2 미션 수행
    print('=' * 50 + ' 미션 02 ' + '=' * 50)
    while True:
        lv = 0
        print()
        print('-' * 110)
        print()
        conv(npc, f"내 움직임을 따라해봐.")
        print()
        print(f'* ↑ : w / ← : a / ↓ : s / → : d')
        print(f'* 별도의 구분없이 연속으로 입력하세요. (예시) ↓ ↑ ↓ → : swsd')
        print('-' * 110)
        while True:
            dance = input(f'\n{danceList[lv]} : ')
            if dance == answerList[lv]:
                if lv == len(answerList)-1:
                    print()
                    conv(npc, f"춤 좀 추는데?")
                    print()
                    print('=' * 110)
                    print()
                    print()
                    sys("레벨이 1 올랐습니다.")
                    print()
                    print()
                    print()
                    print()
                    print()
                    pLevel += 1
                    break
                else:
                    lv += 1
                    continue
            else:
                print()
                conv(npc, f"이런, 스텝이 꼬였구나. 몸 좀 풀고 다시 도전해봐.")
                print()
        break
    input("\x1b[31m>> \x1b[0m")
    os.system('clear')
    #미션 02-3 이동 전 독백
    print()
    print()
    print()
    print()
    print()
    conv(pName, f"아, 춤을 췄더니 배가 너무 고프네.")
    conv(pName, f"매점에 가볼까?")
    input("\x1b[31m>> \x1b[0m")
    print()
    print()
    print()
    print()
    print()
    sys("음악실에서 나왔습니다.")
    print()
    print()
    print()
    print()
    print()
    #미션 02 종료
    input("\x1b[31m>> 계속하려면 아무 키나 입력하세요. \x1b[0m")
    print()
    print()
    print()
    print()
    print()
    pLoc = 3
################################## ▲ 미션02 ▲ ###################################

################################## ▼ 미션03 ▼ ###################################
while pLoc == 3:
    # 미션 03 시작 초기 변수 설정
    os.system('clear')
    print("            *   *   *   *   *   *   *   *            \n\n\n\n")
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⢶⡶⣶⢶⡶⣶⢶⡶⣶⢶⡶⣶⢶⡶⣶⢶⢶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⣴⡶⢶⡆⣶⡆⢰⡆⣴⡶⢶⡆⣶⠶⢶⣦⠀⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠻⢷⣶⡄⣿⡷⣾⡇⣿⠆⢸⡇⣿⡶⡾⠟⠀⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢾⣦⣼⡇⣿⡇⢸⡇⢿⣧⣼⠇⣿⠀⠀⠀⠀⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡶⣶⢶⣶⢶⡶⢶⡶⣶⠶⣶⢶⡶⣶⢶⣶⡶⣶⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣤⣤⣾⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣼⣿⣤⣤⣤⣤⣤⣤⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣿⣃⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣈⣿⡄⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣾⣏⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣙⣿⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠘⢛⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣻⡟⠃⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢨⣿⠀⣿⠛⠛⠛⠛⠛⠛⠛⣿⠀⣾⡟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿⠀⣽⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠰⣿⠀⢿⣿⠾⠷⠿⠾⠷⢿⡿⠀⠿⣷⡿⠾⠷⠿⠾⠷⠿⠾⠷⠿⠾⠷⠿⠾⣷⠿⠀⢾⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢘⣿⠀⢸⡷⠀⠀⠀⠀⠀⢸⡇⠀⠀⢾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣻⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢨⣿⠀⢸⣟⠀⠀⠀⣤⡄⢸⡇⠀⠀⣻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣽⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠰⣿⠀⢸⣯⠀⠀⠀⠀⠀⢸⡇⠀⣿⡟⠻⠛⠟⠻⠛⠟⠻⠛⠟⠻⠛⠟⠻⠛⠟⣿⠀⢾⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢘⣿⠀⢸⡷⠀⠀⠀⠀⠀⢸⡇⠀⠿⠷⠶⠷⠾⠶⠷⠾⠶⠷⠾⠶⠷⠾⠶⠷⠾⠿⠀⣻⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢠⣾⣿⣶⣾⣿⣶⣶⣶⣶⣶⣾⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⢿⣷⡄⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢸⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣼⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⠀⠁⠈⠀⠁⠈⠀⠁⠈⠀⠁⠈⠀⠁⠈⠀⠁⠈⠀⠁⠈⠀⠁⠈⠀⠁⠈⠀⠁⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀
    """)
    print()
    print()
    sys(f"{Loc[pLoc]} 입니다.")
    input("\x1b[31m>> \x1b[0m")
    os.system('clear')
    npc = "혜자로우신 매점 아주머니"
    # 스킬발현
    if pLoc in playerList[pIdx]['skill']:
        pSkill = skill_succ  # True if (random.choices((0, 1), choice)) else False
        offset = 1 if pSkill else 0
    else:
        pSkill = False
        offset = 0
    # 미션 03-1 상황설명
    res_num = []
    que_num = []
    num_lst = [" → → → ↓ ↓ ↓ ↓ ← ← ↑ ↑ ↑ ", "↓ ↓", " → → → ↓ ↓ ← ← ↓ ↓ → → ", " → ↓ ← → ↓ ← ", " ↓ → ↑ ↓ ", " ← ← ← ↓ ↓ → → ↓ ↓ ← ← ", " ← ← ← ↓ ↓ → → ↓ ↓ ← ← ↑ ",
               " ↑ ↑ → → ↓ ↓ ↓ ↓ ↓ ", "↑ ↑ → → ↓ ↓ ↓ ↓ ↓ ← ← ↑ ↑ → → ", " ↑ ↑ ↑ ← ← ↑ ↑ → → ↓ ↓ "]
    print()
    print()
    print()
    print()
    conv(pName,"문에 포스트잇이 붙어있다.")
    str1 = '공지'
    str2 = '이 문제를 풀고 이 곳에 들어올 수 있는 자만이'
    str3 = '매점을 이용할 자격이 주어집니다.'
    str4 = ''
    str5 = ' 김 혜 자 백'
    str6 = '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'
    #### 포스트잇
    print()
    print("⠀⠀⣶⣶⠀⠀⠀⢰⣶⣶⣶⣶⡆⠀⢰⣶⣶⣶⣶⣶　　　　", "{0:　^40}".format(str6))
    print("⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣿⣿　　　　", "{0:　^31}".format(str1))
    print("⠀⠀⣿⣿⠀⠀⠀⢸⣿⠿⠿⠿⠇⠀⠸⠿⠿⠿⣿⣿　　　　", "{0:　^31}".format(str4))
    print("⠀⠀⣿⣿⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿　　　　", "{0:　^31}".format(str2))
    print("⠀⠀⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿　　　　", "{0:　^31}".format(str3))
    print("　　　　　　　　　　　　　　　　　　　 ", "{0:　>31}".format(str4))
    print("⣿⣿⠀⠀⣿⡇⠀⢸⣿⠿⠿⠿⠇⠀⢸⣿⠿⠿⠿⠿　　　　", "{0:　^40}".format(str5))
    print("⣿⣿⣤⣤⣿⡇⠀⢸⣿⣤⣤⣤⡄⠀⢸⣿⣤⣤⣤⣤　　　　", "{0:　^40}".format(str6))
    print("⠛⠛⠛⠛⣿⡇⠀⠘⠛⠛⠛⣿⡇⠀⢸⣿⠛⠛⢿⣿")
    print("⠀⠀⠀⠀⣿⡇⠀⢠⣤⣤⣤⣿⡇⠀⢸⣿⣤⣤⣼⣿")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⢸⣿⠛⠛⢸⣿⠀⣿⣿⠛⠛⣿⣿⠀⣿⣿⠛⠛⣿⣿")
    print("⢸⣿⠀⠀⢸⣿⠀⣿⣿⣤⣤⣿⣿⠀⣿⣿⣤⣤⣿⣿")
    print("⠀⠀⠀⠀⢸⣿⠀⣿⣿⠉⠉⣿⣿⠀⠀⠀⠀⠀⣿⣿")
    print("⠀⠀⠀⠀⢸⣿⠀⣿⣿⣶⣶⣿⣿⠀⠀⠀⠀⠀⣿⣿")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⢰⣶⣶⣶⣶⡆⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀")
    print()
    print()
    print()

    while True:
        for i in range(0, 3):
            res_num.append(random.randint(0, 9))
            if res_num[i] == 3 or res_num[i] == 4 or res_num[i] == 1:
                res_num[i] = 0
                que_num.append(num_lst[res_num[i]])
            else:
                que_num.append(num_lst[res_num[i]])

        #### 문제list , 정답list 출력
        print(que_num)
        ### 사용자 입력값 받기
        while True:
            num1 = list(input("* 1 ~ 9까지 ,를 사용하여 입력하세요 :"))
            if len(num1) == 5:
                try:
                    break
                except IndexError:
                     continue
            print("* 다시 입력해 주세요.")

        ### 입력값 리스트 int형으로 변환 변수
        answer = [num1[0],num1[2],num1[4]]
        # 문자가 원소인 리스트를 int형 리스트로 형 변환하기
        answer = list(map(int, answer))

        if res_num == answer:
            #### 대사
            print()
            conv(pName, "먹을 자격을 얻었다~!!!")
            print()
            break
        else:
            print()
            conv(pName, "꼭 풀고 말테야 포기 하지 말자")
            print()
            continue
    print()
    print()
    print()
    print()
    print()
    input("\x1b[31m>> \x1b[0m")
    os.system('clear')
    print()
    print()
    print()
    print()
    print()
    conv(pName, "사장님 크림빵이랑 딸기우유 주세요")
    conv(npc, "잠깐 기다려 주겠니? 빵 정리를 못 끝내서 ")
    print()
    print()
    print()
    conv(pName, f"{npc}가 곤란하신 상황인거 같다. 정리를 도와드릴까?")
    print()
    pKind - yesorno()
    print()
    print()
    print()
    print()
    os.system('clear')
    # 미션 03-2 미션 수행
    print('=' * 50 + ' 미션 03 ' + '=' * 50)
    print()
    print('-' * 110)
    print()
    conv(npc, "빵이 왜 칸에 맞게 안들어가는거지?? ")
    print()
    print("* 매점 아주머니에게 질문할 말로 옳은 것을 고르세요.")
    while True:
        que = input(" (1) 선반에 들어갈 빵이 총 몇개 인가요? \n (2) 백종원님을 불러올까요? \n (3) 빵이 총 얼마인가요?\n\n입력 : ")
        print()
        print('-' * 110)
        if int(que) == 1:
            print()
            conv(npc, "16개란다.")
            conv(pName, "흠... 선반 칸과 맞지 않은걸 선반 칸을 늘려 드려야겠다.")
            print()
            break
        elif int(que) != 1:
            print()
            conv(npc, "질문을 다시 해주겠니?")
            print()
            continue
        elif not (str(que).isnumeric()) or not (0 < int(que) <= 4):
            print()
            sys("잘못 입력 되었습니다. 다시 입력해주세요.")
            print()
            continue
    while True:
        print('-' * 110)
        print()
        print("* 빵을 알맞게 넣기 위한 선반 범위가 알맞은 것을 고르세요.")
        print('** Hint: 매점 선반은 15칸 입니다.')
        que = input(" (1) range(1,15,1)\n (2) range(0,15,1)\n (3) range(14,0,-1)\n (4) range(0,16,1)\n\n입력 : ")
        print()
        print('-' * 110)
        if int(que) == 4:
            print()
            conv(npc, f"{pName}이는 리스트 범위를 잘 이해하고 있구나. 똑똑한 개발몬이 되겠어~")
            print()
            print('=' * 110)
            print()
            print()
            sys("레벨이 1 올랐습니다.")
            print()
            print()
            print()
            print()
            print()
            pLevel += 1
            break
        elif not (str(que).isnumeric()) or not (0 < int(que) <= 4):
            print()
            sys("잘못 입력 되었습니다. 다시 입력해주세요.")
            print()
            continue
        else:
            print()
            conv(npc, f"{pName}이는 리스트 범위를 이해하지 못했지만 다시 한번 맞춰보렴")
            print()
            continue
    # 미션 03-3 이동 전 독백
    input("\x1b[31m>> \x1b[0m")
    os.system('clear')
    print()
    print()
    print()
    print()
    print()
    conv(pName, "이제 다른 곳으로 이동 하자.")
    input("\x1b[31m>> \x1b[0m")
    print()
    print()
    print()
    print()
    print()
    sys("매점에서 나왔습니다.")
    os.system('clear')
    print()
    print()
    print()
    print()
    print()
    conv(pName, "이제 배를 채웠으니 마음의 양식을 쌓으러 가볼까?")
    # 미션 03 종료
    print()
    print()
    print()
    print()
    print()
    input("\x1b[31m>> 계속하려면 아무 키나 입력하세요. \x1b[0m")
    print()
    print()
    print()
    print()
    print()
    pLoc = 4
################################## ▲ 미션03 ▲ ###################################

################################## ▼ 미션04 ▼ ###################################
while pLoc == 4:
    # 시작 초기 변수 설정
    os.system('clear')
    print("            *   *   *   *   *   *   *   *            \n\n\n\n")
    print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠈⠉⠙⠛⠿⢿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⠿⠛⠛⠉⠉⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣶⣄⢀⣴⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣿⣿⣿⠛⠛⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡟⠛⠛⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣿⣿⣿⠀⠀⢸⣿⣿⡇⠀⠀⠀⣾⣿⣷⣶⣤⣀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⢀⣠⣴⣶⣿⣿⡆⠀⠀⢸⣿⣿⡇⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣿⣿⣿⠀⠀⢸⣿⣿⡇⠀⠀⠀⠙⠛⠻⢿⣿⣿⣷⠀⠀⢸⣿⣿⡇⠀⠀⢰⣿⣿⣿⠿⠛⠛⠁⠀⠀⢸⣿⣿⡇⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣿⣿⣿⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⢸⣿⣿⡇⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣿⣿⣿⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣿⣿⣿⠀⠀⢸⣿⣿⡇⠀⠀⠀⣾⣿⣷⣶⣤⣀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⢀⣠⣴⣶⣿⣿⡆⠀⠀⢸⣿⣿⡇⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣿⣿⣿⠀⠀⢸⣿⣿⡇⠀⠀⠀⠉⠛⠿⢿⣿⣿⣷⠀⠀⢸⣿⣿⡇⠀⠀⢰⣿⣿⣿⠿⠛⠋⠁⠀⠀⢸⣿⣿⡇⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣿⣿⣿⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⢸⣿⣿⡇⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣿⣿⣿⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣿⣿⣿⠀⠀⠸⣿⣿⣿⣷⣶⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣾⣿⣿⣿⡇⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠉⠛⠛⠻⠿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⡿⠿⠛⠛⠋⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣿⣿⣿⣀⣀⣀⣀⡀⠀⠀⠀⠀⠉⠙⠻⢿⣿⣿⣷⣤⡀⢸⣿⣿⡇⠀⣠⣶⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⣀⣀⣀⣀⣸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣤⣭⣿⣿⣿⣿⣾⣿⣿⣷⣾⣿⣿⣿⣯⣤⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠛⠛⠛⠛⠛⠛⠻⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠛⠛⠛⠛⠛⠛⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠿⢿⣿⠿⠟⠋⠉⠁⠀⠀⠀⠀⠀
    ''')
    print()
    print()
    sys(f"{Loc[pLoc]} 입니다.")
    input("\x1b[31m>> \x1b[0m")
    os.system('clear')
    npc = "얼굴 천재 차은우"
    # 스킬발현
    if pLoc in playerList[pIdx]['skill']:
        pSkill = skill_succ  # True if (random.choices((0, 1), choice)) else False
        offset = 1 if pSkill else 0
    else:
        pSkill = False
        offset = 0
    # 미션 04만의 변수 설정
    date=["07-31","07-15","07-02","06-27","06-11","05-31"]
    name = ["뉴진스 혜린","아이브 유진","르세라핌 채원","에스파 닝닝","아이브 원영","르세라핌 윤진"]
    book=["엑셀X파이썬","혼자공부하는 머신러닝+딥러닝","오렌지3 with 파이썬","비전공자를 위한 이해할 수 있는 파이썬","파이썬 머신러닝 판다스 데이터 분석","파이썬 코딩의 기술"]
    born_book = ["길벗","한빛미디어","생능북스","티더블유아이지","정보문화사","길벗"]
    write=["정성일","박해선","김현철","최원영","오승환","데이비드 메르츠"]
    num = random.randint(0, 4)
    st = book[num].replace(book[num], "//////////")
    book[num] = st
    # 미션04-1 상황설명
    print()
    print()
    print()
    print()
    print()
    conv(pName, f"{npc}가 곤란해 하고 있다. 당장 도와주자.")
    input("\x1b[31m>> \x1b[0m")
    print()
    print()
    print()
    print()
    print()
    conv(pName, f"{npc}! 무슨 일 있어?")
    conv(npc, f"{pName}아 {name[num]}이가 빌린 책을 나도 보고 싶은데 대출 목록 종이가 찢어져 있어서 못 찾겠어 찾는 걸 도와줄래?")
    print()
    pKind -= yesorno()
    print()
    print()
    print()
    print()
    os.system('clear')
    # 미션 04-2 미션 수행
    print('=' * 50 + ' 미션 04 ' + '=' * 50)
    print("* 대출 목록")
    for i in range(0,6):
        book_lst = [date[i],name[i],book[i],born_book[i],write[i]]
        print(book_lst)
    print()
    print('-' * 110)
    print()
    conv(npc, f"{name[num]}이가 빌린 책을 찾으려면 인덱스 몇을 입력하면 보여줄까?")
    print()
    ### 숫자만 입력하기 (입력값 오류처리)
    while True:
        try:
            res_book = int(input("* 입력 : "))
            if res_book == num:
                print()
                conv(npc, f"{pName}이 덕분에 {name[num]}이가 빌린 책을 알게됐어~\n{pName}아 너무 고마워")
                print()
                print('=' * 110)
                print()
                print()
                sys("레벨이 1 올랐습니다.")
                print()
                print()
                print()
                print()
                print()
                pLevel += 1
                break
            else:
                print()
                conv(npc, f"이건 {name[num]}이가 빌린 책이 아닌 것 같아.")
                print()
                continue
        ### ValueError 발생하면 수행
        except ValueError:
            print()
            sys("입력값이 숫자가 아닙니다.")
            print()
            continue
    # 미션 04-3 이동 전 독백
    input("\x1b[31m>> \x1b[0m")
    os.system('clear')
    print()
    print()
    print()
    print()
    print()
    conv(pName, "아까 먹은 빵이 소화가 안되네. 운동장 한바퀴 걷고 올까?")
    pWeight -= yesorno()
    print()
    print()
    print()
    print()
    print()
    sys(f"{Loc[pLoc]}에서 나왔습니다.")
    os.system('clear')
    print()
    print()
    print()
    print()
    print()
    print("야옹~~~~~야아아아아아오오오오오오오오오옹~~~~~")
    print()
    print()
    conv(pName, "이게 무슨 소리지??? 소리가 나는 곳을 찾아보자.")
    input("\x1b[31m>> \x1b[0m")
    print()
    print()
    print()
    print()
    print()
    print()
    sys("나무위에 춘식이를 발견했습니다.")
    # 미션04 종료
    print()
    print()
    print()
    print()
    print()
    input("\x1b[31m>> 계속하려면 아무 키나 입력하세요. \x1b[0m")
    print()
    print()
    print()
    print()
    print()
    pLoc = 5
################################## ▲ 미션04 ▲ ##################################

################################## ▼ 미션05 ▼ ###################################
while pLoc == 5:
    # 시작 초기 변수 설정
    os.system('clear')
    print("            *   *   *   *   *   *   *   *            \n\n\n\n")
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⣠⡶⠟⠛⠛⠶⠾⠛⠛⠛⠉⠉⠉⠛⠛⠻⠶⣶⠶⠟⠿⠶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣠⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣶⣶⣶⣤⣤⣀⠀⠀⢀⣴⣾⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀
    ⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀
    ⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀
    ⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⠿⠁⠀⠀⠀⠀⠀⠀⢿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀
    ⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⣦⣤⠶⠟⠛⠳⠶⢦⣄⣠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀
    ⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⠀⠀⠀⠀⠀⠀⢻⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀
    ⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠐⠛⠋⠻⢦⣤⡶⣦⣤⣴⠟⠻⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠘⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠈⠻⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠙⠷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⠟⠉⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡛⠛⠶⠶⢶⣦⣤⣤⣤⣤⠶⠶⠶⠞⠛⠉⠁⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠶⢶⣤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣾⣿⣿⣿⣿⣿⡿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')
    print()
    print()

    sys(f"{Loc[pLoc]} 입니다.")
    input("\x1b[31m>> \x1b[0m")
    os.system('clear')
    npc = "귀여운 춘식이"
    # 스킬 발현
    if pLoc in playerList[pIdx]['skill']:
        pSkill = skill_succ  # True if (random.choices((0, 1), choice)) else False
        offset = 1 if pSkill else 0
    else:
        pSkill = False
        offset = 0
    # 미션 05만의 변수 설정
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
                rise = rise + '  ↑  '
                answer = answer + 'w'
            elif rd == 1:
                rise = rise + '  ←  '
                answer = answer + 'a'
            elif rd == 2:
                rise = rise + '  ↓  '
                answer = answer + 's'
            elif rd == 3:
                rise = rise + '  →  '
                answer = answer + 'd'
        riseList.append(rise)
        answerList.append(answer)
    # 미션 05-1 상황설명
    print()
    print()
    print()
    print(f"야옹~~")
    conv(pName, f"어서 나무 위로 올라가 {npc}를 구하자!")
    pKind -= yesorno()
    print()
    print()
    print()
    print()
    print()
    os.system('clear')
    # 미션 05-2 미션 수행
    print('=' * 50 + ' 미션 05 ' + '=' * 50)
    while True:
        print()
        print('-' * 110)
        print()
        print(f'나무를 오르기 위해 다음 퍼즐에서 동물 단어 5가지를 찾아서 입력하세요.\n한 단어씩 다섯 번 입력하세요.')
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
            print()
            ms51 = input(f'동물 단어 입력 {round}: ')
            if ms51 in animalList:
                print("정답입니다.")
                print()
                round +=1
                if round ==6:
                    break
                else: continue
            else:
                print("오답입니다.")
                continue
        sys("나무를 다 올라왔습니다.")
        print()
        print()
        rise = True
        while rise:
            input("\x1b[31m>> 다음 미션을 시작하려면 아무 키나 입력하세요.\n>> \x1b[0m")
            os.system('clear')
            lv = 0
            print()
            print('-' * 110)
            print()
            print(f"* {npc}가 {pName}을 경계하고 있습니다. {npc}가 다가올 수 있도록 구애의 춤을 춰야합니다.")
            print(f'* ↑: w / ←: a / ↓: s / →: d')
            print(f'* 별도의 구분없이 연속으로 입력하세요. (예시) ↓ ↑ ↓ → : swsd')
            print()
            print('-' * 110)
            print()
            while True:
                rise = input(f'\n{riseList[lv]}: ')
                if rise == answerList[lv]:
                    if lv == 0 or lv == 1:
                        sys(f"{npc}가 관심을 보입니다.")
                        lv += 1
                        continue
                    elif lv == 2 or lv == 3:
                        sys(f"{npc}가 조금씩 다가옵니다.")
                        lv += 1
                        continue
                    elif lv == 4:
                        print()
                        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡖⠉⠑⠒⠋⠉⠉⠉⠉⠒⠒⠒⠒⢦⠀⠀⠀⠀")
                        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢇⠀⠀⠀")
                        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀")
                        print("⠀⠀⠀⠀⠀⢀⣀⡀⢀⡇⠀⠀⠀⠀⢠⣤⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⣇⠀")
                        print("⠀⠀⠀⠀⣠⠏⠀⢧⣸⠀⠀⠀⠀⠀⢠⣡⠤⠶⠤⣄⣈⡁⠀⠀⠀⠀⠀⠀⢹⠀")
                        print("⠀⠀⠀⡞⠀⠀⢲⠀⢹⡀⠀⠀⠀⠀⠤⢇⣀⣀⣀⣨⣏⠀⠀⠀⠀⠀⠀⠀⡾⠀")
                        print("⠀⠀⠀⣇⠀⠀⣸⠀⠘⣇⠀⠀⠀⠀⠀⠀⠘⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀")
                        print("⠀⠀⠀⠈⠉⠻⢅⡀⠀⣘⣦⣀⠀⠀⠀⠀⠘⠒⠂⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀")
                        print("⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿⣿⣿⣿⣷⣶⣄⣀⡀⠀⠀⣀⣀⣀⡤⠴⠚⣅⠀⠀⠀")
                        print("⠀⢀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡉⠉⠉⠉⠉⠀⠀⠀⠀⠘⡆⠀⠀")
                        print("⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⢀⡴⠆⠀⠀⠀⠀⣷⠀⠀")
                        print("⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⡏⠀⠀⠀⠀⠀⢠⠇⠀⠀")
                        print("⠀⠀⠈⠉⠙⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠤⠷⢤⣤⡤⠴⠞⠁⠀⠀⠀")
                        print("⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠋⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        conv(npc, f"야옹♥ (고맙다는 뜻)")
                        print()
                        print('=' * 110)
                        print()
                        print()
                        sys("레벨이 1 올랐습니다.")
                        print()
                        print()
                        print()
                        print()
                        print()
                        pLevel += 1
                        break
                else:
                    print()
                    conv(npc, f"야옹!!!!!!")
                    print()
            break
        break

    # 미션 05-3 이동 전 독백
    os.system('clear')
    print()
    print()
    print()
    print()
    print()
    conv(pName, f"춘식이는 땅에 내려놓자마자 어디론가 도망가버렸다.")
    conv(pName, f"운동장으로 계속 가볼까?")
    input("\x1b[31m>> \x1b[0m")
    print()
    print()
    print()
    print()
    print()
    # 미션 05 종료
    pLoc = 6
################################### ▲ 미션05 ▲ ###################################

################################### ▼ 미션06 ▼ ###################################
while pLoc == 6:
    # 시작 초기 변수 설정
    os.system('clear')
    print("            *   *   *   *   *   *   *   *            \n\n\n\n")
    print('''

    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⡿⠿⣿⡿⢿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⠿⠟⠻⠿⣷⣦⡀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢰⣿⠏⣠⣾⠟⠀⠀⠹⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠈⢿⣷⠀
    ⠀⠀⠀⠀⠀⠀⠀⢺⣿⡾⠛⠁⠀⣠⣶⠿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀
    ⠀⠀⠀⠀⠀⠀⠀⠘⣿⣧⡀⠀⣼⠟⢁⣼⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡟⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⠏⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡿⠁⠀⠀⠀⠀⠀⠀⣠⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠟⠀⠀⠀⠀⠀⢀⣴⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠋⠀⠀⠀⢀⣠⣾⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡟⠁⠀⠀⣠⣴⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⠋⠀⢀⣴⣾⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⢀⣾⡿⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢀⣀⣀⣴⣿⠟⠁⢀⣴⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢰⣿⠿⢿⣿⣅⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠸⣿⣦⡀⠙⢿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠈⠻⣿⣦⣴⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠈⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

    ''')
    print()
    print()

    sys(f"{Loc[pLoc]} 입니다.")
    input("\x1b[31m>> \x1b[0m")
    os.system('clear')
    npc = "에이스 양현종"
    # 스킬 발현
    if pLoc in playerList[pIdx]['skill']:
        pSkill = skill_succ  # True if (random.choices((0, 1), choice)) else False
    else:
        pSkill = False
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
    # 미션06-1 상황설명
    print()
    print()
    print()
    print()
    conv(pName, f"운동장 한 가운데서 {npc}이가 캐치볼을 하고 있다.")
    input("\x1b[31m>> \x1b[0m")
    print()
    print()
    print()
    print()
    print()
    conv(npc, f"{pName}! 여기서 뭐하고 있어?")
    conv(pName, "소화 시킬 겸 산책하려고")
    conv(npc, f"소화 시킬 겸 머리쓰는 야구 게임은 어때?")
    conv(pName,"좋아 문제 드루와!!!")
    print()
    pKind -= yesorno()
    print()
    print()
    print()
    print()
    os.system('clear')
    #미션 06-2 미션 수행
    print('=' * 50 + ' 미션 06 ' + '=' * 50)
    print()
    conv(npc, f"3자리 숫자를 맞춰봐. 범위는 1에서 9까지야.")  # 현종이대사
    if pSkill:
        print("* Hint : 첫번째 자리 숫자 >>", num_lst[0])
    #미션 06 수행 함수 선언
    mis_baseball(npc)
    print()
    print()
    pLevel += 1
    conv(npc,"너 야구부에 들어 오지 않을래?")
    conv(pName, "아니 나는 졸업해서 개발자가 될꺼야")
    conv(npc, "너도 개발 에이스가 되길 바랄게")
    conv(pName, "너는 우리나라 최고의 야구선구가 되어줘")
    print()
    print()
    input("\x1b[31m>> 계속하려면 아무 키나 입력하세요. \x1b[0m")
    os.system('clear')
    #미션06 이동 전 독백
    print()
    print()
    print()
    print()
    sys("레벨이 1 올랐습니다.")
    print()
    print()
    print("██╗░░░░░ ██╗░░░██╗ ░░███╗░░ ░█████╗░ ██╗")
    print("██║░░░░░ ██║░░░██║ ░████║░░ ██╔══██╗ ██║")
    print("██║░░░░░ ╚██╗░██╔╝ ██╔██║░░ ██║░░██║ ██║")
    print("██║░░░░░ ░╚████╔╝░ ╚═╝██║░░ ██║░░██║ ╚═╝")
    print("███████╗ ░░╚██╔╝░░ ███████╗ ╚█████╔╝ ██╗")
    print("╚══════╝ ░░░╚═╝░░░ ╚══════╝ ░╚════╝░ ╚═╝")
    print()
    print()
    print()
    print()
    print()
    conv(pName, "개발레벨이 10이 된거 같은데 교무실로 이동하자")
    input("\x1b[31m>> 계속하려면 아무 키나 입력하세요. \x1b[0m")
    print()
    print()
    print()
    print()
    print()
    #미션 06 종료
    pLoc = 7
################################### ▲ 미션06 ▲ ###################################

################################### ▼ 미션07 ▼ ###################################
while pLoc ==7:
    # 시작 초기 변수 설정
    os.system('clear')
    print("            *   *   *   *   *   *   *   *            \n\n\n\n")
    print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⢀⣀⣀⡀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⠗⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣟⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⠟⠂⠀⠴⠛⠛⠛⠛⠿⠷⠂⠀⠀⠀⢀⣤⣤⣴⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠈⠉⠛⠋⢻⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠴⠛⠛⠻⢿⡿⠀⠀⠀⠀⢠⣶⣷⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⢿⣿⣿⡀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡀⠀⠀⠀⠛⠿⠿⢷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⢁⡀⠀⠀⠀⠀⠀⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠐⠛⢀⣀⡀⠀⢀⣀⡙⠦⠀⠀⠀⢀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠉⠉⡟⢻⣿⣇⠀⠀⠀⢀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣗⠀⠀⠀⠀⠀⠀⠀⣤⣄⠀⠒⠂⠀⠲⢿⣿⡗⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠻⠿⠿⣿⡿⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣆⣤⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⡀⣀⣀⣼⣿⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⣀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠒⠦⠀⠀⠘⠿⢿⣿⣿⣿⣿⡇⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

    ''')
    sys(f"{Loc[pLoc]} 입니다.")
    input("\x1b[31m>> \x1b[0m")
    os.system('clear')
    npc = "주먹왕 마선생님"
    win = 0
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
    #print(teacher)

    # 미션 07-2 상황설명
    os.system('clear')
    print()
    print()
    print()
    print()
    print()
    conv(pName, "선생님 저 레벨이 10이 되었어요. 이제 졸업할 수 있는거죠??")
    conv(npc,"정말 10이 되었다니 기특하구나. 하지만 아직 마지막 관문이 남아있어")
    conv(pName, "에에~?? 마지막 관문이 뭔데요??")
    conv(npc, "내가 왜 주먹왕 인지 아니?? 가위 바위 보를 잘하기 때문이야 나를 이겨 봐!!")
    print()
    print()
    print()
    print()
    print()
    input("\x1b[31m>> 계속하려면 아무 키나 입력하세요. \x1b[0m")
    print()
    print()
    print()
    print()
    print()
    os.system('clear')
    # 미션 07-3 미션 수행

    # 미션 07-4 수행 함수 선언
    round = 1

    while True:
        while round <= 3:
            print()
            if round == 1 and pSkill:
                print('* 스킬이 발동되어 첫 판에는 선생님이 무엇을 낼 지 알 수 있습니다.')
                print(f'* Hint : {teacher[0]}, ?, ?')
            player = input(f"[Round {round}] 가위, 바위, 보 중 하나를 입력하세요 : ")
            #print(player)
            if player == '가위' or player == '바위' or player == '보':
                i = round - 1
                print()
                #print(teacher[i], player)
                if teacher[i] == '가위' and player == '가위':
                    #print('teacher: 비김')
                    result = "Draw"
                    print(f"\x1b[44m {result.center(38, ' ')} \x1b[0m ")
                    print("   ⠀⠀⠀⡴⠒⢦⠀⠀⢰⠒⢲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠠⡞⠉⢦⠀⠀⡴⠋⢳⠀")
                    print("   ⠀⠀⠀⢻⠀⠘⡆⢀⡏⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠘⡆⢰⠇⠀⡾⠀")
                    print("   ⠀⠀⠀⠘⡇⠀⢹⣼⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⡆⠀⢻⡞⠀⢰⠇⠀")
                    print("   ⢀⣀⣴⠋⢻⡦⠤⠧⣤⣼⡇⠀⠀⠀⠀⠀⠀⠀⣀⣤⣞⠉⣻⠶⠶⠶⠤⣾⡀⠀")
                    print("   ⢿⠀⠹⣆⠘⣦⣤⡄⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⢧⠀⢹⣄⠙⣶⣦⠀⠀⠀⢳⠀")
                    print("   ⠘⣧⠴⠟⠛⠉⡟⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠸⣷⠞⠋⠉⠁⠏⠀⠀⠀⡼⠀")
                    print("   ⠀⠙⢦⣀⣀⣀⣀⣀⣀⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣄⣀⣀⣀⣀⡤⠞⠁⠀")
                elif teacher[i] == '가위' and player == '보':
                    #print('teacher: 내가 이겼단다')
                    result = "You Lose"
                    print(f"\x1b[44m {result.center(38, ' ')} \x1b[0m ")
                    print("   ⠀⠀⠀⢀⣀⡀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀")
                    print("   ⠀⠀⠀⢯⠀⢹⡄⠀⣼⠁⢸⡇⠀⠀⠀⠀⠀⠀⢠⡚⢢⠀⡇⢸⠀⢰⠛⡆⠀⠀")
                    print("   ⠀⠀⠀⠸⡄⠀⢧⢠⠇⠀⣼⠀⠀⠀⠀⠀⢀⣀⠀⡇⠘⡄⡇⢸⠀⡇⢰⠁⠀⠀")
                    print("   ⠀⠀⢀⣤⣷⠀⠘⡟⠀⢀⡇⠀⠀⠀⠀⠀⠸⡀⢣⣿⠀⢷⠇⠸⡿⠀⡎⠀⣀⡀")
                    print("   ⣰⠒⢿⡀⢸⡋⠉⠙⠛⠻⣇⠀⠀⠀⠀⠀⠀⠱⡀⠙⠀⠀⠀⠀⠀⢰⡷⠊⢁⡇")
                    print("   ⢹⡄⠈⣷⣤⡿⣻⠃⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⢀⠔⠋⠀⠀⡰⠋⠀")
                    print("   ⠀⢿⡉⠁⠀⠀⠋⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠈⠀⠀⠀⡰⠁⠀⠀")
                    print("   ⠀⠀⠙⠲⠶⠖⠶⠶⠒⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠒⠒⠒⠊⠀⠀⠀⠀")

                elif teacher[i] == '가위' and player == '바위':
                    win = win + 1
                    #print('teacher: 네가 이겼단다')
                    result = "You Win"
                    print(f"\x1b[44m {result.center(38, ' ')} \x1b[0m ")
                    print("   ⠀⠀⠀⣴⠒⢦⠀⠀⢠⠖⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⣀⡀⠀⠀")
                    print("   ⠀⠀⠀⢹⡀⠘⡇⠀⡞⠀⢸⠃⠀⠀⠀⠀⠀⢀⡴⠦⡞⠉⢹⡇⠀⣿⠁⢹⡆⠀")
                    print("   ⠀⠀⠀⠈⣇⠀⢹⣸⠃⠀⡾⠀⠀⠀⠀⠀⠀⢸⠀⠀⡇⠀⢸⡇⢀⣿⡀⢸⣧⠀")
                    print("   ⠀⣀⣰⠚⢻⣤⣤⣯⣤⣰⡇⠀⠀⠀⠀⠀⠀⠸⣦⡤⠿⢶⡟⠉⠉⠉⠉⠙⠻⡇")
                    print("   ⢾⠉⠹⣆⠘⣦⣤⡀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠙⢲⡶⠀⠀⠀⢸⠃")
                    print("   ⠈⣧⡤⠟⠒⠋⣾⠀⠀⠀⢨⠇⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⠈⠁⠀⠀⣠⠏⠀")
                    print("   ⠀⠘⢦⣀⠀⠀⠀⠀⣀⡠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠒⠒⠒⠒⠒⠋⠁⠀⠀")
                    print("   ⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                elif teacher[i] == '바위' and player == '바위':
                    # print('teacher: 비김')
                    result = "Draw"
                    print(f"\x1b[44m {result.center(38, ' ')} \x1b[0m ")
                    print("   ⠀⣀⣀⡤⠶⣴⠚⠓⡶⠒⢢⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⠶⢦⡞⠛⢶⠒⠲⡄⠀")
                    print("   ⣾⠀⢸⡇⠀⢸⠀⠀⡇⠀⢸⡀⠀⠀⠀⠀⠀⢰⠃⠈⡇⠀⢸⡇⠀⢸⠀⠀⣇⠀")
                    print("   ⣿⠀⢸⣇⣠⠾⠶⠶⠷⠦⢼⣷⠀⠀⠀⠀⠀⢸⡄⢀⣧⣀⡼⠷⠶⠾⠶⢴⡿⡄")
                    print("   ⢸⠉⠉⠀⠹⣄⣀⣀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⡏⠉⠀⠈⢧⣀⣀⠀⠀⠀⢀⡇")
                    print("   ⠈⣇⠀⠀⠀⠀⠸⠁⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠰⠇⠀⠀⠀⡼⠀")
                    print("   ⠀⠘⢦⣀⣀⣀⣀⣀⣀⡤⠊⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⣀⣀⣀⣀⣀⡤⠞⠁⠀")
                elif teacher[i] == '바위' and player == '가위':
                    # print('teacher: 내가 이겼단다')
                    result = "You Lose"
                    print(f"\x1b[44m {result.center(38, ' ')} \x1b[0m ")
                    print("   ⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡖⠙⢦⠀⠀⣴⠚⢲⠀")
                    print("   ⠀⣀⣀⡤⠶⣴⠚⠓⡶⠒⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠘⡆⢠⠇⠀⡼⠀")
                    print("   ⣾⠀⢸⡇⠀⢸⠀⠀⡇⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⢻⡾⠀⢠⡇⠀")
                    print("   ⣿⠀⢸⣇⣠⠾⠶⠶⠷⠦⢼⣷⠀⠀⠀⠀⠀⠀⢀⣠⡞⠉⣻⠶⠶⠤⠤⣼⡀⠀")
                    print("   ⢸⠉⠉⠀⠹⣄⣀⣀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⢯⠀⢹⡄⠙⣦⣤⠀⠀⠈⢳⠀")
                    print("   ⠈⣇⠀⠀⠀⠀⠸⠁⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⠸⣦⠴⠛⠛⠁⡏⠀⠀⠀⣸⠀")
                    print("   ⠀⠘⢦⣀⣀⣀⣀⣀⣀⡤⠊⠀⠀⠀⠀⠀⠀⠀⠀⠙⢤⣀⣀⣀⣀⣀⣠⠔⠁⠀")
                elif teacher[i] == '바위' and player == '보':
                    win = win + 1
                    # print('teacher: 네가 이겼단다')
                    result = "You Win"
                    print(f"\x1b[44m {result.center(38, ' ')} \x1b[0m ")
                    print("   ⠀⠀⠀⠀⠀⠀      ⠀⠀⠀⠀⠀⠀⠀⡤⣄⠀⡎⢱⠀⢀⠤⡄⠀⠀")
                    print("   ⠀⣀⣀⡤⠶⣴⠚⠓⡶⠒⢢⠀⠀⠀⠀⠀⠀⠀⠈⡇⢸⠀⡇⢸⠀⡜⢀⠇⠀⠀")
                    print("   ⣾⠀⢸⡇⠀⢸⠀⠀⡇⠀⢸⡀⠀⠀⠀⠀⢸⠙⢆⢣⠀⣇⡇⢸⣤⠁⡸⠀⠀⠀")
                    print("   ⣿⠀⢸⣇⣠⠾⠶⠶⠷⠦⢼⣷⠀⠀⠀⠀⠈⢣⠈⠾⠀⠈⠁⠀⠉⢀⣇⠴⠊⡦")
                    print("   ⢸⠉⠉⠀⠹⣄⣀⣀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⣠⠤⠈⠁⢀⠔⠁")
                    print("   ⠈⣇⠀⠀⠀⠀⠸⠁⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠸⠁⠀⠀⢠⠇⠀⠀")
                    print("   ⠀⠘⢦⣀⣀⣀⣀⣀⣀⡤⠊⠀⠀⠀⠀⠀⠀⠀⠀⠘⠦⠤⠤⢤⣤⠴⠋⠀⠀⠀")
                elif teacher[i] == '보' and player == '보':
                    # print('teacher: 비김')
                    result = "Draw"
                    print(f"\x1b[44m {result.center(38, ' ')} \x1b[0m ")
                    print("  ⠀⠀⠀⡤⢤⠀⡜⠉⡆⠀⡤⢤⠀⠀⠀⠀⠀⠀⠀⡤⢤⠀⡜⠉⡆⠀⡤⢤⠀⠀")
                    print("   ⠀⠀⠀⢱⠀⡇⣇⠀⡇⢰⠁⡞⠀⠀⠀⠀⠀⠀⠀⢱⠀⡇⣇⠀⡇⢰⠁⡞⠀⠀")
                    print("   ⠰⡍⠱⣸⡄⢸⣿⠀⣇⡇⢰⠃⠀⠀⠀⠀⠰⡍⠱⣸⡄⢸⣿⠀⣇⡇⢰⠃⠀⠀")
                    print("   ⠀⠹⡄⠹⠇⠀⠁⠀⠉⠀⣾⡤⠚⢳⠀⠀⠀⠹⡄⠹⠇⠀⠁⠀⠉⠀⣾⡤⠚⢳")
                    print("   ⠀⠀⠙⡄⠀⠀⠀⣠⠴⠂⠉⢀⡴⠁⠀⠀⠀⠀⠙⡄⠀⠀⠀⣠⠴⠂⠉⢀⡴⠁")
                    print("   ⠀⠀⠀⢳⠀⠀⠐⠃⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠐⠃⠀⠀⢀⡞⠀⠀")
                    print("   ⠀⠀⠀⠀⠓⠤⠤⠤⠤⠤⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠤⠤⠤⠤⠤⠊⠀⠀⠀")

                elif teacher[i] == '보' and player == '바위':
                    # print('teacher: 내가 이겼단다')
                    result = "You Lose"
                    print(f"\x1b[44m {result.center(38, ' ')} \x1b[0m ")
                    print("  ⠀⠀⠀⣀⡀⠀⡤⠢⡀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⣀⡀⠀⠀")
                    print("   ⠀⠀⠀⡇⢸⠀⡇⠀⡇⢸⠀⡇⠀⠀⠀⠀⠀⢀⡴⠦⡞⠉⢹⡇⠀⣿⠁⢹⡆⠀")
                    print("   ⢠⠒⣄⢱⠀⣇⡇⠀⣇⠇⢰⠁⠀⠀⠀⠀⠀⢸⠀⠀⡇⠀⢸⡇⢀⣿⡀⢸⣧⠀")
                    print("   ⠈⢆⠘⣾⡄⠘⠃⠀⠛⠀⡎⣀⠤⢄⠀⠀⠀⠸⣦⡤⠿⢶⡟⠉⠉⠉⠉⠙⠻⡇")
                    print("   ⠀⠈⢆⠀⠀⠀⠀⢀⣀⠐⠛⠁⡠⠃⠀⠀⠀⠀⣇⠀⠀⠀⠙⢲⡶⠀⠀⠀⢸⠃")
                    print("   ⠀⠀⠈⡆⠀⠀⢰⠋⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⠈⠁⠀⠀⣠⠏⠀")
                    print("   ⠀⠀⠀⠘⢄⣀⣀⣀⣀⣠⠜⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠒⠒⠒⠒⠒⠋⠁⠀⠀")
                elif teacher[i] == '보' and player == '가위':
                    win = win + 1
                    # print('teacher: 네가 이겼단다')
                    result = "You Win"
                    print(f"\x1b[44m {result.center(38, ' ')} \x1b[0m ")
                    print("   ⠀⠀⢀⣀⠀⢰⠒⡄⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡖⠒⢦⠀⠀⣰⠒⢢⠀")
                    print("   ⠀⠀⠀⢣⠈⡆⢸⠀⡇⢠⠃⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠸⡄⢠⡇⠀⣼⠀")
                    print("   ⢠⡖⢦⢸⡀⢱⣾⠀⡇⡞⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⢳⡼⠀⢠⡇⠀")
                    print("   ⠀⢣⡀⢻⡇⠈⠋⠀⠛⠁⣸⢀⠤⢦⠀⠀⠀⠀⢀⣀⡖⠛⣷⠤⠬⣥⣤⣼⠀⠀")
                    print("   ⠀⠀⢳⡀⠀⠀⠀⠀⣀⡀⠛⠁⣠⠞⠀⠀⠀⠀⣏⠈⢻⡀⠻⣤⣤⠀⠀⠈⢧⠀")
                    print("   ⠀⠀⠀⢧⠀⠀⠀⠎⠁⠀⠀⡰⠁⠀⠀⠀⠀⠀⠸⣦⠼⠛⠚⠉⡟⠀⠀⠀⣸⠀")
                    print("   ⠀⠀⠀⠈⢦⣀⣀⣀⣀⣀⠴⠁⠀⠀⠀⠀⠀⠀⠀⠳⣄⣀⢀⣀⡀⢀⣀⠴⠃⠀")
                    print("   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠀⠀⠀⠀")
                round = round + 1
            else:
                continue
        if win >= 2:
            break
        else:
            print()
            conv(npc, "다시 도전 해봐. 야 너두 졸업 할 수 있어")
            print()
            round = 1
            continue
    # 미션 07-5 이동 전 독백
    conv(npc, "너는 이제 개발자가 될 준비가 된거 같다.")
    print()
    print()
    print()
    print()
    print()
    input("\x1b[31m>> 졸업을 완료 했습니다.\n계속하려면 아무 키나 입력하세요. \x1b[0m")
    os.system('clear')
    # 미션 07-6 종료
    print()
    print()
    print()
    pLoc = 9
################################### ▲ 미션07 ▲ ####################################

################################### ▼  졸업  ▼ ####################################
import sys

now = datetime.now()
date = now.strftime("%Y.%m.%d")

str1 = ' 졸 업 장'
str22 = f'{pName} (인성 : {pKind})'
str3 = date
str31 = '위 학생은 개발 능력 향상을 위해'
str32 = '전 과정을 성실히 마쳤으므로'
str34 = '이 졸업증서를 수여합니다.'
str4 = '교 장  최 하 문'
str5 = ' '


l01 = ("{0:　^32}".format(str1))
l02 = ("{0:　>33}".format(str5))
l03 = ("{0:　>31}".format(str22))
l04 = ("{0:　^32}".format(str5))
l05 = ("{0:　^34}".format(str31))
l06 = ("{0:　^33}".format(str32))
l07 = ("{0:　^35}".format(str34))
l08 = ("{0:　^38}".format(str5))
l09 = ("{0:　^35}".format(str3))
l10 = ("{0:　^33}".format(str4))
print()
print()
print()
print()

print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⡿⠿⠛⠻⢿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀"+ f"\x1b[33m    {l01}    \x1b[0m ")
print("⠀⠀⠀⠀⢀⣠⣴⣾⡿⠟⠋⠁⠀⠀⠀⠀⠀⠈⠙⠻⠿⣷⣦⣄⡀⠀⠀⠀⠀⠀"+ f"\x1b[33m    {l02}    \x1b[0m ")
print("⠀⢀⣴⣾⣿⠛⠋⠁⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣀⣀⣀⣈⡉⠛⣿⣷⣦⡄⠀⠀"+ f"\x1b[33m    {l03}    \x1b[0m ")
print("⠀⠀⠉⠛⠿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠛⠛⣻⣿⣿⣿⣿⠛⠉⠀⠀⠀"+ f"\x1b[33m    {l04}    \x1b[0m ")
print("⠀⠀⠀⠀⠀⠀⢹⣿⠻⢿⣶⣦⣄⡀⠀⢀⣠⣴⣶⡿⠿⣿⡏⢹⣿⠀⠀⠀⠀⠀"+ f"\x1b[33m    {l05}    \x1b[0m ")
print("⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠈⠙⠻⠿⣿⠿⠟⠋⠁⠀⠀⣿⡇⢸⣿⠀⠀⠀⠀⠀"+ f"\x1b[33m    {l06}    \x1b[0m ")
print("⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⢸⣿⠀⠀⠀⠀⠀"+ f"\x1b[33m    {l07}    \x1b[0m ")
print("⠀⠀⠀⠀⠀⠀⠘⣿⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠇⢸⣿⠀⠀⠀⠀⠀"+ f"\x1b[33m    {l08}    \x1b[0m ")
print("⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣶⣤⣤⣄⣀⣀⣤⣤⣶⡿⠟⠁⠀⢸⣿⠀⠀⠀⠀⠀"+ f"\x1b[33m    {l09}    \x1b[0m ")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"+ f"\x1b[33m    {l10}    \x1b[0m ")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")


end = input("\x1b[31m>> Enter 입력 시 종료 \x1b[0m")
if end == "":
    sys.exit("게임을 종료합니다.")