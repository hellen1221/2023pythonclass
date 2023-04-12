outStr = ""
inStr = input("문자열을 입력하세요 : ")
count = len(inStr)

for k in range(0, count) :
     outStr += inStr[count - (k + 1)]

print("내용을 거꾸로 출력 --> %s" % outStr)