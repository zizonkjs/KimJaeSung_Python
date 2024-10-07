# 함수와 변수 - 지역/전역 변수
# 전역변수(Global)
# 파일 내에 존재하며 모든 곳에서 사용이 가능함.
# 프로그램이 실행시 메모리에 존재, 종료 시 메모리에서 삭제.
# 예시
total=100

# 함수와 변수 - 지역/전역 변수
# 지역변수(function) 내에 존재하며 함수에서만 사용가능
# 함수 실행 시 메모리 존재
# 함수 종료 시 메모리에서 삭제
# Hisotry : 회사에서 누가 언제 왜 수정했는지 적음.


#예시
# 함수 기능 : 정수를 덧셈 한 후 결과를 반환하는 함수
# 함수이름 : addInt
# 매개변수 : 0개~N개 -> 가변인자 *num
# 함수결과 : 정수 result
def addInt(*nums):
    total=0
    for n in nums:
        total +=n
    return total

def mutilInt(*nums):
    total1=1
    for n in nums:
        total1 *=n
    return total1 + total
# 지역변수에 total 없으니 Golbal 변수의 total=100 을 불러옴
# 그래서 total1 =1 을 생성

def mutilInt2(*nums):
    #전역변수의 데이터 값을 변경 할 경우 그냥 사용 할 수 없음.
    # 시스템한테 알려줘야됨
    global total
    for n in nums:
        total = total*n
    return total

#함수호출
res1=addInt(1)
print(f'res1= {res1}')


print(f'전 글로벌{total}')
res2=mutilInt2(5)
print(f'후 글로벌{total}')


