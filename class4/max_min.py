n=int(input("몇개의 데이터 처리 : "))
listex = []         # append 안쓰고 대입하려면 listex = [0]*n                  
sum = 0

print('%d개의 데이터 입력 : ' % n)
for k in range(n):
    listex.append(int(input()))   #listex[k] = int(input())
    sum += listex[k]
      
print('리스트 데이터의 합과 평균  : %d, %.2f\n' % (sum, sum/n))

max, min = listex[0], listex[0]

for k in range(1, n):
    if listex[k] < min :
        min = listex[k]
    if  listex[k] > max  :
        max = listex[k]

print('주어진 리스트는 최대값(%d), 최소값(%d)을 가지고 있습니다' % (max, min))

# sum, min, max 리스트 함수 있음 max_min2.py참고