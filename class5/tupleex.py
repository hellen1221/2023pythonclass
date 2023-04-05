menu = ('기본햄버거', '치즈햄버거', '불고기버거', '와퍼킹버거')
price = (4000, 4500, 5000, 7000)

for k in range(len(menu)):
    print(k+1, ':', menu[k], ':', price[k])


# 만약에 메뉴추가한다면 list로 만들어 추가 한후 다시 튜틀로 가능
# menu.append('새우버거')
# price.append(5500)

lmenu = list(menu)
lprice = list(price)
lmenu.append('새우버거')
lprice.append(5500)

menu = tuple(lmenu)
price = tuple(lprice)
print('메뉴:',menu)
print('가격:', price)