from random import randrange
from random import sample

#randrange() 함수와 집합을 이용, 중복을 제거
mylotto = set()
while True:
    num = randrange(1, 10)
    print(num, end=' ')
    mylotto.add(num)
    if len(mylotto) == 6:
        break
print('\n집합: {}'.format(mylotto))
print('정렬리스트: {}'.format(sorted(mylotto)))

#또 다른 방법 sample() 함수를 이용하면 매우 간편
print('\nsample로 번호리스트 만들기')
lotto = sample(range(1, 46), 6)
print('sample 함수 리스트: {}'.format(lotto))
print('sample 함수 정렬리스트: {}'.format(sorted(lotto)))