# 반복문과 continue
# continue 구문을 만나면 구문 아래 코드 실행을 하지 않는다!
# 반복문으로 가서 다음 요소 데이터를 가지고 온다.
# 1~50까지 숫자로 구성된 데이터
# 3의 배수인 경우만 화면에 출력하세요.

data=list(range(1,51))

for d in data:
    if d%3==0:
        print(d)

for d in data:
    if d%3: continue # 조건문이 참이면 continue가 처리하지말고 돌아가라! 다시 for 문으로 돌아감
    print(d)