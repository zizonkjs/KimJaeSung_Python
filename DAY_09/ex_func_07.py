# 함수 이해 및 활용
# 함수기능 : 3개의 정수를 덧셈한 결과를 반환하는 함수
# 함수이름 : add3
# 매개변수 : num1, num2, num3
# 함수결과 : 정수반환 res=0
# -----------------------------

def add3(num1, num2, num3):
    res=num1+num2+num3
    return res
print(add3(22,33,44))
#  함수 이해 및 활용
# 함수기능 : 3개의 정수를 곱셈한 결과를 반환하는 함수
# 함수이름 : mutli3
# 매개변수 : num1, num2, num3
# 함수결과 : 정수반환 res=0

def multi3(num1, num2, num3):
    res=num1*num2*num3
    return res
print(multi3(22,33,44))



#  함수 이해 및 활용
# 함수기능 : 2개의 정수를 나눗셈한 결과를 출력
# 함수이름 : div
# 매개변수 : num1, num2
# 함수결과 : 실수반환 res=0

def div(num1,num2):
    if num2!=0:
        res=num1/num2
        print(res)
    else:
        print("두번째 숫자에 0쓰지마라 이눔시키야")

div(10,4)

# 함수 사용하기 즉 호출(improt)
# 덧셈하기
val=add3(5,6,7)

# 나눗셈하기
value1=div(3,4)
print(value1)

def plus(num1=0, num2=0, *num):
    total=0
    for n in num:
        total += n
    return num1+num2+total

def minus(num1=0, num2=0, *num):
    total=0
    for n in num:
        total -= n
    return num1-num2-total

def nanugi(num1=0, num2=1):
    if num2:

        return num1/num2
    else :
        print("0으로 나눌 수 없음")


def gopsam(num1=0, num2=1, *num):
    totla=1
    for n in num:
        totla *=n
    return num1*num2*totla

# 연산 수행 후 결과를 반환하는 함수
# 함수이름 : calc
# 매개변수 : 함수명, str 숫자 2개
# 함수결과 : 없음
def calc(func, num1, num2):
    num1=float(num1)
    num2=float(num2)
    
    print(f'결과 : {func(num1,num2)}')
   

# 함수기능 : 입력받은 데이터가 유효한 데이터인지 검사하는 함수
# 함수이름 : data_check
# 매개변수 : str 데이터, 데이터 수
# 함수결과 : True 또는 False
# def check_data(data, count):
#     data=data.split()
#     if len(data) == count:
#         isok=True
#         for d in 
    


# print(plus(1,2,3,4,5,6,7,8))
# print()
# print(minus(1,2,3,4,5,6,7,8))
# print()
# print(nanugi(1,plus(1,2,3,4,5)))
# print()
# print(gopsam(1,2,3,4,5,6,7,8))
# print("-----------------------------------------------")
#메뉴 출력 함수
# 함수 기능 : 계산기 메뉴 출력하는 함수
# 함수 이름 : gaesangi_menu
# 매개 변수 : 없음
# 함수 결과 : 없음

def print_menu():
    print(f'{"*":*^16}')
    print(f'{"계산기":^14}')
    print(f'{"*":*^16}')
    print(f'{"* 1 덧   셈 *":^14}')
    print(f'{"* 2 뺄   셈 *":^14}')
    print(f'{"* 3나 눗 셈 *":^12}')
    print(f'{"* 4 곱   셈 *":^14}')
    print(f'{"* 5 종   료 *":^14}')
    print(f'{"*":*^16}')

#계산기
# 사용자가 원하는 만큼 입력받을 수 있게 -> 'x', 'X' 입력 시
# 연산방식과 숫자 데이터 입력 받기
# while 함수 사용

# 사용자에게 원하는 계산을 선택하는 메뉴 출력
# 종료 메뉴 선택시 프로그램 종료
# -> while 반복문사용
# while True:
#     # 입력 받기
#     req=input("연산(+, -, *, /) 입력, 정수 2개 입력(예:+ 10 2) :")
#     # 종료 조건 검사
#     if req=='x' or req=='X':
#         print("계산기를 종료합니다.")
#         break
#     # 입력에 대한 연산방식과 데이터 추출 ' + 10 2'
#     op, num1, num2= req.split() # ['+','10','2']
#     num1=float(num1) # str 형변환 int
#     num2=float(num2)
#     #연산방식에 따라 계산 진행
#     if op=='+':
#         print(f'{num1}+{num2}= {plus(num1,num2)}')
#     elif op=='-':
#         print(f'{num1}-{num2}= {minus(num1,num2)}')
#     elif op=='*':
#         print(f'{num1}*{num2}= {gopsam(num1,num2)}')
#     elif op=="/":
#         print(f'{num1}/{num2}= {nanugi(num1,num2)}')
#     else:
#         print(f'{op}는 잘못된 연산자입니다.')

while True:
    print()
    print(print_menu())
    menu=input("하고싶은 연산을 선택하세요.") # isdecimal(사용해서 if 문으로 검사하는 방법도 있음.)
    if '1' in menu:
        num1=input('숫자1 입력 :')
        num2=input('숫자2 입력 :')
        if num1.isdecimal() and num2.isdecimal():
            calc(nanugi,num1,num2)
        else:
            print("잘못된 데이터입니다.")
        # print((f'{num1}+{num2}={plus(num1,num2)}'))
    elif '2' in menu:
        num1=input('숫자1 입력 :')
        num2=input('숫자2 입력 :')
        if num1.isdecimal() and num2.isdecimal():
            calc(nanugi,num1,num2)
        else:
            print("잘못된 데이터입니다.")
        # print((f'{num1}-{num2}={minus(num1,num2)}'))
    elif '3' in menu:
        num1=input('숫자1 입력 :')
        num2=input('숫자2 입력 :')
        if num1.isdecimal() and num2.isdecimal():
            calc(nanugi,num1,num2)
        else:
            print("잘못된 데이터입니다.")
        # if num2!=0:
        #     print((f'{num1}/{num2}={nanugi(num1,num2)}'))
        # else:
        #     print('0으로 나눌수 없습니다.')
    elif '4' in menu:
        num1=input('숫자1 입력 :')
        num2=input('숫자2 입력 :')
        if num1.isdecimal() and num2.isdecimal():
            calc(nanugi,num1,num2)
        else:
            print("잘못된 데이터입니다.")
        # print((f'{num1}*{num2}={gopsam(num1,num2)}'))
    elif '5' in menu:
        print("프로그램을 종료합니다.")
        break
    else:
        print("1~5까지 숫자만 입력하세요.")

    


