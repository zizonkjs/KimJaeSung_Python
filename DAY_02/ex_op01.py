#----------------------------------------------
# 연산자 
#----------------------------------------------
# [1] 산술 연산자
# 종류: +,-,*,/,//(몫),%(나머지),**(제곱)
num1=8
num2=3

# 출력형태 : 8 + 3 = 11
print(f'{num1}+{num2}={num1+num2}')
print(f'{num1}-{num2}={num1-num2}')
print(f'{num1}*{num2}={num1*num2}')
print(f'{num1}/{num2}={num1/num2}')
print(f'{num1}//{num2}={num1//num2}')
print(f'{num1}%{num2}={num1%num2}')
print(f'{num1}**{num2}={num1**num2}')
print("-------------------------------------------------")
# [2] 비교연산자 ------------------------------
# - 종류 : >, <, >=, <=, ==, !=(같지않다) 결과는 True, False로 나옴.
num1='aF'
num2='ac'
print(f'{num1}>{num2}={num1>num2}')
print(f'{num1}<{num2}={num1<num2}')
print(f'{num1}>={num2}={num1>=num2}')
print(f'{num1}<={num2}={num1<=num2}')
print(f'{num1}=={num2}={num1==num2}')
print(f'{num1}!={num2}={num1!=num2}')
