menulist = ['기본햄버거', '치즈햄버거', '불고기버거', '와퍼킹버거']
pricelist = [4000, 4500, 5000, 7000]

# 두 리스트를 튜플이나 딕셔너리로 짝을 만들고 싶을때 zip()함수 사용
tlist = list(zip(menulist, pricelist))
dlist = dict(zip(menulist, pricelist))

print('튜플리스트 = ', tlist)
print('딕셔너리리스트 = ', dlist)
