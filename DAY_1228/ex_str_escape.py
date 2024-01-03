# ---------------------------------------------------
# str 데이터에서 특별한 의미를 자기는 문자를 이스케이프문자
# - 형태 : \알파벳1개 또는 \문자1개
# - 대표
#   \n  : 줄바꿈       \t  : 탭간격
#   \'  : 인용부호     \"  : 인용부호
#   \u  : 유니코드     \\  : 파일이나 웹 주소 경로
# ---------------------------------------------------
print('Happy New Year 2024~!')
print('Happy New \'Year\' 2024~!')
print("Happy New \"Year\" 2024~!")

# 파일 경로 -------------
print("C:\\ProgramData\\tGoodix")

# => 파일 또는 데이터 경로일 경우 이스케이프 문자를 비활성화 설정
# => r'경로'
print(r'C:\ProgramData\tGoodix')