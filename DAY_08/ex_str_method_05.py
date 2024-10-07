
# 1개 문자열을 여러개 문자열로 분리해주는 메서드 split()
# 분리기준 기본값 : 공백
msg=" Happy New Year "
print(msg.split())
res=msg.split()
print(f'result => {type(res)}')
print(res)

phone='010-2222-3333'
res=phone.split() # 공백이 없을시 하나의 원소로 저장
pres=phone.split('-') # 쪼개고싶을 때 기준을 정해서 요소저장하기
print(pres)

phon2e='오늘은 날씨가 좋군요. 내일도 날씨가 좋을까요?'
res=phon2e.split('.')
print(res)

# 여러개 문자열을 1개로 합쳐주는 join()
# 합칠문자.join( 여러개 문자열 )
# 010*1111*2222
con = '_'

phone=con.join(pres)
print(phone)

con = ' '

phone=con.join(pres)
print(phone)

# 문자열 구성하는 문자 검사 메서드 => 변수명.isOOO()
# -----------------------------------------------------------------------------
# 문자열 내에 숫자 존재여부 체크 메서드들 3종류
# - 변수명.isnumeric()  : 0~9까지의 숫자, 5¹, 5₁, ①, ➊, ⅒, Ⅳ, ⅳ, 百
# - 변수명.isdigit()    : 0~9까지의 숫자, 5¹, 5₁, ①, ➊ 
# - 변수명.isdecimal()  : 0~9까지의 숫자
#    ==> 실수, 음수, 나머지 : False
# - isdecimal() < isdigit() < isnumeric()
# -----------------------------------------------------------------------------