# 중첩 반복문일 경우의 break는 가장 가까이 있는 반복문만 종료
# 단의 숫자만큼만 구구단을 출력하세요.
# 2단이면 2*1=2  2*2=4
# 3단이면 3*1=3  3*2=6 3*3=9
# 4단 이면 . . . .
#dan=int(input("출력 원하는 단 입력 : "))

# [중첩 반복문] 내부 반복문 종료 시 외부 반복문 종료
# 내부 반복문 종료여부를 변수에 저장
# 내부 반복문이 종료되면 함께 종료하기
# 단출력하는 반복문 하나
dan=int(input("숫자만 입력 : "))
sibreak=False # 변수 선언
for d in range(2,10):
    print(f'\n[{d}단]', end=" ")
    for n in range(1,10):
         print(f'{d} * {n} = {d*n:<2}', end=" ")
         if n==d:
            sibreak=True # 내부 반복문 종료여부를 변수에 저장
            break
    print( "outer for")
    if sibreak: break # 내부 반복문이 종료되면 함께 종료하기 현재 sibreak 값은 True

#변수 선언 안했을 때. 
# for d in range(2,10):
#     print(f'\n[{d}단]', end=" ")
#     for n in range(1,10):
#          print(f'{d} * {n} = {d*n:<2}', end=" ")
#          if n==d: break
#     if d == dan: break

# break문 안썼을 때
# for d in range(2, dan+1):
#     print(f'\n[{d}단]', end=" ")
#     for n in range(1, d+1):
#         print(f'{d} * {n} = {d*n:<2}', end=" ")