#----------------------------------------------------------------
# 사용자 정의 함수 def
#----------------------------------------------------------------
# 함수의 기능 : 2개의 정수를 덧셈 한 후 결과를 return 하는 함수
# 함수 이름 : add
# 매개 변수 : 2개, num1, num2
# 함수 결과 : 덧셈 계산 값 변수명(정할수있음)

def 더하기(num1, num2):
    결과=num1+num2
    return 결과
# 함수 사용하기 함수 호출-------------------------------
# 함수명(데이터1, 데이터2, 데이터3)
value=더하기(10,20)
print(value)

# 함수의 매개변수 갯수와 다른 데이터 전달은 안됨!
# val=더하기(10,20,30)
# print(val)

# 부족해서 에러
val=더하기(10) 
print(val)




























