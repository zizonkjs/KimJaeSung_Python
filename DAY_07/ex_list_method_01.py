# 리스트 전용 함수(메서드)
# 리스트의 원소/요소를 제어하기 위한 함수
import random as rand

# 임의의 정수 데이터 10개 구성된 list
datas=[10,9,7,3,8,3,5,71,22,3]

# 메서드 요소 인덱스를 반환하는 메서드 index()
# 11의 인덱스를 알고 싶음.
# print(f'11의 인덱스번호 : {datas.index(11)}') # <- 데이터값 넣어주면 찾아줌 왼쪽에서 부터 오른쪽으로 찾아줌

# 데이터 0의 인덱스 찾기 ==> 없는 데이터 값은 error
if 0 in datas:
    print(f'11의 인덱스번호 : {datas.index(0)}')
else: print("0은 없는 데이터입니다.")

# -> 3의 인덱스 찾기
if 3 in datas:
    idx=datas.index(3)
    print(f'첫번째 3의 인덱스 : {idx}')

if 3 in datas:
    idx=datas.index(3,idx+1)
    print(f'두번째 3의 인덱스 : {idx}')

if 3 in datas:
    idx=datas.index(3,idx+1)
    print(f'세번째 3의 인덱스 : {idx}')

#반복문으로도 만들수잇음

# 데이터가 몇개 존재하는지 갯수 파악하는 메서드 count(데이터)
cnt=datas.count(3)
print(f'3의 개수 : {cnt}개')

idx=0
for i in range(cnt):
    idx=datas.index(3, idx if not i else idx+1)
    print(f'{i+1}번째 3의 인덱스 : {idx}')
