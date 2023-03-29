arr = [0]*3   #배열에 대입문을 쓰려면 초기화 필요
arr[0]=100
arr[1]=200
arr[2]=300
sum = 0
for k in range(3) :
    sum += arr[k]
print('List Sum = ', sum)