import random as r
import time as t

def sadari(st) :        # def: 사용자가 만든 함수 sadari()
    s= r.randrange(st)
    return s                # returns: s값반환, 함수 끝

sdr= [0]
sdr= input('사다리 타기 항목 입력: ').split()
for k in range(len(sdr)) :
    hit= sadari(len(sdr))  # sadari()로부터 값 받음
    t.sleep(2)              # 2초간 뜸들이다가
    print(k, '번은', sdr[hit])
    del(sdr[hit])           # 출력된 항목 리스트에서 삭제
