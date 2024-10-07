# 디폴트 매개변수 함수
# 함수 호출 시 데이터가 전달되지 않는 경우 미리 지정된 값으로 처리해줌.
# 형식 def 함수명 (매개변수1, 매개변수2, ...., 매개변수=0) 매개변수에 기본값이 미리 들어가있음.
def add(num1=0, num2=0):
    return num1+num2
print(add())
print(add(5))
print(add(4,5))

# 함수기능 : 회원가입
# 함수이름 : register()
# 매개변수 : id, pw, gender
#           성별은 기본 값으로 '남' 
# 함수 결과 : 'ooo님 가입을 환영합니다.' str
def register( id, pw, gender='남'): # 디폴트 매개변수는 뒤로 가게만들기
    return f'{id}님 {gender}가입을 환영합니다.'

print(register('kk', 'k123'))

print(register('kk', 'k123', '여'))

def test(n1, n2, *nums):
    print(n1, n2, nums)

