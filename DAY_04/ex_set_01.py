# -------------------------------------
# set 자료형 살펴보기
# 여러가지 종류의 여러 개 데이터를 저장
# 특징 : 중복된 데이터 값은 불가능
# Colletion 타입의 데이터 저장시 tuple만 가능, List 사용 불가능.
# 형태 : {데이터1, 데이터2, 데이터n....}
#--------------------------------------------------------------------
# set 생성
data=[] # list
data=() # tuple
data={} # dict
data=set() # set

print(f'data의 type : {type(data)}, 원소/요소 갯수 : {len(data)}개, 데이터 : {data}')

# 여러개 데이터 저장한 set
data={10,20,30,40,50,60,-1,-5,-6}
print(f'data의 type : {type(data)}, 원소/요소 갯수 : {len(data)}개, 데이터 : {data}')

data={10,20,30,40,50,60,-1,-5,-6,9.34,"aplle", True, False}
print(f'data의 type : {type(data)}, 원소/요소 갯수 : {len(data)}개, 데이터 : {data}')

# data={1,2,3,[1,2,3]} list[]는 안됨!
# print(f'data의 type : {type(data)}, 원소/요소 갯수 : {len(data)}개, 데이터 : {data}')

data={1,2,3,(1,)} # Tuple()은 됨! 중복은 저장하지 않음. 중복된 데이터를 제거 하고 출력할 때 사용.
print(f'data의 type : {type(data)}, 원소/요소 갯수 : {len(data)}개, 데이터 : {data}')

# data2={1,2,3, {1:100}} # dict 안됨!
# print(f'data의 type : {type(data2)}, 원소/요소 갯수 : {len(data2)}개, 데이터 : {data2}')

# set() 내장함수
data={1,2,3} # =====> set([1,2,3]) -> because 생성자 함수.(데이터를 넣어주는 역할)
data=set()
data=set({1,2,3})

# list, str, dict, tuple를 set으로 형변환 시켜줄때
data=set([1,2,3,4]) # list를 set으로 저장할 때
print(data)
data=set("Good") # o가 중복되서 하나만 출력됨
print(data)
data=set({"이름":"김재성", "나이":"28살", "이름":"홍길동"}) # dict도 set()쓰면 가능. 중복될경우, 뒤에 있는 요소를 앞에거에 덮어씀.
print(data)
data=set((1,2,1,2,1,2)) # Tuple 사용시 중복된 값은 덮어 씌워서 출력함.
print(data)

print("-"*30)
#--------------------------------------------------------------------
# set 데이터 타입에 추가하거나 꺼낼땐 전용 method 사용해야 함.
# set 자료형 살펴보기
# 연산자
#--------------------------------------------------------------------
d1={1,3,5,7}
d2={2,4,6,8,3,5,7}

# 덧셈연산 ==> method 사용을 해야함.
# print(d1+d2), 합집합 무조건 중복은 제거함.
print(d1.union(d2), d1|d2)

# 공통 원소 ==> 교집합, 2가지 set에 모두 존재하는 값 출력.
print(d1.intersection(d2), d1&d2)

# 차집합 ==> 공통된 원소를 제외한 나머지 출력.
print(d2.difference(d1), d2-d1)
print(d1.difference(d2), d1-d2)