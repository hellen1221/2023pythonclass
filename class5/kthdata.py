# 데이터선택문제
#0에서 99까지의 random number를 20개 만든다
from random import randrange
#import random

exlist=[]
for k in range(20):
    exlist.append(randrange(0,100))

# 오름차순으로 정렬한 후 k번째 수 선택
k = int(input("몇번째 데이터를 원하시나요?"))
print(exlist)
exlist.sort()
print(exlist)
print(k, 'th data = ', exlist[k-1])

count = 1
exlist2 = []
while count < 10:
    num = randrange(0,10)
    print(num)
    if num not in exlist2:
        exlist2.append(num)
        count += 1

print(exlist2)

# 최소값을 구하고 삭제하는 것을 k 번 한다

for d in range(k):
    mvalue = min(exlist2)
    di = exlist2.index(mvalue)
    del(exlist2[di])

print(k, 'th value', mvalue)
# print(exlist2)
    