k = 3
exlist = [20, 10, 7, 30, 35, 70, 35]
for d in range(k):
    mvalue = min(exlist)
    di = exlist.index(mvalue)        # 최소값의 인덱스를 구하는 함수 index사용
    del(exlist[di])
print(k, 'th value', mvalue)