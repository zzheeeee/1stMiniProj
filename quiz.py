alphabet = 'a'
str1 = '───'+' '
str2 = alphabet+' │ '

print(' ',str1*10)
print(' │',str2*10)
print(' ',str1*10)
#######################
alphabet = 'a'
str1 = '───'+' '
str2 = alphabet+'   '

print(' ',str1*10)
print('  ',str2*10)
print(' ',str1*10)
#######################

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

alphabet = 'a'
str1 = '───'+' '
str2 = alphabet+'   '

print(' ',str1*10)
print('  ',str2*10)
print(' ',str1*10)

#("%4s"%k)
str00 = "{0:<15}".format('┃')
str01 = "{0:>15}".format('┃')
str1 = "┏"+"┓"

pt1 = "★　보안　설정 ★"
pt2 = "- 폴더 비밀번호 (월마다 교체 필수!!)"
pt3 = "   8월 : Z F T F H G"
pt4 = "   9월 : H V K G V N Y U I"
pt5 = "   10월 : L X G L Y U I"
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
print(aa+'\n'+dd+'\n'+ff+'\n'+pt3+'\n'+pt4+'\n'+pt5+'\n'+pt6+'\n'+zz+'\n'+aa)

import random
month = random.randint(1,12)
pw = ['QZMFZIB', 'UVYIFZIB', 'NZIXS', 'ZKIRO', 'NZB', 'QFMV', 'QFOB','ZFTFHG', 'HVKGVNYVI', 'LXGLYVI', 'MLEVNYVI', 'WVXVNYVI']

err = 0
print('* Hint : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')
print('* Hint : Z Y X W V U T S R Q P O N M L K J I H G F E D C B A')
print(len('* Hint : Z Y X W V U T S R Q P O N M L K J I H G F E D C B A'))
while True:
    upw = input(f'지금은 {month}월이다. \n비밀번호 입력: ')
    if upw.upper() == pw[month-1]:
        print('열렸다!')
        break
    else:
        print('오답입니다.')
        continue






