# -------------------------------------------------------------------
# 튜플과 리스트
# -------------------------------------------------------------------
mydata = (10, 20, ['Hong',30],('KIM',12))

# 튜플의 원소/요소 갯수 확인 함수 => len()
print(f'mydata 원소 수 : {len(mydata)}개')

# 인덱스 범위
print(f'mydata 인덱스 : 0 ~ {len(mydata)-1}')

# 튜플에서 원소/요소 데이터 읽기
print(f'mydata[2] : {type(mydata[2])}')
print(f'mydata[3] : {type(mydata[3])}')
print(f'mydata[0] : {type(mydata[0])}')

# 튜플에서 0번째 원소의 데이터를 변경하기
# mydata[2] = 'Ten'       #튜플의 2번째 요소 변경 => 미지원
#mydata[2][0] = 'Park'   #['Hong', 30][0] = 'Park'

mydata[3][0] = 'Park'   #('KIM', 12)[0] = 'Park'

print(mydata)

# -------------------------------------------------------------------
# 튜플과 연산
# -------------------------------------------------------------------
# 1~10 범위에서 2의 배수로 구성된 정수 튜플 1개 => two
# 1~10 범위에서 5의 배수로 구성된 정수 튜플 1개 => five

two = tuple(range(2,11,2))
five = tuple(range(5,11,5))

print(two+five, two, five, sep='\n')

print(two*2,two,sep='\n')