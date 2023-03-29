import random
score=0
for k in range(5):
    correct = False
    tnum = 0
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    while tnum < 3 and not correct :      
        print('%d + %d = ' % (num1, num2), end='')
        ans = int(input())
        if ans == num1+num2:
            print('Corrcet!!!')
            correct = True
            score += (20-tnum*3)
        else:
            print('Try Again ---')
        tnum += 1
print('Score=%d' %score)