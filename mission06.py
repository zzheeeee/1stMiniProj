import random     # random.randint를 사용하기 위해 random모듈을 포함시킨다.
hee = {'name':'쩡','level':4, 'kind':80, 'weight':0, 'skill':[1,2,5]}
cha = {'name':'수빈','level':4, 'kind':100, 'weight':0, 'skill':[3,4,6]}
playerList = [hee, cha]
pIdx = random.randint(0,1)

pName = playerList[pIdx]['name']
pLevel = playerList[pIdx]['level']
pKind = playerList[pIdx]['kind']
pWeight = playerList[pIdx]['weight']

# 스킬 발동 여부 (확률)
pSkillTrue = random.randint(1,100)
if pSkillTrue >= 15:
    print("System : 쩡 스킬이 발동 성공하여 힌트를 얻습니다.")
else:
    print("System : 20% 확률로 스킬 발동 실패했습니다.")

where = "운동장"
npc = "양현종"
mission = "야구게임 시작"
inseong = -10
print(f"System:{where}입니다.")
print("상황설명")
print(f"{npc}:{mission}")
print("\'Y\'입력하면 시작 \'N\' 입력시 거절")
mission_yn = input("게임을 시작하시겠습니까?")
# 미션 예외 처리 / 미션 시작
if mission_yn == "Y" and mission_yn == "y" :
    print("Game Start")
elif mission_yn.upper !="N" or mission_yn == " " or mission_yn== "" or mission_yn != "n":
    print("System : 잘못 입력 하셨습니다.")
    mission_yn = input("게임을 시작하시겠습니까?")
elif mission_yn == "N" or mission_yn == "n":
    print(f"System: 인성이 {inseong} 되었습니다.")
    mission_yn = input("게임을 시작하시겠습니까?")

# 스킬 발동 여부 (확률)
pSkillTrue = random.randint(1,100)
if pSkillTrue >= 15:
    print("System : 쩡 스킬이 발동 성공하여 힌트를 얻습니다.")
else:
    print("System : 20% 확률로 스킬 발동 실패했습니다.")

# 야구 게임
num_lst = []

# 중복체크
for i in range(0,3):
    num_lst.append(random.randint(1,9))  # random.randint 1부터 9까지 정수 중 하나를 무작위로 선택해 num_lst에 추가
#print("처음 num_lst: ",num_lst)

for i in range(0,3):
    for j in range(0,3):
        if i != j:
            if num_lst[i] == num_lst[j]:
                #print(num_lst[i],num_lst[j])
                num_lst[j] = random.randint(1,9)
            #else:
                #print("중복체크 else: ",num_lst)
# 정답 숫자
#print(num_lst)
# 스킬 발동 첫번째 자리 알려주기
if pSkillTrue >= 15 :
    print("* Hint : 첫번째 자리 숫자 >>",num_lst[0])
# 1round - 9round
for r in range(0,9):
    strike_cnt = 0
    ball_cnt = 0
    out_cnt = 0
    # round 1 출력
    print(f"[ {r+1} Round ]")
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
    for i in range(0,3):
        for j in range(0,3):
            if num_lst[i] != int(user_num[j]):
                out_cnt = out_cnt + 1
            elif i == j:
                if num_lst[i] == user_num[j]:
                    strike_cnt = strike_cnt + 1
            else:
                if num_lst[i] == user_num[j]:
                    ball_cnt = ball_cnt + 1
    if strike_cnt + ball_cnt == 0 :
        print("out")
        print("---------------------------")
    # 9라운드 전에 정답을 맞힐경우
    elif strike_cnt == 3:
        print("정답입니다. 9라운드 되기전 맞춘 숫자 천재 ")
        #print(num_lst)
        break
    else:
        print("strike: ",strike_cnt)
        print("ball: ",ball_cnt)
        print("---------------------------")
#print("정답 :"num_lst)
print("System: 미션 성공입니다.")
print()
print(f"{npc}: 너 야구부에 들어 올지 않을래?")
print(f"{pName}: 아니 나는 졸업해서 개발자가 될꺼야")
print("이동중 독백 -------------------------")
f_key = input("System: 계속 하시려면 f 입력 ")
if f_key == "f":
# 미션 이동
    print("미션  교무실로 이동 ")
