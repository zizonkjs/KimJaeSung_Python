# 모듈 : 변수, 함수, 클래스가 들어있는 파이썬 파일
# 패키지 : 동일한 목적의 모듈들을 모은 것
#          여러개의 모듈 파일이 존재함.
# 모듈 사용법 : improt 모듈파일명 <- 확장자 제외
import random as rad # as 사용하면 원하는 변수명으로 저장.

rad.random()

# 임의의 숫자를 생성해서 추출
rad.random

# 임이의 숫자 10개 생성 -> 0.0 <=~<1.0
for cnt in range(10):
    print(int(rad.random()*10))

print("-------------------------------------------------------------")
# -> 
for cnt in range(10):   
    print(rad.randint(0,1))

print("-------------------------------------------------------------")

# 로또 프로그램 범위
# 로또가 뭔지 조사
# 1~45 범위에서 중복되지! 않는 6개 추출
# 반복의 횟수 -> 알수 없음
# while문사용
# 종료조건 : 중복되지 않는 6개 숫자 출력되면 종료. -> dict
# dict의 key 설정

lotto=[0,0,0,0,0,0]
idx=0
while True:
    num = rad.randint(1,45)
    if num not in lotto:
        lotto[idx] = num
        idx=idx+1
    if idx==6: break
print(lotto)

lotto={}
key=1
while len(lotto)<6:
    num = rad.randint(1,45)
    if num not in lotto.values():
        lotto[key] = num
        key=key+1
    
print(lotto.values())

#------------------------------------------------------------
# set 타입의 add() 메서드(원소추가)
lotto=set()
while len(lotto)<6:
    num = rad.randint(1,45)
    lotto.add(num)
print(lotto)
