# 사용자 정의 함수
# 덧셈, 뺄셈, 곱셈, 나눗셈 함수를 각각 만들기
# 매개변수는 : 정수 2개
# 함수 결과 : 연산 결과 반환
# n1=int(input("숫자를 입력 :"))
# n2=int(input("두번째 숫자를 입력 :"))

def 덧셈(num1, num2):
    
    return num1+num2

print(덧셈(1, 2))

def 뺄셈(num1, num2):
   
    return num1-num2

print(뺄셈(1, 2))

def 나눗셈(num1, num2):
    
    return num1/num2 if num2 else '0으로 나눌 수 없음.'

print(나눗셈(1, 2))

def 곱셈(num1, num2):
    
    return num1*num2

print(곱셈(1, 2))

# 사용자로부터 연산자, 숫자1, 숫자2, 입력받아서 
# 연산결과를 출력해주세요.
# input("연산자, 숫자1, 숫자2 :").split(',')
user=input("연산자, 숫자1, 숫자2 :").split(',')


if '+' in  user:
    덧셈(int(user[1]),int(user[2]))
    print(f'덧셈결과 : { 덧셈(int(user[1]),int(user[2]))}')
elif '-' in user:
    뺄셈(int(user[1]),int(user[2]))
    print(f'뺄셈결과 : { 덧셈(int(user[1]),int(user[2]))}')
elif '/' in user:
    나눗셈(int(user[1]),int(user[2]))
    print(f'나눗셈결과 : { 나눗셈(int(user[1]),int(user[2]))}')
    if int(user[2])==0:
        print("0으로 나눌수 없음")
elif '*' in user:
    곱셈(int(user[1]),int(user[2]))
    print(f'곱셈결과 : { 곱셈(int(user[1]),int(user[2]))}')
else:
    print("잘못된 데이터 +,정수,정수 로 입력하세요. \',\'도 넣으세요.")


# op, num1, num2 = input("연산자, 정수 2개 입력(,사용) :").split(',')

# if op not in ['+','-','*','/']:
#     print(f'{op} 잘못된 연산자입니다.')
# else:
#     if num1.isdecimal() and num2.isdecimal():
#         num1=int(num1)
#         num2=int(num2)
#         result=0
#         if op == '+' : 덧셈(num1, num2)
#         elif op == '-' : 뺄셈(num1, num2)
#         elif op == '/' : 나눗셈(num1, num2)
#         elif op == '*' : 곱셈(num1, num2)
#         print(f'{num1}{op}{num2}={result}')
#     else:
#         print('정수만 입력가능합니다.')

# 함수 기능 : 입력 데이터가 유효한 데이터인지 검사해주는 기능
# 함수이름 : check_data
# 매개 변수 : 문자열 데이터, 데이터 갯수 data, count
# 함수 결과 : 유효 여부 True/False

def 입력데이터유효검사(data, count, sep=' '):
    # 데이터여부
    if len(data):
        data2=data.split(sep)
        return True if count == len(data2) else False
    else:
        return False