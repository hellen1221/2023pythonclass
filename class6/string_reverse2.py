outStr = ""
inStr = input("문자열을 입력하세요 : ")
count = len(inStr)

for k in range(count-1, -1, -1) :
     outStr += inStr[k]

print("내용을 거꾸로 출력 --> %s" % outStr)