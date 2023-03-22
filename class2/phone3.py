st_price = int(input('기본 통신비: '))
st_data = int(input('기본 데이터량: '))
ad_price = int(input('1기가당 추가 통신비: '))
used = int(input('한 달 기본 사용량: '))
unlimited = int(input('무제한요금: '))

add = (used - st_data) * ad_price
total = st_price + add

print('\n%d기가까지 %d원' % (st_data, st_price))
print('%d기가 사용하면 %d원' % (used, total))

if total > unlimited :
    print('무제한 요금제를 추천합니다')
else:
    print('특판요금제를 추천합니다')
    
