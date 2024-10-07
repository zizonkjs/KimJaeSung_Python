# for 문 구구단 2단 부터 9단까지 모두출력
# 중첩 for 문
for n in range(2,10):
    print(f'단 : {n}')

    for m in range(1,10):
        gugudan=m*n
        print(f'{n}*{m} : {gugudan}')
