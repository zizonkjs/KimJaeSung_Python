# while 문으로 3단을 출력하기
# 단 while 문 사용
dan=3
n=0
while dan==3:
    dan*n
    n=n+1

    print(f'{dan} * {n}= {dan*n}')
    if n>=9: break

cnt=1
while cnt<10:
    print(cnt, f'3 * {cnt} = {3*cnt}')
    cnt=cnt+1

# 1~30 범위의 수 중에서 홀수만 출력
# 단 while문만 사용
# 1부터 30 까지 while문으로 출력
nums=1
cnt=0
while nums<31:
    if nums%2:
        print(nums)
    nums=nums+1
    
nums=1
cnt=0
while nums<31:
    print(nums)
    nums=nums+2
