# [문제]-----------------------------------------------------
# - 문자열 여러개와 실수 숫자 여러개를 두 줄로 일력 받기
# - 첫번째 입력 받은 값은 Key
# - 두번째 입력 받은 값은 Value
# - 딕셔너리로 저장해 주세요.
# -----------------------------------------------------------
twoData = input("문자열 4 ~ 5개, 실수 숫자 4 ~ 5개를 두줄로 입력\n단. 문자열과 실수 갯수는 동일\n(예:ab bb cc dd, 3.1 5.2 6.5 8.1) : ")

# key와 value로 데이터 분리
keys, values = twoData.split(',')

#datas=twoData.split(',')
#keys=datas[0].split()
#values=datas[1].split()


# 입력 데이터 존재 여부 체크
if (len(keys)==4 and len(values)==4) or (len(keys)==5 and len(values)==5) :
    print("입력 OK")
    dataDict = {}
    if len(keys)==4:
        dataDict[keys[0]] = values[0]
        dataDict[keys[1]] = values[1]
        dataDict[keys[2]] = values[2]
        dataDict[keys[3]] = values[3]
    else:
        dataDict[keys[0]] = values[0]
        dataDict[keys[1]] = values[1]
        dataDict[keys[2]] = values[2]
        dataDict[keys[3]] = values[3]
    print(f'dataDict => {dataDict}')
else:
    print("입력된 데이터가 정확하지 않습니다.")