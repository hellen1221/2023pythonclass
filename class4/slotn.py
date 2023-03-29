import random as r
import time as t

slot = [0, 0, 0] # slot = [0] * 3도 같은 코드
n = int(input('슬롯머신을 몇 번 돌릴까요?'))

              
for s in range(n) :
    for k in range(3) :
        slot[k] = r.randrange(7, 10) # 무작위 수 7, 8, 9 생성
        print('%d ' % slot[k], end = '')
        t.sleep(2)
    if slot[0] + slot[1] + slot[2] == 21 : # 모두 7인지 검사
        print('\n잭팟이 터졌네요')
        break
    else :
        print('\n아까워\n')