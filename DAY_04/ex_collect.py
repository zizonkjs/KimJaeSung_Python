#------------------------------------------
# Collection 자료형에 공통적인 부분 살펴보기
#------------------------------------------
# 여러개의 변수에 데이터 저장
name='홍길동'
age='12살'
job='의적'
gender='남'
# 변수명 = tuple type <-패킹 방식
data= '홍','12','의적','남'

# 변1,변2,...,변n = tuple <- 언패킹 방식
name,age,job,gender='홍길동','12살','의적','남'
print(name,age,job,gender)
# name,age='홍길동','12살','의적','남' -> 변수명과 데이터가 동일해야함.

name,age,_,_='홍','11살','의사','여' # -> 변수명 대신 _ 사용하면 안쓸 수 있음.
print(name, age, _,_) # 마지막의 값이 들어옴.

# tuple 이나 list해서 사용하면됨.
jumsu=[100,90]
kor,math= [100,90]
print(jumsu, kor, math)

#dict 사용시.
per={'name':'박', 'age':11}
k1,k2={'name':'박', 'age':11}
print(per,k1,k2)

# 생성자(constructer) 함수 : 타입명과 동일한 이름의 함수
# int(), float(), str(), bool(), list(), tuple(), dict(), set()
# map(), range()
# 기본 데이터 타입
num=int(10)         # num=10
fnum=float(10.0)    # fnum=10.2
masg=str("good")    # msg="good"
isok=bool(True)     # isok=False

# 컬렉션 type
lnums=list([1,2,3,4]) # nums=[1,2,3,4]
tnums=tuple((3,6,9))  # tnums=(3,6,9)
dicts=dict(d1=10, d2=30) # dicts={'d1:10', 'd2':30}
ss=set({1,1,3,3,5})   # ss={1,1,3,3,5}
print(lnums, tnums, dicts, ss)

# 타입변경=형변환 ---------------------------------------------
# dict 자료형은 다른 자료형과 달리 데이터 형태가 다름.
# 데이터 형태 : key:value
# dict(key=value, key2=value2,...keyn=valuen) : 이때 key는 숫자 안되고 문자열만 가능. 대신에 Value에서 문자열 입력시 "",'' 반드시 사용.
ds=dict(name=1, age=2, gender="남") # key에는 "",'' 사용하면 안됨
print(ds)

ds=dict([('name', '마징가'), ('age', 12)]) # list 안에 tuple 사용시 문자열 가능 (key,vlaue) 
print(ds)

ds=dict([['name', '마징가'], ['age', 12]]) # list 안에 lsit 사용시 문자열 가능 (key,vlaue) 
print(ds)

# 내장함수 : zip() : 같은 index 원소/요소를 서로 묶어줌.
l1=['name', 'age', 'gender']
l2=['마징', 12, '남']
l3=[False,True,True]
print(list(zip(l1,l2,l3))) # list로 형변환 해줘야함. list type
print(tuple(zip(l1,l2,l3))) # tuple로 형변환 해줘야함. tuple type

ds=dict(zip(l1,l2))
print(ds) # dict type