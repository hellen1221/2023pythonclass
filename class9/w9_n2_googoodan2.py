
print('Googudan by python---')

for dan in range(2, 10):
    print('\n%d단 :' % dan, end='') if dan % 2 == 0 else print() 
    for num in range(1, 10):
        if num == 1 or num == 9 :
            continue
        if dan % 2 == 0 :
            print('%2d x%2d =%3d ' % (dan, num, dan*num), end='')
        else:
            break

