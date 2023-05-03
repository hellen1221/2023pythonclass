def mykeyprint(**dargs):
    for key in dargs:
        print(key, ':', dargs[key], end = ' ')
    print()
    
mykeyprint(여자친구=6, 마마무=4)
mykeyprint(엑소=9, 트와이스=9, 블랙핑크=4, 방탄소년단=7)

coffeeprice = {'에스프레소': 2500, '아메리카노': 2800, '카페라떼': 3200}
mycar =	{"brand": "현대", "model": "제네시스", "year": 2016}
mykeyprint(**coffeeprice)
mykeyprint(**mycar)
