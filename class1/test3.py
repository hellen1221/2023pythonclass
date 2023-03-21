count = 1
score = 10
ok = 0
while(count <= 3):
    print(count, end = " ")
    plan = input("생활계획 입력 : ")
    print("오늘 이 계획을 잘 수행했나요?(yes/no)")
    ans = input()
    if (ans == "yes"):
        ok = ok+1
    count = count + 1
score = score + (ok * 30)
print("오늘의 생활점수는 :", score)
