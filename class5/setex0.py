s1 = {0,1,3,5,7}  
s2 = set()
s2.add(2), s2.add(4), s2.add(6), s2.add(8), s2.add(0)

print('{0}과 {1}의 합집합 = {2}'.format(s1, s2, s1|s2))
print('{0}과 {1}의 교집합 = {2}'.format(s1, s2, s1&s2))
print('{0}과 {1}의 차집합 = {2}'.format(s1, s2, s1-s2))