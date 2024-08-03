#import random
#
#month = random.randint(1, 12)
#pw = ['QZMFZIB', 'UVYIFZIB', 'NZIXS', 'ZKIRO', 'NZB', 'QFMV', 'QFOB', 'ZFTFHG', 'HVKGVNYVI', 'LXGLYVI',
#      'MLEVNYVI', 'WVXVNYVI']
#
#
#for i in range(0, 12):
#    print(pw[i], " ", end="")  # 원래 비밀번호
#    le = len(pw[i]) - 3  # 뒤에서 3자리 지우고 남은 길이
#    print(pw[i][0:le], " ", end="")  # 뒤에서 3자리 지우고 남은 비밀번호
#    print(pw[i][le:], " ", end="")  # 뒤 3자리 : 사용자 입력 정답 값
#    justle = len(pw[i])
#    print(pw[i][0:le].ljust(justle, "_"))  # 뒤 3자리 '_'로 채운 값 : 문제
#
#
#question = pw[month][0:len(pw[month]) - 3].ljust(len(pw[month]), "_")
#answer = pw[month][len(pw[month]) - 3:]
#print(f"{month}월: {question} 답: {answer} // {pw[month]}")


pt01 = ''
print(f"\x1b[40m    {pt01}    \x1b[0m ")
print(f"\x1b[41m    {pt01}    \x1b[0m ")
print(f"\x1b[42m    {pt01}    \x1b[0m ")
print(f"\x1b[43m    {pt01}    \x1b[0m ")
print(f"\x1b[44m    {pt01}    \x1b[0m ")
print(f"\x1b[45m    {pt01}    \x1b[0m ")
print(f"\x1b[46m    {pt01}    \x1b[0m ")