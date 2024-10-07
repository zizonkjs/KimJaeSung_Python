# ---------------------------------------------
# dict 자료형 살펴보기
# - dict 자료형 전용의 함수메서드(method)
# - 사용법 : 변수명.메서드명()
# ---------------------------------------------
# [dict에서 키만 추출해주는 method : keys()]
p1={ 'name':'홍길동', 'age':20, 'job':'학생'}
result=p1.keys()
print(f'키 추출 : {result}, {type(result)}')
# 대괄호 사용했다고 list type이 아님을 명심해야함. 원소/요소로 접근 할 수 없음(보여주기만함)
# Lsit로 형변환 시킨후 저장해야함. => list(dick_keys타입)
result=list(result)
print(result)

# key 말고 값(value) 출력하고 싶을때
result=p1.values()
print(f'vlaues 추출 : {result}, {type(result)}')

## dict 에서 값/데이터 하나로 묶어서 추출 items()
result=p1.items() # 튜플로 추출
print(f'items 추출 : {result}, {type(result)}')

result=list(result)
print(f'items 추출 : {result[0]}, {type(result[0])}')


