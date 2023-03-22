import random
gnum = 0
while True :
    com = random.randrange(3)
    user = int(input('가위0 바위1 보2 선택: '))

    if not(user in [0,1,2]):
        print('%d회 가위바위보 ==End of game===' % gnum)
        break
    
    print('user = %d, com = %d' % (user, com))
    gnum += 1
    if user == com :
        print('비겼습니다!')
    elif (user == 0 and com == 2) or (user == 1 and com == 0) or (user == 2 and com == 1) :
        print('user 승!')
    else : 
        print('com 승!')
        



