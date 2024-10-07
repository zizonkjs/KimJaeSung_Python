# 입력 10번 숫자데이터 받기
# 입력 데이터를 모두 더해서 합계가 30 이상이 되면
# 10번 입력 안 받았더라도 종료해주세요.

# nums=list(map(int, input(" 숫자 입력 받기 10개: ").split()))
total=0
for cnt in range(10):
    data=int(input("숫자입력 : "))
    total=total+data
    print(total)
    if total>30: break


        