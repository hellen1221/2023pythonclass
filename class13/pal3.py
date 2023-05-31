from collections import deque

def palindrom_check3(pstring):
    qu = deque()
    st = deque()
    for x in s:
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())
    while qu:
        if qu.popleft() != st.pop():
            return False

    return True


pstringList = ['아하아', '역삼역', '구로구', 'Mom', '기러기', '비둘기', '기특한 특기', 'racer', 'father', '봄', '여름']

for s in pstringList:
    print('{0} = {1}'.format(s, palindrom_check3(s)))
