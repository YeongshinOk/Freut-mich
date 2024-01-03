'''
출력 기능의 내장함수 print()
'''
# 1개 데이터 화면 출력 -----------------------------
print(1000)

# 2개 데이터 화면 출력 -----------------------------
print(100,200)
print(100, "Good Luck")

# 여러 개 데이터 화면 출력 --------------------------
print("ABC", 5.,"1000","HappyNewYear")

# 데이터가 없는 경우 화면 출력 -----------------------
print()

# -----------------------------------------------
# 데이터 출력을 좀 더 편하게 하는 방법들
# => 문자열과 숫자가 섞여 있는 경우가 대부분
# -----------------------------------------------
# [출력] 오늘은 2024년 12월 27일입니다.
print('오늘은 2024년 12월 27일입니다.')

year=2024
month=12
day=27

print("오늘은", year,"년",month,"월",day,"일입니다.")

# 변수를 str에서 적용해서 출력하는 방법 --- (1) ' %알파벳1개 '
# %d -- 10진수 정수 ===> "당신의 나이는 %d입니다."   %age
# %f -- 실수       ===> "평균이 %f점 입니다."      %avg
# %s -- 문자열     ===> " 당신의 고향은 %s입니다."  %name
age=100
avg=98.4
name="마징가"
print('당신의 나이는 %d세 입니다.' %age)
print("평균이 %f점 입니다." %avg)
print("당신의 고향은 %s입니다." %name)

print('당신의 나이는 %d세, 평균은 %f점, 고향은 %s이군요'%(age,avg,name))

# 변수를 str에서 적용해서 출력하는 방법 -- (2) f'{변수명}' f-스트링방식
print(f'당신의 나이는 {age}세 입니다.')
print(F'당신의 나이는 {age}세 입니다.')
print(f'당신의 나이는 {age}세이고, 평균은 {avg}점, 고향은 {name}이군요')
print(f"당신의 나이는 {age}세이고, 평균은 {avg}점, 고향은 {name}이군요")

# ------------------------------------------------------------------
# [실습] 본인 이름, 전공, 나이를 메모리 저장하기
#       저장된 정보를 아래와 같은 형태로 출력하세요.
#       이름 : 홍길동
#       전공 : 체육학과
#       나이 : 21세
# ------------------------------------------------------------------

name="옥영신"
major="사회학"
age=27

print(f'이름 : {name}')
print(f'전공 : {major}과')
print(f'나이 : {age}세')

print('이름 : %s' %name)
print('전공 : %s과' %major)
print('나이 : %d세'%age)

# ------------------------------------------------------------------
# 특별한 의미를 가지는 문자 조합 => 이스케이프문자
# 백슬러쉬 + 알파벳 1개
# \n --- new line 약자 줄바꿈
# \t --- tab 약자 키보드 탭키 만큼 간격
# ------------------------------------------------------------------
print(f'이름 : {name}\n 전공 : {major}과\n 나이 : {age}세')

# ------------------------------------------------------------------
# print()함수에서 여러 개의 데이터를 분리해서 출력해주는 방법
# - 기본 : 공백
# - 변경 : sep 매개변수 => 여러 개 데이터를 화면에 보기 좋게 분리
#           시켜 주는 방법 설정
# ------------------------------------------------------------------
print("홍","길동","의적")
print("홍","길동","의적",sep="")
print("홍","길동","의적",sep="****")
# ------------------------------------------------------------------
# print()함수에서 데이터 화면 출력 후 끝에 추가하는 문자 지정
# - 기본 : 줄바꿈 이스케이프 문자 \n
# - 변경 : end 매개변수 => 화면 출력 후 원하는 문자를 지정 가능
# ------------------------------------------------------------------
print("A", end='')
print("B",end='***')
print("C")

# ------------------------------------------------------------------
# [실습] 아래와 같이 출력이 되도록 코드를 작성하세요.
#       단 print()함수는 1개만 사용
#       ABCDEFG
#       123456789
#       ABCDEFG
# ------------------------------------------------------------------
# [방법1] - 이스케이프문자 사용
print("ABCDEFG\n123456789\nABCDEFG")

# [방법2] - print()함수의 sep
print("ABCDEFG", 123456789, "ABCEDFG", sep='\n')

# [방법3] - print()함수 여러개 사용하는 경우
print("ABCDEFG")
print(123456789)
print("ABCDEFG")