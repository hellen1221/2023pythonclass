upp, low, dig, pct = 0, 0, 0, 0

pswd = input('암호 입력: ')
if pswd.isalnum() == False : pct = 1    # 특수문자 있으면 pct = 1
for k in pswd:
    if k.isupper() : upp = 1            # 대문자 있으면 upp = 1
    elif k.islower() : low = 1          # 소문자 있으면 low = 1
    elif k.isdigit() : dig = 1          # 숫자 있으면 dig = 1

if low + upp + dig + pct >= 3 :
    print('사용 가능')
else : print('!!불가능한 암호!!')