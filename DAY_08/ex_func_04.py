# 사용자 정의 함수
# 회원가입
# ID :
# pw :
# 직업, 이름, 번호, 성별, 등등
# 매개변수의 전달되는 데이터가 지정되지 않는 경우
# 어떤 데이터 종류 = 값 => 키워드 파라미터(매개변수)/키워드매개변수
# 형식 : def 함수명(**매개변수) -> **(키=값)의 형태로 넣어라

# 함수 기능 : 회원가입 가능 함수
# 함수이름 : register
# 매개변수 : 가입하는 사람마다 입력하는 정보가 모두 다름. **매개변수
# 함수결과 : 가입메시지str 

def register(**매개변수):
    print(type(매개변수))

register(name='honggidong', job='의적')
register(id='gmdgod123', age=10, gender='남')
register()



# 함수 기능 : 회원가입 가능 함수
# 함수이름 : register2
# 매개변수 : 필수입력사항 id, pw , email
# 선택입력 : **매개변수
# 함수결과 : 가입메시지str 

def register2(id, pw, email, **매개변수):
    print(type(매개변수))

register2("Hong", "H12345", "h@naver.com", gender='F') # **은 키값=값 으로 추가
register2("Hong", "H12345", "h@naver.com")