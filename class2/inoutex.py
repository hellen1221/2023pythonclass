pay = int(input('시간당: '))                            # input() 문자 입력, int() 정수로 변환
wtime = float(input('일한 시간: '))                     # input() 문자 입력, float() 실수로 변환

total = int(pay * wtime)
tax = int(total * 0.03)

print('\n시간당 %d원, %.1f시간 일함' % ( pay, wtime))   # \n은 줄바꿈
print('세금 %d원, 총액 %d원' % (tax, total - tax))
