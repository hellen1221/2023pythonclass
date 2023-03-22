print("===1부터 n까지의 짝수의 합 구하기 =")
sum = 0
n = int(input("어디까지의 합 ? "))
for digit in range(2, n+1, 2):
    sum = sum + digit
print("1부터 ", n, "까지의 짝수의 합 = ", sum)
