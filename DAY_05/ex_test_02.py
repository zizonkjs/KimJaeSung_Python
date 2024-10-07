# 조건부표현식
# 임의의 숫자가 5의 배수가 맞는지 결과를 출력
# 2와 5를 제외한 나머지는 고려하지 않는다.

num=int(input("정수 입력 : "))

if num%5 ==0:
    print(f"{num}은 5의 배수")
else:
    print(f'{num}은 5의 배수가 아님')

print(f"{num}은 5의 배수") if num%5==0 else print(f'{num}은 5의 배수가 아님')

a=True if  num%5==0 else False
print(f'입력된 값 : {num}, 5의 배수확인: {a}')

# 문자열 입력 받아서 문자열 원소 개수를 저장
# 단 원소 개수가 0이면 None 저장
# 1. 문자열 입력 받기
# 2. 0인 경우 None을 저장
msg=input("문자열 입력 : ")
if len(msg):
    result=len(msg)
else:
    result=None

num=len(msg) if not len(msg)==0 else None

num2=len(msg) if len(msg) else None

print(f'저장된 문자열 갯수 확인 : {num}')
print(f'저장된 문자열 갯수 확인 : {num2}')

#사칙연산자
# +,-,*,/ 와 숫자 2개 입력받기
## 입력된 연산자에 따라서 계산 결과 저장
# 예) 입력 : + 10 3 출력 : 13
command=input("4칙 연산자 1개 숫자 2개 입력 : ").split()

print(f'입력된 값 확인 : {command}')
command[1]=float(command[1])
command[2]=float(command[2])
if command[0]=='+':
    r=(command[1])+(command[2])
elif command[0]=='-':
    r=(command[1])-(command[2])
elif command[0]=='*':
    r=(command[1])*(command[2])
elif command[0]=='/':
    r=(command[1])/(command[2])

print(f'계산한 결과 값 : {r}')


