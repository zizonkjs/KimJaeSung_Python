# 반복문
# 출력하고 싶은 단을 입력받아서 해당단의 구구단을 출력.
# 출력예시 2*1=2 ~ 9*9=81 까지
dan=3
nums=[1,2,3,4,5,6,7,8,9]
for n in nums: # for n(한개씩 저장) in nums
    print(f'{dan} * {n} = {dan*n}')

# for문을 사용하려면 저장된 변수가 필요함.
a=['1', '2']
for n in a:
    print(int(n))

for n in range(1,10):
    gugudan=dan*n