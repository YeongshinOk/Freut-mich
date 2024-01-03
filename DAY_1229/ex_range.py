# -----------------------------------------------------------
# range() 내장함수
# - 숫자의 범위를 생성해주는 함수
# - 반환값/결과값/리턴값 : range 타입
# - 범위에 포함되는 숫자 데이터는 원소/요소라고 함 => 인덱싱
# -----------------------------------------------------------
# 1 ~ 20 으로 구성된 정수 데이터 생성
nums = range(20)

print(f'nums => {nums},{type(nums)}')
print(f'nums => {nums[0]},{type(nums[0])}')
print(f'nums => {nums[-1]},{type(nums[-1])}')
print(f'nums => {len(nums)}개')

# 앞부분 5개 원소까지만 추출 => 슬라이싱
print(f'nums[0:5] => {nums[0:5]}, {type(nums[0:5])}')

# range ==> list 형 변환하기 => list(데이터)
print(f'list(nums) => {list(nums)}')

# 1 ~ 100으로 구성된 정수 리스트 생성해주세요
numlist = list(range(1,101))
print(f'numlist => {numlist}')

# ---------------------------------------------------------------
# range(시작값, 끝값)
# - 시작값 => 기본 : 0       range(10) => 0 <= ~ < 10
# - 시작값 => 1              range(1,10) => 1 <= ~ < 10
# - 시작값 => 5              range(5,10) => 5 <= ~ < 10
# ---------------------------------------------------------------
# 1 ~ 30 범위에서 3의 배수만으로 구성된 리스트 생성

threes = list(range(3,31,3))
print(threes)

# 1 ~ 1000 범위에서 3의 배수만으로 구성된 리스트 생성

tri = list(range(3,1001,3))
print(tri)
