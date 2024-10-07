# for 와 range 사용하기
# for 저장하고 출력할 변수 in range(횟수)
#   반복할 코드
for 저장하고반복시킬변수 in range(10):
    print("재성아 힘내라")

# 반복문에서 변수의 변화 알아보기
for 저장하고반복시킬변수 in range(10):
    print('Hello, word!', 저장하고반복시킬변수)

#for 과 rnage 응용하기
# 시작하는 숫자와 끝나는 숫자 지정하기
for 변수 in range(5,12):
    print('hello, world', 변수)

# 증가폭 사용하기
for 변수 in range(0, 10,2):
    print('hello, world', 변수)

# 숫자를 감소시키기
for 변수 in range(10,0,-1):
    print('hello', 변수)

for 변수 in reversed(range(10)):
    print('hello', 변수)

# 입력한 횟수대로 반복하기
count = int(input('반복시킬 횟수 : '))

for i in range(count):
    print('hello, w', i)


