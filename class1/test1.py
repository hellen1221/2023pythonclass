csum = 0
day = 1
while(day <= 7):
    fah = int(input("화씨온도 : "))
    cel = (fah - 32) * 5 / 9
    print(day,"일의 섭씨온도 : ", cel)
    csum = csum + cel
    day = day + 1
print("섭씨온도 평균 = ", csum/7)