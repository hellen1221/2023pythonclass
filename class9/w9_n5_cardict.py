carDict = {'H101': ('2017', '3000'), 'K301': ('2022', '2000'), 'H401': ('2020', '3200'),
           'D221': ('2020', '1500'), 'H111': ('2022', '3000'), 'K301':('2022', '2700')}

for k in carDict :
    print(k, carDict[k])
    
yearList = []
for k in carDict :
    idata = int(carDict[k][0])
    yearList.append(idata)
print(yearList)

syear=int(input('몇년도 차의 수 검색 : ?'))
print('%d의 등록 차는 %d대입니다' %(syear, yearList.count(syear)))
