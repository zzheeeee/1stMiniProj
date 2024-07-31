import random
import os

hee = {'name': '쩡', 'level': 4, 'kind': 80, 'weight': 0, 'skill': [1, 2, 5]}
cha = {'name': '수빈', 'level': 4, 'kind': 95, 'weight': 0, 'skill': [3, 4, 6]}
playerList = [hee, cha]
pIdx = random.randint(0, 1)

pName = playerList[pIdx]['name']
pLevel = playerList[pIdx]['level']
pKind = playerList[pIdx]['kind']
pWeight = playerList[pIdx]['weight']


# 시작 화면
start = input("System : 게임을 시작작하려면 \'f\'를 입력하세요.")

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

# 캐릭터 선택
where = "교무실"
npc = "이하복 교수님"
mission = "미션 시작"
choice_num = int(input("개발몬을 선택하세요."))
if choice_num == 1:
    pIdx = choice_num
elif choice_num == 2:
    pIdx = choice_num
print(f"System : {pName} 개발몬 선택 ")

# 터미널에서 python file 실행 시 위에 출력 화면 지워준다.
# 터미널 python file 실행 방법 : python3 파일명.py
os.system('clear')

print(f"System : {where}입니다.")
print()

print(f"{pName} : 교수님 졸업 시켜주세요.")
def pass_con():
    cont = input("대화 넘어가기 enter 입력")
    return cont
if pLevel < 10 :
    print(f"{npc} : 너 레벨이 몇이니?")
    pass_con()
    print(f"{pName} : {pLevel} 입니다.")
    pass_con()
    print(f"{npc} : 졸업하기엔 개발 레벨이 낮구나.")
    print(f"{npc} : 미션을 줄테니 레벨 10이되면 다시 찾아오거라.")
elif pLevel == 10 :
    print(f"{npc} : 졸업 축하한다.")