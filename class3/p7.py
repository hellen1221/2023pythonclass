# 내장함수 eval(), range()
select = int(input("1. 입력한 수식 계산  2. 두 수 a부터 b까지 의 합계 : "))

if  select == 1 :
    nexp = input(" *** 수식을 입력하세요 : ")
    answer = eval(nexp) 
    print(" %s 결과는 %5.1f입니다. " %(nexp, answer))
    
elif select == 2 :
    num1 = int(input(" *** 첫 번째 숫자를 입력하세요 : "))
    num2 = int(input(" *** 두 번째 숫자를 입력하세요 : "))
    answer = 0
    for i in range(num1, num2+1) :
        answer = answer + i
    print("%d+...+%d는 %d입니다. " %(num1, num2, answer))

else :
    print("1 또는 2만 입력해야 합니다.")