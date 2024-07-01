# page 74
# 1. 다음 중 변수를 만드는 방법으로 올바른 것을 고르세요.
# x = 10
# 2. 다음 중 변수 이름으로 사용할 수 없는 것을 모두 고르세요.
# 300, if, 99%, 30seconds
# 3. 다음 중 변수와 연산자의 사용 방법으로 올바르지 않은 것을 모두 고르세요.
# b+=a, c-=b
# 4. 다음과 같이 값이 두개 입력됩니다. 입력된 값을 실수로 변환하여 변수 두 개에 저장하는 방법을 고르세요.
# 1.5 2.7
# a, b = map(float, input("실수를 입력하세요 : ").split())

#-----------------------------------------------------------------------------------------------------
# 연습문제 : 정수 세 개를 입력받고 합계 출력하기
# a, b, c=map(int, input("값을 입력하세요 입력후 띄어주세요 : ").split())

# print(a+b+c)

# 심사문제 변수 만들기
# 다음 소스 코드를 완성하여 50, 100, None이 출력되게 만드세요
# a, b, c=50, 100, None
# print(a, b, c)

# 심사문제 : 평균 점수 구하기
# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다. 평균 점수를 출력하는 프로그램을 만드세요.
# input에서 안내문자를 출력하지마세요. 평균점수를 출력할 때 소수점 이하 자리를 생략합니다.
# korean, engilsh, math, sicence= map(int, input().split())
# (korean + engilsh + math + sicence)/4

# 퀴즈 
# 1. 다음 중 3.1 Python 100을 한 줄에 출력하는 방법으로 올바른 것을 고르세요.
# print(3.1, 'python', 100)

# 2. 다음 중 16:9를 출력하는 방법으로 올바른 것을 고르세요.
# print(16, 9, sep=':')

# 다음 중 "Hello" 와 'Python'을 두 줄로 출력하는 방법으로 올바른 것을 모두 고르세요.
# print("Hello", "python", sep="\n")

# 연습문제 : 날짜와 시간 출력하기
# 다음 소스 코드를 완성하여 날짜와 시간이 출력되게 만드세요.
# year=2000
# month = 10
# day = 27
# hour= 11
# minute = 43
# second = 59
# print(year, month, day, sep="/", end=" ")
# print(hour, minute, second, sep=":")

# 심사문제 : 날짜와 시간 출력하기
# 표준 입력으로 년, 월, 일, 시,분, 초가 입력됩니다. 
# 다음 소스 코드를 완성하여 입력된 날짜와 시간을 년-월-일T시:분:초 형식으로 출력하세요.
# year=1999
# month=12
# day=31
# hour=10
# minute=37
# second=21
# print(year, month, day, sep="-", end="T")
# print(hour, minute, second, sep=":")


# 변수에 값이 어떻게 저장되는지 확인하는 스크립트
# import sys
# print(sys.getrefcount(1000))

# x=1000
# print(sys.getrefcount(1000))

# y=1000
# print(sys.getrefcount(1000))

# print(x is y)

#행렬 곱센 연산자
#행렬 곱센 연산자는 파이썬 3.5 이상 부터 사용
import numpy as np # numpy 모듈을 가져옴
a = np.array([[1, 2, 3], [4,5,6], [7,8,9]]) # 3x3 행렬 생성
b = np.array([[1,2,3], [4,5,6], [7,8,9]]) # 3x3 행렬 생성
a @ b # 행렬 곱셈
print(a @ b )

#page 93 퀴즈
# 'x는 5와 같다 >>> x = 5

# 비교 연산자의 결과로 올바르지 않은 것은.
#  8 is 4 * 2.0

# 다음 중 비교 연산자와 논리 연산자의 결과로 올바른 것을 모두 고르세요.
# a=10, b=20 일 때
# b != 20 or a !=10 True
# not b != 20 and a > 5, False

# 다음 중 논리 연산의 결과를 뒤집는 연산자로 올바른 것을 고르세요.
# not 

# 연습문제 : 합격 여부 출력하기
# 국어, 영어, 수학, 과학 점수가 있을 때 한 과목이라도 50점 미만이라면 불합격.
# 다음 소스 코드를 완성하여 합격이면 True, 불합격이면 False를 출력.
# korean=92
# english=47
# math=86
# science=81
# print(korean>=50, english>=50, math>=50, science>=50)

# 심사문제 : 합격 여부 출력하기
# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력.
# 국어는 90점 이상, 영어는 80점 초과, 수학은 85점 초과, 과학은 80점 이상일 때 합격
# 다음 소스 코드를 완성하여 합격이면 True, 불합격이면 False가 되게 출력.
# kor=90
# eng=81
# math=86
# sice=80
# print(kor>=90, eng>80, math>85, sice>=80)

#page 100 quiz
# 문자열을 표현하는 방법으로 올바른 것을 모두 고르세요.
# "Hello, world!", 'Hello, world!'

# 문자열을 여러 줄로 표현하는 방법
# '''안녕하세요.
# 파이썬 입니다'''
# """안녕하세요
# 파이썬 입니다"""

# 문자열 안에 '(작은따옴표)'나 "(큰따옴표)"를 넣는 방법
# 'Hello, \'python\''
# """"hello", python"""

# 연습문제:여러 줄로 된 문자열 사용하기
d = '''드디어 과제의 막바지
허리가 부러질거 같다.
이제 노트북 닫고 자야지'''
print(d)

# 심사문제 : 여러 줄로 된 문자열 사용하기
s ='''\'python\' is a \"programming language\" \n that lets you work quickly\n and \n integrate systems more effectively.'''
print(s)

