# for문 한개써서 구구단 작성
# gugu=""

# for dan in range(2,10):
#     print(f'{dan}단')
#     a=list(range(1,10))

#     gugu=dan*a[0], dan*a[1], dan*a[2], dan*a[3], dan*a[4], dan*a[5], dan*a[6], dan*a[7], dan*a[8]
#     print(gugu)
#     print(f'{dan}*{a[0]}={dan*a[0]}')
#     print(f'{dan}*{a[1]}={dan*a[1]}')
#     print(f'{dan}*{a[2]}={dan*a[2]}')
#     print(f'{dan}*{a[3]}={dan*a[3]}')
#     print(f'{dan}*{a[4]}={dan*a[5]}')
#     print(f'{dan}*{a[6]}={dan*a[6]}')
#     print(f'{dan}*{a[7]}={dan*a[7]}')
#     print(f'{dan}*{a[8]}={dan*a[8]}')


# 구구단 출력시 2단   3단   4단   5단
            #  ...   ...   ...  ...
#              6단   7단   8단   9단       
#              ...  ...    ...  ...

# 규칙을 찾는게 먼저임. 손도 못된 이유 : 규칙을 찾을 생각 안했음.
# 검색하고 챗봇해도 되는데 내걸로 만들어야함. 즉 이해하고 활용할 수 있도록 외워야함.

  # 모르겠네요................................

# while 반복문으로 문자 10번 출력하기
# i = 0
# while i <10:
#     print('안녕')
#     i=i+1

# while 반복문 사용하기
# while 조건식:
#   반복할 코드
#   변화식

# 초깃값을 1부터 시작하기
# i = 1
# while i <10:
#     print('안녕')
#     i=i+1

# 초깃값을 감소시키기
# i = 20
# while i > 10:
#     print('안녕')
#     i=i-1

# 입력한 횟수대로 반복하기
# count=int(input("반복횟수 입력 :"))
# i = 0
# while i < count:
#     print("안녕")
#     i=i+1

# random 모듈을 이용해서 while 사용하기 -> import random 선언해줘야함.
# import random
# i = 0
# while i !=3:
#     i = random.randint(1,6)
#     print(i)

# random.choice
# dice=[1,2,3,4,5,6]
# print(random.choice(dice))
# print(random.choice(dice))
# print(random.choice(dice))

# while 반복문으로 무한 루프 만들기
# while True:
#     print("안녕")
# 나가고 싶으면 ctrl+C

# 퀴즈
# 1번, b,c
# 2번 b
# 3번 문제가 잘못됨 
# 4번 e,a

# 연습문제: 변수 2개를 다르게 반복하기
# 정수 2, 5, 4
# 4,8,3
# 2, 32, 1 
# 각줄에 출력되게 만들기
# while 조건식은 두개 지정 두 변수 모두 변화
# i=2
# j=5
# while i<=32 or j>=1:
#     print(i,j)
#     i *= 2
#     j -= 1

# 심사문제: 교통카드 잔액 출력하기
# 표준 입력으로 금액이 입력.
# 1회당 요금 1350원 사용 할 때마다 각줄에 잔액을 출력하는 프로그램만들기
# 최초금액은 출력하지 않기, 잔액은 음수가 될 수 없고 부족하면 출력끝
# mycash=int(input("내 돈 입력(양수만 사용) : "))
# cost=1350

# if mycash<0:
#         print("음수로 입력된 돈")
#         zandon=mycash
# elif mycash<1350:
#       print("잔액부족함")
#       zandon=mycash
# elif mycash>=cost:
#       zandon=mycash-cost

# while zandon>=cost:
#       zandon=zandon-cost
#       print(f"당신의 잔돈 : {zandon}")
#       if zandon<1350:
#             print("잔액부족")
            

            
# break로 반복문 끝내기
# while 에서 break로 반복문 끝내기
# i = 0
# while True:
#     print(i)
#     i +=1
#     if i ==100:
#           break

# for에서 break로 반복문 끝내기
# for i in range(10000):
#       print(i)
#       if i== 100:
#             break

#continue로 코드 실행 건너뛰기
# for i in range(100):
#       if i % 2 ==0:
#             continue
#       print(i)

# while 반복문에서 continue로 코드 실행 건너뛰기
# i = 0
# while i <100 :
#       i +=1
#       if i % 2 == 0:
#             continue
#       print(i) -> 나머지가 0이면 무시 1이면 True로 출력.

# 반복문과 pass
# for i in range(10):
    # pass -> 아무일도 하지 않음

#입력한 횟수대로 반복하기
# count = int(input('반복할 횟수 입력 :'))
# i=0
# while True:
#       print(i)
#       i +=1
#       if i == count:
#             break

# 입력한 숫자까지 홀수 출력하기
# count = int(input('반복할 횟수를 입력 : '))

# for i in range(count+1):
#     if i % 2 ==0:
#         continue
#     print(i)

# 퀴즈
# 1번 b,d
# 2. b
# 3. c

# 연습문제: 3으로 끝나는 숫자만 출력하기 18.5
# 0~73 사이의 숫자 중 3으로 끝나는 숫자출력
# 3 13 33 43 53 63 73 규칙 찾기 연산자 사용해서 -> %10 했을 때 나머지 3
# i=0
# while True:
#     if i>73: break

#     if i%10 !=3: 
#         i=i+1
#         continue # 컨티뉴를 그만두게 하는 코드 넣어줘야함.
    
#     print(i, end='')
#     i=i+1


#심사문제: 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력하기
# 표준 입력으로 정수 2개 입력
# 첫번째 값 범위는 1~200
# 두번째 값은 10~200
# 첫번째 입력 값은 두 번째 입력 값보다 항상 작다.
# 첫째 정수와 둘째 정수 사이의 숫자 중 3으로 끝나지 않는 숫자가 출력.

# strat=int(input("숫자입력 : "))
# stop=int(input("숫자입력 2 : "))

# i = strat
# while True:
#     if i>stop: break
#     if i%10==3:
#         i=i+1
#         continue # 가능하면 컨티뉴 전에 증가 시켜주기
#     print(i,end='')
#     i=i+1


# i = 1
# j = 20
# while i<j:
#     i=i+1
#     print(i)

# 중첩 루프 사용하기
# for i in range(횟수):
#     for j in range(횟수):
#         가로처리코드
#     세로처리코드

# for i in range(5): # 5번 반복, 바깥쪽 루프는 세로 방향
#     for j in range(5): # 5번 반복 안쪽 루프는 가로 방향
#         print('j:', j, sep='', end=' ') # j값 출력
#     print('i:', i, '\n', sep='') # i 값 출력

# 사각형으로 출력하기
# for i in range(5):
#     for j in range(5):
#         print('*', end='') # j 뿐만 아니라 i 도 이 코드를 사용함.
#     print()

# for i in range(3): # 3번 세로 반복
#     for j in range(7): # 7번 가로반복
#         print('*', end='')
#     print()

# # 계단식으로 출력하기
# for i in range(5):
#     for j in range(5):
#         if j <=i:
#             print('*', end='')
#     print() # 가로방향으로 별을 그린뒤 다음줄로 넘어감

# # 대각선으로 별출력하기
# for i in range(5):
#     for j in range(5):
#         if j==i:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print() # 가로방향으로 별 그리고 다음줄

#     #연습문제 : 역삼각형 모양으로 별 출력하기
#     for i in range(6):
#         for j in range(6):
#             if j<=i:
#                 print(' ', end='')
#             else:
#                 print('*', end='')
#         print()

# 심사 문제 : 산 모양으로 별 출력하기
num=3




# for i in range(num):
   
#     for j in range(num):
#         if j < i:
#             print(' ', end='')
#             if j==0:
#                 print('*', end='')
       

# FizzBuzz 문제
# 1부터 100까지 숫자 출력하기
# for i in range(1,100):
#     print(i)

# # 3의 배수일 때와 5의 배수일 때 처리하기
# for i in range(1, 101):
#     if i % 3 == 0:
#         print('Fizz')
#     elif 1 % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# #3과 5의 공배수 처리하기
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5==0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# # 논리 연산자를 사용하지 않고 3과 5의 공배수 처리하기
# for i in range(1,101):
#     if i % 15 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# # 코드 단축하기
# for i in range(1, 101):
#     print('Fizz' * (i % 3 == 0)+'Buzz'*(i % 5 == 0) or i)

# 연습문제
# for i in range(1,101):
#     if i%2 == 0 or i%11 == 0:
#         print('FizzBuzz')
#     elif i%2 == 0:
#         print('Fizz')
#     elif i%11 == 0:
#         print('Buzz')
#     else:
#         print(i)

# 심사문제 : 5와 7의 배수, 공배수 처리하기
# a = int(input("작은수 입력 : "))
# b = int(input("큰수 입력 : "))

# for c in range(a,b):
#     if c%5 == 0 or c%7==0 :
#         print("FB")
#     elif c%5 == 0:
#         print("F")
#     elif c%6==0:
#         print("B")
#     else:
#         print(c)



        


    

    
          