#-------------------------------------------------
# 중첩조건문
# if 조건식:
#   실행코드
#   if 조건식:
#       실행코드
#   else:
#       실행코드
# else:
#   실행코드
# 숫자가 음이아닌 정수와 음수 구분하기
# 음이 아닌 정수중에 0과 양수 구분하기
# 음이아닌 정수 : 숫자>=0
#   숫자>0 는 양수로 출력.
num=int(input("숫자만 입력 : "))

if num>=0:
    print(f'{num}은 음이 아닌 정수')
    if num>0:
        print(f'{num}은 양수')
    else:
        print(f'{num}은 양수는 아닙니다.')
else:
    print(f'{num}은 음수')

if num>0:
    print(f"{num}은 양수")
elif num<0:
    print(f"{num}은 음수")
else:
    print(f"{num}은 0입니다.")

#-------------------------------------------------------
# 동네이름 데이터에서 입력 받은 동네이름 해당 여부 member 연산자 사용
city=['대구,', '부산', '울산']
data='마산'
if data in city:
    print(f'{data}는 광역시입니다.')
else:
    print(f'{data}는 광역시가 아닙니다,')

