# str 데이터 타입 전용 함수, 메서드 살펴보기
# 문자열을 구성하는 문자를 검사해주는 메서드
# 특징 : isxxxx() ---> True, False 출력
# 알파벳으로 구성된 문자열 인지 검사해줌. isalpha()
data="Good"
print(f'{data} => 알파벳인지 검사 {data.isalpha()}')

#대문자인지 검사 .isupper()
data="Good"
print(f'{data} => 대문자 검사 {data.isupper()}')
print(f'GGOODD=> 대문자 검사 {"GGOODD".isupper()}')
print(f'good=> 대문자 검사 {"good".isupper()}')

# 소문자 검사 .islower()
print(f'GGOODD=> 소문자 검사 {"GGOODD".islower()}')
print(f'good=> 소문자 검사 {"good".islower()}')
print(f'GGoooD=> 소문자 검사 {"GGoooD".isupper()}')

# 숫자로 구성된 문자열인지 검사 .idsecimal()
print(f'1234=> 숫자 검사 {"1234".isdecimal()}')
print(f'GGoooD123=> 숫자 검사 {"GGoooD123".isdecimal()}')

# 숫자 문자(aplha) 혼합된 경우 : isalnum()
print(f'1234=> 숫자 문자 혼합 검사 {"1234".isalnum()}')
print(f'GGoooD123=> 숫자 문자 혼합 검사 {"GGoooD123".isalnum()}')

# 공백 문자 여부 검사 .isspace()
print(f'1234    => 공백검사 {"1234   ".isspace()}')
print(f'            => 공백검사 {"         ".isspace()}')


























