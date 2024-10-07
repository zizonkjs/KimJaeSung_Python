# 리스트 전용 함수(메서드)
# 리스트의 원소/요소를 제어하기 위한 함수
# 요소 순서 제어 메서드 reverse()
import random as rad
rad.seed(10) # 동일한 random 숫자 추출을 위한 기준점.
data=[]
for cnt in range(10):
    data.append( rad.randint(1,30))

print(f'{len(data)}=> {data}')

# 0번을 -1으로 보내고 -1번을 0번으로 보내기.
data.reverse()
print(f'{len(data)}=> {data}')

# 요소의 크기를 비교해서 정렬 해주는 메서드. sort()
# 오름차순으로 정렬 sort
data.sort()
print(f'{len(data)}=> {data}')

# 내림차순으로 정렬 
data.sort(reverse=True)
print(f'{len(data)}=> {data}')

#--------------------------------------------------------------------------------
# 리스트에서 요소를 꺼내는 메서드 pop()
# list에서 삭제!
val=data.pop() # data의 마지막 요소를 꺼내서 새로운 변수에 저장한 상황
print(f'value : {val} - {len(data)}=> {data}')

val=data.pop(0) # data의 0번 요소를 꺼내서 새로운 변수에 저장한 상황 예) pop(1), pop(2) ...
print(f'value : {val} - {len(data)}=> {data}')

#--------------------------------------------------------------------------------
# 리스트를 확장 시켜주는 메서드 extend()
data.extend([11,22,33]) # list
print(f'{len(data)}=> {data}')

data.extend((555,777)) # tuple
print(f'{len(data)}=> {data}')

data.extend("good LUCK") # str
print(f'{len(data)}=> {data}')
 
data.extend({555,777,555,777}) # set
print(f'{len(data)}=> {data}')

data.extend({'홍':"홍길", 'age':12}) # key 값만 들어감
print(f'{len(data)}=> {data}')

# 모든 원소 삭제 메서드 clear()
data.clear()
print(f'{len(data)}=> {data}')