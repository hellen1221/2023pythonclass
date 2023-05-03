
def fibo(n):
    if n < 2 : return 1
    else : return fibo(n-1)+fibo(n-2)


for k in range(13) :
    print('%d개월 후 토끼의 수 = %d' %(k, fibo(k)))