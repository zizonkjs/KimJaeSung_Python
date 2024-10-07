# 반복문 중단
# 반복을 중단 시키는 조건문과 함께 사용
# 숫자 데이터의 합계가 30이상이 되면 더이상 더하기 하지 마시요.
# 숫자 데이터는 1,50 으로 구성됨.

nums=range(1,51)
total=0

for n in nums:
    if total >= 30 :
        break # 반복중단
    total=total+n
print(f'total 값 : {total} {1} ~ {n-1} 까지의 합계')

# 4개 과목의 점수가 있음.
# 과목 점수가 평균 <= 40 이하 불합격. (한과목이라도 40이하면 불합격)
# 4개 과목 평균이 60점 이상되면 합격임.

# 40미만인지 체크
jumsu=list(map(int, input(" 점수를 입력 : ").split())) # 입력 받은 값을 정수로 변환하고 리스트로 저장.
ispass=True # -> flag 변수
for jum in jumsu:
    if jum<40:
        print("당신은 과락입니다.")
        ispass=False
        break

#합격 불합격 처리

if ispass:
    avg=sum(jumsu)/len(jumsu) # 평균
    if avg>=60:
         print(f' 당신은 평균 60점 이상! 합격')
    else:
        print(f' 당신은 평균 60점 미만! 불합격')
else:
    print(f' 당신은 40점 미만인 과목으로 불합격')

