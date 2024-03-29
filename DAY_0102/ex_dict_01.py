# ----------------------------------------------------------------------
# [질문] 10명 학생에 대한 학점을 저장하기
# - 학생의 이름과 학점
# ----------------------------------------------------------------------
# 방법1) 학생 이름 변수 10개 => stdName1 ~ stdName10
#        학점 변수 10개 => jumsu1 ~ jumsu10
stdNums01='std01'
stdNums02='std02'
stdNums03='std03'
stdNums04='std04'
stdNums05='std05'

# jumsu01=90
# jumsu02
# jumsu03
# jumsu04
# jumsu05

# 방법2) 학생 이름 변수 1개 => stdNames[학생 이름1,....,학생 이름10
#        학점 변수 1개 => stdJumsus=[점수1,....,점수10]
stdNums = ['std01','std02','std03','std04','std05']
stdJumsus = [90,89,100,76,34]

# => 학번03번 학생의 학번과 점수를 출력하세요~
idx=stdNums.index('std03')

print(f"{stdNums[idx]}학번 학생의 점수 {stdJumsus[idx]}")

# 방법3) 학생 이름 변수 10개 => stdNames[학생 이름1,....,학생 이름10
#
stdNumsJums = [['std01',90],['std02',89],['std03',100],['std04',76],['std05',34]]

# -----------------------------------------------------------------------
# dict 자료형
# - 연관되어 있는 데이터를 하나로 묶어서 저장하는 방식 => 연관배열
# - 형태 => 키 : 데이터 (예 : 주민번호:이름, 학번 : 전공)
# - 조건 => 키가 중복되면 안됨!
# - 문법 => {키1 : 데이터1, 키2 : 데이터2,...,키N:데이터N}
# -----------------------------------------------------------------------
stdnumsJumsu= {'std01':90,'std02':80,'std03':70,'std04':95,'std05':99}
print(f'stdnumsJumsu : {len(stdnumsJumsu)}개,{type(stdnumsJumsu)},{stdnumsJumsu}')

# 원소 읽는 방법 => 변수명[키] 딕셔너리는 인덱스 없다!
print(f"stdnumsJumsu['std03'] => {stdnumsJumsu['std03']}")

# 마지막 원소 지정하는 -1 사용 ==> -1에 대한 키가 없으면 ERROR
# print(f"stdnumsJumsu[-1] => {stdnumsJumsu[-1]}")

# ------------------------------------------------------------
# 원소/요소 추가 방법 => 변수명[새로운 키] = 데이터
# ------------------------------------------------------------
stdnumsJumsu['std10']=99.8
print(f'stdnumsJumsu : {len(stdnumsJumsu)}개,{stdnumsJumsu}')

# ------------------------------------------------------------
# 원소/요소 데이터 변경 => 변수명[기존 키] = 새로운 데이터
# ------------------------------------------------------------
# 학번 10인 학생의 점수 99점으로 변경
stdnumsJumsu['std10']=99
print(f'stdnumsJumsu : {len(stdnumsJumsu)}개,{stdnumsJumsu}')

# ------------------------------------------------------------
# 원소/요소 데이터 삭제 => del 변수명[키] 또는 del(변수명[키])
# ------------------------------------------------------------
del stdnumsJumsu['std10']
print(f'stdnumsJumsu : {len(stdnumsJumsu)}개,{stdnumsJumsu}')
