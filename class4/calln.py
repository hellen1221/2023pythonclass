m = int(input('몇으로 나누는 놀이를 할까요?'))
print('Start : %d로 나누어지는 가장 가까운 수로 답하기\n' % m)

for k in range(5):
    call_number = int (input('Call number = '))

    r = call_number % m
    if (m-r) < r :
        ans = call_number + (m-r)
    else:
        ans = call_number - r
    print('The answer is %d\n' % ans)