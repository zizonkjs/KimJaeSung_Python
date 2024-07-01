#-------------------------------------------------------
# tuple 데이터 자료형 살펴보기
# 다양한 종류의 여러 개 데이터를 저장하는 타입
# List와 비슷하지만 수정, 삭제 안됨
# 형식 : (data1, data2.....)
#        data1, data2....
#        한개일때도 ,를 붙여줘야함.
#-------------------------------------------------------
# 튜플 데이터 생성 --------------------------------------
datas=()
print(type(datas), datas, len(datas))

datas=(1, 5, 7)
print(type(datas), datas, len(datas))

datas=(1,) # 한개일때 사용법
print(type(datas), datas, len(datas))

datas=1,
print(type(datas), datas, len(datas))

print("----------------------------------------------")

# 튜플 데이터 원소or요소 읽기---------------------------------------
datas=11,22,33,44,55
# 인덱스를 파이썬이 붙여줌.

# 2번요소 읽기
print(datas[2], datas[-3])

# 1,2,3 요소 읽기
print(datas[1:4])

# 요소/원소 수정 및 삭제 즉, 변경 불가, 추가 불가, 읽기만 가능
# 마지막 원소를 'A'로 변경하고싶음. 
# #이럴땐 Tuple를 List 로 형변환 시킨후 다시 Tuple로 형변환 시키면 됨.
birthday=(2024,1,1)

# 월이 1월에서 3월로 변경
birthday=list(birthday)
birthday[1]=3

# list ==> Tuple
birthday=tuple(birthday)
print(birthday)
