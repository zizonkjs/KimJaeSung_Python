# 요소 추가 method append(추가데이터)

datas=[1,3,5]

# new data 
datas.append(100) # 추가하면 마지막 원소로 추가
print(f'datas 개수 : {len(datas)}, {datas}')

datas.append(100) # 추가하면 마지막 원소로 또 추가
print(f'datas 개수 : {len(datas)}, {datas}')

# 특정위치에 요소 추가 insert(인덱스 번호, 데이터)
datas.insert(0, 300)
print(f'datas 개수 : {len(datas)}, {datas}')

datas.insert(-1, 300) # 마지막자리에 추가 할땐 -1, 원래 있던 요소는 뒤로 밀림
print(f'datas 개수 : {len(datas)}, {datas}')

# 임의의 숫자 10개 저장하는 리스트 생성
# random
import random

# data=[0,0,0,0,0,0,0,0,0,0]
# idx=0
# while True:
#     num=random.randint(1,100)
#     if num not in data:
#         data[idx] = num
#         idx=idx+1
#     if idx==10: break
# print(data)

# append 써서 빈리스트에 값넣기
data=[]
for cnt in range(10):
    data.append( random.randint(1,100))

print(f'data=> {data}')

# 요소 삭제 메서드 remove(데이터)
# 존재하지 않는 데이터를 넣을시 Error 발생
datas.remove(300)
print(f'datas 개수 : {len(datas)}, {datas}')
for cnt in range(datas.count(300)):
    datas.remove(300)
    print(f'datas 개수 : {len(datas)}, {datas}')

   
