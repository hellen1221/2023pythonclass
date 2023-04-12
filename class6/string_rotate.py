import time as t

st1 = input("문자열 입력: ")

for k in range(len(st1) + 1) :
    for m in range(len(st1)) :
        print(' ', st1[ (k + m) % len(st1)], end='' ) # 한 글자씩 회전
    t.sleep(0.2)
    print('---')