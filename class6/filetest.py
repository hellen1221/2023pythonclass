# 텍스트 파일 경로 설정
file_path = "d:\data\class.d"  #space 분리 데이터파일
# 딕셔너리 초기화
data_dict = {}

# 파일 오픈
with open(file_path, "r") as f:
    # 파일의 각 라인에 대해 반복
    for line in f:
        # 라인에서 id와 데이터를 추출하여 딕셔너리에 추가
        # id, *data = line.strip().split(":")
        # id, *data = line.split(":")
        id, *data = line.strip().split()
        data_dict[id] = tuple(data)

# 딕셔너리 출력
#print(data_dict)

for k in data_dict :
    print(k, data_dict[k])

smax = 0
for k in data_dict :
    if int(data_dict[k][1]) > smax :
        smax = int(data_dict[k][1]) 
print('최대 수강인원은 = ', smax)

# 리스트에 수강인원을 append하여 max()함수 이용

snumList = []
for k in data_dict :
    idata = int(data_dict[k][1])
    snumList.append(idata)
 
print('리스트 함수이용: 최대 수강인원은 = ', max(snumList))
