


# for문의 실행결과를 예측하라.
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)
# 사과
#귤
#수박
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print('######') # 저장된 데이터 개수만큼 반복한다. 그래서 3번 출력된다.
# ######
# ######
# ######

#for 문과 동일한 기능을 수행하는 코드를 작성
for 변수 in ["A", "B", "C"]:
    print(변수)
print("A")
print("B")
print("c")

# for 문을 풀어서 동일한 동작을 하는 코드르 작성하라.
for 변수 in ['a', 'b', 'c']:
    print('출력 : ', 변수)
print('출력 : ', 'a')
print('출력 : ', 'b')
print('출력 : ', 'c')

# for 문을 풀어서 동일한 동작을 하는 코드를 작성하라.
for 변수 in ['a', 'b', 'c']:
    b = 변수.upper()
    print('변환:', b)

#다음 코드를 for문으로 작성하라.
# 변수 = 10
# print(변수)
# 변수 = 20
# print(변수)
# 변수 = 30
# print(변수)
변수=[10,20,30]
for a in [10,20,30]:
    print(a)

# 다음 코드를 for문으로 작성하라.

# print(10)
# print("-------")
# print(20)
# print("-------")
# print(30)
# print("-------")

for a in [10,20,30]:
    print(a)
    print("-------------")

print("+++++++")
for a in [10,20,30]:
    print(a)

# 다음 코드를 for문으로 작성하라.

# print("-------")
# print("-------")
# print("-------")
# print("-------")
for a in [1,2,3,4]:
    print("-----------------")

# 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력하라. 단 부가세는 10원으로 가정한다.

리스트 = [100, 200, 300]
# 110
# 210
# 310

for a in 리스트:
    print(a+10)

for a in ['김밥', '라면', '튀김']:
    print(f'오늘의 메뉴 :{a}')

리스트 = ["SK하이닉스", "삼성전자", "LG전자"]

for a in 리스트:
    print(len(a))

리스트 = ['dog', 'cat', 'parrot']
for b in 리스트:
    print(f'{b}의 글자길이 : {len(b)}')

for c in 리스트:
    print(f'{c}의 첫글자 : {c[0]}')

리스트 = [1, 2, 3]
for d in 리스트:
    print(f'{3} x {d} = {3*d}')

리스트 = ["가", "나", "다", "라"]
for e in 리스트[1:]:
    print(e)
    
print("------------------------------------")
리스트 = ["가", "나", "다", "라"]

for a in range(len(리스트)):
    # print(리스트[a])
    if a==0 or a==2:
        print(리스트[a])
print("------------------------------------")

리스트 = ["가", "나", "다", "라"]
for idxb in range((len(리스트))):
   print(리스트[3-idxb])

for 변수 in 리스트[: :-1]:
  print(변수)
print("------------------------------------")

리스트 = [3, -20, -3, 44]

for a in 리스트:
    if a<0:
        print(a)
print("------------------------------------")

리스트 = [3, 100, 23, 44]
for a in 리스트:
    if a%3==0:
        print(a)

print("------------------------------------")

msg = ["I", "study", "python", "language", "!"]

for b in range(len(msg)):
    if len(msg[b])>=3:
        print(msg[b])

msg= ["A", "b", "c", "D"]
for b in msg:
    if b.isupper()==True:
        print(b)

msg2= ["A", "b", "c", "D"]
for c in msg2:
    if c.islower()==True:
        print(c)

domul=['dog', 'cat', 'parrot']

for a in domul:
    print(a.capitalize())

files=['hello.py', 'ex01.py', 'intro.hwp']

for a in files:
    print(a.split('.')[1])

files2=['intra.h', 'intra.c', 'define.h', 'run.py']

for b in files2:
    if '.h' in b:
        print(b)
print("-----------------------------------------")
for a in files2:
    if '.c' in a or '.h' in a:
        print(a)

# for a in range(1,100):
#     print(a)

# for c in range(2002,2051):
#     if c%4==0:
#         print(c)
print("-----------------------------------------")
for x in range(2002, 2051, 4):
    print(x)

for z in range(1,31):
    if z%3==0:
        print(z)

for a in range(99,0,-1):
    print(a)

for a in range(10):
    print(a/10)

for b in range(1,10):
    print(f'3단 : {3} * {b} = {3*b}')

for b in range(1,10):
    if (3*b)%2==1:
        print(f'3단 : {3} * {b} = {3*b}')

hab=0
for a in range(1,10):
    hab +=a
    print(f"합 :{hab}")

hab2=0
for b in range(1,10):
    if b%2==1:
        hab2 +=b
        print(f'합 : {hab2}')

hab=1
for a in range(1,10):
    hab *=a
    print(f"합 :{hab}")

price_list = [32100, 32150, 32000, 32500]
for a in range(len(price_list)):
    print(price_list[a])

price_list = [32100, 32150, 32000, 32500]
for a in range(len(price_list)):
    print(a, price_list[a])

print("----------------------------------------------")

price_list = [32100, 32150, 32000, 32500]
for a in range(len(price_list)):
    print(3-a, price_list[3-a])

price_list = [32100, 32150, 32000, 32500]

for a in range(1,4):
    print(90+10*a, price_list[a])

my_list = ["가", "나", "다", "라"]

# for a in my_list[:3]:
#     print(a, my_list[1:)
for i in [0,1,2]:
    print(my_list[i], my_list[i+1])

my_list = ["가", "나", "다", "라", "마"]
print(my_list[0], my_list[1], my_list[2])
print(my_list[1], my_list[2], my_list[3])
print(my_list[2], my_list[3], my_list[4])
print("-------------------------------------------")
for i in [0,1,2]:
    print(my_list[i], my_list[i+1], my_list[i+2])
print("-------------------------------------------")
my_list = ["가", "나", "다", "라"]

for i in (3, 2):
    print(my_list[i], my_list[i-1])
print(my_list[1], my_list[0])



my_list = [100, 200, 400, 800]

# 200 idx [1] - 100[0] print
# 400[2] - 200[1] print
# 800[3] - 400[2] print
# range(4)
for n in range(0,3):
    print(my_list[n+1]-my_list[n])

for n in range(len(my_list)-1):
    print(my_list[n+1]-my_list[n])
print()
my_list = [100, 200, 400, 800, 1000, 1300]
# 첫째줄 : 0 1 2 의 평균 print
# 둘째줄 : 1 2 3 의 평균 print
# 셋째줄 : 2 3 4 print
#         3 4 5 print
for i in range(4):
    print((my_list[i]+my_list[i+1]+my_list[i+2])/3)

l  = [100, 200, 400, 800, 1000]
h = [150, 300, 430, 880, 1000]
# 고가 - 저가 = 변동폭
# h1-l1 = 값저장
# h2-l2
# h4-l4 = 값저장
# 변동폭 값을 리스트에 저장
data=[]
for i in range(5):
    data.append(h[i]-l[i])

print(data)

# [101호 102호] print
# [201, 202] print
# [301 302] print
hosu=[['101호', '102호'], ['201호', '202호'], ['301호', '302호']]
print(hosu)

sotck={'10/10':[80,110,70,90], '10/11':[210,230,190,200]}
print(sotck)

apart = [ [101, 102], [201, 202], [301, 302] ]
for a in apart:
    for b in a:
        print(b, '호')
print()
apart = [ [101, 102], [201, 202], [301, 302] ]


for a in reversed(apart):
    for b in a:
        print(b, '호')
print()
for a in apart[::-1]:
    # [301, 302] 1.얘읽고
    # [202, 201] 2.얘읽고
    # [102, 101] 3.얘읽고
    for b in a[::-1]:
        print(b, '호')
print()
apart = [ [101, 102], [201, 202], [301, 302] ]
for a in apart:
    for b in a:
        print(b, '호')
        print('-----')
print()
apart = [ [101, 102], [201, 202], [301, 302] ]
for a in apart:
    
    for b in range(2):
        print(a[b], '호')
        if a[b]%2==0:
            print("----")
print()
for a in apart:
    for b in a:
        print(b, "호")
    print("-----")

print()

for a in apart:
    
    for b in range(2):
        print(a[b], '호')
        if a[b]==302:
            print("----") 

print()
for row in apart:
    for col in row:
        print(col, "호")
print("-" * 5)

print("-----------------------------")

data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

res=[]
for a in data:
    for b in a:
        res.append(b*1.00014)
print(res)
print()

result = []
for line in data: # data 요소 하나하나 line으로 뽑게하고
    sub = []    # 저장할 변수 지정
    for column in line: # 뽑은 요소를 또 변수지정해서 하나씩 반복
        sub.append(column * 1.00014) # 반복하면서 그 값 column에 1.00014 곱해주고. sub 빈 리스트에 appeend로 저장
    result.append(sub) # sub에서 만들어진 리스트들을 append 해서 result에 또 저장.
print(result)

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for a in ohlc[1:]:
    for b in range(1):
        print(a[b+3])
print()
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for a in ohlc[1:]:
    for b in range(1):
        if a[b+3]>150:
            print(a[b+3])
print()
for a in ohlc[1:]:
    for b in range(1):
        if a[b+3]>=a[b]:
            print(a[b+3])

v=[]
for a in ohlc[1:]:
    for b in range(1):
        v.append(a[b+1]-a[b+2])

print(v)
v=[]
for a in ohlc[3]:
    v.append(a)
print(v[3]-v[0])
print()
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
v=[]
for a in ohlc[1:]:
    for b in range(1):
        v.append(a[b]-a[b+3])
print(f'총수익 계산: {sum(v)}')

print()
profit = 0
for row in ohlc[1:]:
    profit += (row[3] - row[0])
print(profit)



        



        



    
    
