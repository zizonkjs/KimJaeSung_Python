# 함수명에 대해서 
# 코드가 있는 부분에 붙여진 이름임.
# 코드가 시작되는 주소를 저장하고있음.

# 내장함수
p = print
p("show")

func=[ max, min, sum ]

datas=[1,3,5]

# 함수명 max min sum 을 리스트에 담아서 원소로 처리
print(func[0](datas), func[1](datas), func[2](datas))
# func 0 번 요소(max)에서 datas 적용
#      1 번 요소(min)
#      2 번 요소(sum)
#  함수이름을 변수에 저장 가능
# 변수가 함수의 기능을 가지게 됨.

# 람다표현식 또는 람다함수
# 1줄 함수이름, 익명 함수
# 형식 : lambda 매개변수:실행코드
names={1:'Kim', 2:'A', 3:'Zoo'}

# 정렬하기 -> 내장함수 sorted() --> List 반환
# key로 정렬
result=sorted(names)
print("오름차순 정렬", result)

#value로 정렬 -> names.tiems() --> (1,'kim'), (2,'Adam'), (3.'Zoo')
result=sorted(names.items(), key=lambda 그냥변수이름:그냥변수이름[1])
print("오름차순 정렬", result)

res=sorted("This is a test string from Andrew".split(), key=str.lower)
print(res)

res=sorted("This is a test string from Andrew".split())
print(res)

# map()와 lambda ------------------------------------------------
data=[11,22,33,44]

# 각 원소의 값에 곱하기 2해서 다시 list로 저장하고싶어
# def multi2(value): return value*2
# data2=list(map(multi2, data))
data2=list(map(lambda a:a*2, data))
print(data2)

print("---------------------------------------")
#람다 표현식 사용하기
# 숫자를 받은 뒤 10을 더해서 반환하는 함수 만들기
def plus_ten(x):
    return x + 10
print((lambda x:x+10)(1))

# 람다 표현식에선 새 변수를 만들 수 없음.
# 변수가 필요한 코드는 def 를 사용해야함.
# 람다 표현식 바깥에 있는 숫자는 사용할 수 있음.
y=10
print((lambda x:x+y)(2))

print(list(map(lambda x:x +30,[2,4,6])))

# 람다 표현식과 map, filter, reduce 함수 활용하기
# 람다 표현식에 조건부 효현식 사용하기
# lambda 매개변수들:식1 if 조건식 else 식2
a=[1,2,3,4,5,6,7,8,9]
print(list(map(lambda x: str(x) if x % 3 == 0 else x, a)))
# 람다 안에선 elif 조건식 사용 할 수 없음.
# elif 사용해야하는 경우는 함수를 정의해서 갔다 쓰는게 편함.
def f(x):
    if x ==1:
        return str(x)
    elif x==2:
        return float(x)
    else:
        return x+10
print(list(map(f,a)))

# map에 객체를 여러개 넣기
a=[1,2,3,4,5]
b=[2,4,6,8,10]
print(list(map(lambda x,y:x*y,a,b)))

# filter 사용하기
# filter 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져오는데
# 지정한 함수의 값이 True 일때만 해당 요소를 가지고옵니다.
# filter(함수, 반복가능한객체)
def g(x):
    return x> 5 and x < 10
a=[8,3,2,10,15,7,1,9,0,11]
print(list(filter(g,a)))

print(list(filter(lambda x: x>5 and x<10,a)))

#reduce 사용하기
# 반복 가능한 객체의 각 요소를 지정된 함수로 처리 한 뒤 이전 결과와 누적해서 반환하는 함수.
from functools import reduce
a=[1,2,3,4,5]
from functools import reduce
print(reduce(lambda x,y:x+y, a))
# 많이는 안씀

#연습문제
files=['font', '1.png', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
print(list(filter(lambda x:x.find('.jpg') != -1 or x.find('.png') !=-1, files)))

