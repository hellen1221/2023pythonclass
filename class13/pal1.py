
def palindrom_check1(pstring):
    rstring= list(reversed(pstring))
    ispal = True
    for k in range(len(pstring)):
        if pstring[k] != rstring[k]:
            ispal = False
    return ispal

pstringList = ['역삼역', '구로구', 'Mom', '기러기', '비둘기', '기특한특기', 'racer', 'father', '봄', '여름']

for s in pstringList:
    print('{0} = {1}'.format(s, palindrom_check1(s)))



