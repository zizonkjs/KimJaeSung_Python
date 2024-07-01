#--------------------------------------------------
# Tuple 데이터 자료형 살펴보기
# 내장함수 : len(), max(), min(), sum()
# 연산자 : 덧셈, 곱셈, 멤버연산자(in, not in)
#--------------------------------------------------
nums=11,22,33,44,55

# 내장함수 값이 여러개일 경우에만 사용 가능
print(f'nums  : {len(nums)}개')
print(f'nums  : {max(nums)}최대값')
print(f'nums  : {min(nums)}최소값')
print(f'nums  : {sum(nums)}합계')
print(f'nums  : {sorted(nums)}, {sorted(nums, reverse=True)}개')

# 문자열의 쵀대 값 최소 값은 사용 할 수 있는데 sum은 불가능함(단 숫자일땐 가능함)
# 정렬도 가능함. (단 리스트에 담아서 사용해줘야함.)

print("--------------------------------------------------")

# 연산자
## 덧셈
data1=11,22
data2="A","B","C"
data3=[1,2]

print(data1+data2) # Tuple + Tuple = 한개의 튜플로 만들어줌

print("--------------------------------------------------")

print(data1+tuple(data3)) # Tuple + List = 안됨. 타입이 똑같아야함. 요소들을 같은 클래스로 형변환 해줘야함

print("--------------------------------------------------")

## 곱셈 : Tuple * int 만 가능
print(data1*10)
print(data2*10)

print("--------------------------------------------------")

# member 연산자 in, not in
print(11 in data1)
print("A" in data1)
print(11 not in data1)
print("A" not in data1)
