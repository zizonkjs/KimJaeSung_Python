# if 조건문 사용하기
# if 조건문은 if에 조건식을 지정하고 :(콜론)을 붙이고 실행할 코드 입력.
# if 조건식:
#   실행코드

# x = 10
# if x ==10:
#     print(f'{x}입니다.')

# if 조건문 사용시 주의점
# if x =10: 사용시 에러발생 비교연산자 ==을 사용

# if 조건문에서 코드를 생략하기
# x=10
# if x ==10:
#     pass
# pass 는 그냥 넘어간다는 뜻.
# 활용
# if x ==10:
#   pass -> 나중에 할일은 주석으로 남겨 놓는식임. 

# if 조건문: 사용후 들여쓰기 필수~

# 중첩 if 조건문 사용하기
# if x>=10:
#     print('10 이상입니다.')
#     if x ==15:
#         print('15입니다.')
#     if x ==20:
#         print('20입니다.')

# 사용자가 입력한 값에 if 조건문 사용하기
# x = int(input("숫자만 입력하세요 : "))

# if x== 10:
#     print('10입니다.')
# if x == 20:
#     print('20입니다.')

#퀴즈
# 13.5 1번문제 c번, 2번 문제 c,j 3번문제 a

# 연습문제
# x의 값이 10이 아닐때 ok 가 출력
# x =5
# if x!=10:
#     print("ok")  

#심사문제: 온라인 할인 쿠폰 시스템 만들기
# 표준 입력(가격)과 쿠폰 이름이 각줄에 입력. cash 3000 쿠폰 은 3000원, cash 5000쿠폰은 5000원을 할인
# 쿠폰에 따라 할인된 가격을 출력하는 프로그램
# data=int(input())
# cash3000=3000
# if data>3000:
#     print(data-cash3000)

# data2=int(input())
# cash5000=5000
# if data2>5000:
#     print(data2-cash5000)

#else 사용하여 두 방향으로 분기
# if 조건식:
#   실행코드
# else:
#   실행코드
# x=5
# if x ==10:
#     print('10입니다.')
# else:
#     print('10이 아닙니다.')

#if 조건문의 동작 방식 알아보기
# 조건식이 아닌 값으로 if 와 else의 코드를 동작
# if True:
#     print('참')
# else:
#     print('거짓')

# if False:
#     print("참")
# else:
#     print("거짓")

# if None:
#     print("참")
# else:
#     print("거짓")
# print("-"*90)

# # if 조건문에 숫자 지정하기
# if 0:
#     print('참')
# else:
#     print('거짓')
    
# if 1:
#     print('참')
# else:
#     print('거짓')

# if 0x1F:
#     print('참')
# else:
#     print('거짓')

# if 0b1000:
#     print('참')
# else:
#     print('거짓')

# if 13.5:
#     print('참')
# else:
#     print('거짓')
# print("-"*90)

# # if 조건문에 문자열 지정하기
# # 문자열은 내용이 있을 때 참, 빈 문자열은 거짓.
# if 'hello':
#     print('참')
# else:
#     print('거짓')

# if '':
#     print('참')
# else:
#     print('거짓')
# print("-"*90)

# # 0,None,빈 문자열을 not으로 뒤집으면?
# if not 0:
#     print('참')

# if not None:
#     print('참')

# if not '':
#     print('참')
# print("-"*90)

# #조건식을 여러개 지정하기
# x =10
# y=20
# if x ==10 and y==20: # or, not 사용가능
#     print('참')
# else:
#     print('거짓')

# # 14.5 퀴즈
# # 1번 c,
# # 2번 b
# # 3번 참
# # 4번 b,c,e
# # 5번 a

# # 연습문제:합격여부 판단하기
# # A 기업의 입사시험은 필기 80점 이상 코딩 시험을 통과해야 합격(Ture,False 구분) 합격불합격 출력
# Agi=75
# coding_test= True
# if Agi>=80 and coding_test:
#     print("합격")
# else:
#     print("불합격")

#심사문제 : 합격 여부 판단하기
# 입력 값으로 국어 영어 수학 과학 입력.
# 여기서 평균 80점 이상은 합격
# 평균 점수에따라 합격 불합격 출력 100의 범위를 벗어나면 잘못된 점수라고 출력

# kor=int(input("점수만 입력 : ").split())
# eng=int(input("점수만 입력 : ").split())
# math=int(input("점수만 입력 : ").split())
# sic=int(input("점수만 입력 : ").split())

# if kor>100 or eng>100 or math>100 or sic>100:
#     print("잘못된 점수")
# elif kor<=100 or eng<=100 or math<=100 or sic<=100:
#     jumsu=(kor+eng+math+sic)/4
#     print(f'당신의 평균점수 : {jumsu}')
#     if jumsu>=80:
#         print("합격")
#     else:
#         print("불합격")

# 국영수과=input("점수 4개 입력 : ").split()
# 국영수과=list(map(int, 국영수과))

# if 국영수과[:4]>100 or 국영수과[:4]<0:
#     print("잘못된 점수")
#     if 국영수과[:4]<=100:
#         평균=(국영수과[0]+국영수과[0]+국영수과[0]+국영수과[0])/4
#         print(f'평균점수 : {평균}')
#         if 평균>=80:
#             print("합격")
#         else:
#             print("불합격") ---> 안됨 ㅋㅋ
        

#elif 사용
# elif는 else인 상태에서 조건식을 지정할 때 사용
# elif 단독으로 사용 할 수 없음.
# x=30
# if x ==10:
#     print('10입니다')
# elif x==20:
#     print('20입니다')
# else:
#     print('10도 20도 아닙니다.')

# 음료수 자판기 만들기
# button=int(input())

# if button ==1:
#     print('콜라')
# elif button ==2:
#     print('사이다')
# elif button ==3:
#     print('환타')
# else:
#     print('제공하지 않는 메뉴')

#퀴즈
#1번 b,d,e
#2번 e

#연습문제 : if, elif, else 모두 사용하기
# 변수 x가 11과 20사이면 '11~20', 21과 30 사이면 '21~30, 아무것도 해당안되면 '해당안됨' 출력
# x=int(input("정수만 입력 : "))
# if 20>=x>=10:
#     print('11~20')
# elif 21>=x>=30:
#     print('21~30')
# else:
#     print('해당사항 없음')

# 심사문제
# 교통카드 시스템 만들기
# 표준 입력 나이입력. 단 입력 값은 7이상일 때만
# 나이에 맞게 요금을 계산한뒤 잔액이 출력.
# 교통카드는 9000원 있음
# 어린이 7세이상 12세이하 : 650
# 청소년 13세이상 18세 이하 : 1050
# 어른 19세이상 : 1250
# age=int(input('7세이상 나이 입력 :').split())
# mycash=9000

# if 12>=age>=7:
#     print('650원입니다.')
#     잔돈=mycash-650
#     print(f"잔돈은 {잔돈} 입니다.")
# elif 18>=age>=13:
#     print('1050원입니다')
#     잔돈=mycash-1050
#     print(f'잔돈은 {잔돈} 입니다')
# elif age>=19:
#     print('1250원 입니다.')
#     잔돈=mycash-1250
#     print(f'잔돈은 {잔돈} 입니다.')
# else:
#     print('6세이하는 무료입니다.')



