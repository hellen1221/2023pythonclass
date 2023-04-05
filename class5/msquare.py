n = int(input("입력 :")) #마방진사이즈 입력

#0으로 채워진 2차원리스트 만들기
table = [[0]*n for k in range(n)]
i= 0; j = n//2; table[i][j] = 1
count = 2
while count <= n*n:         #for count in range(2, n*n+1)
    row = i-1; col = j-1
    if row < 0 :  row = n-1
    if col < 0 :  col = n-1
    if table[row][col] != 0 :
        i += 1
    else :
        i= row; j = col
    table[i][j] = count
    count += 1
print('magic number = ', sum(table[0])); print(table)
print('------------------------')
for row in table:
    print(row)
print('------------------------')

for row in range(n) :
    for col in range(n) :
        print('%4d' % table[row][col], end='')
    print()
    