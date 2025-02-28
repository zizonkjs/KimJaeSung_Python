# ------------------------------------------------
# dict 자료형 살펴보기
# - 데이터의 의미를 함께 저장하는 자료형
# - 형태 : {key:data}
# ex) {key1:값1, key2:값1}
# key는 중복 할 수 없음. 값은 가능.
# 데이터 분석 시 파일 데이터 가져올 때 많이 사용. 데이터 저장에도 많이 사용.
# ------------------------------------------------------------------------
## {Dict 생성}
data={} # 비어있는 dict
print(f'data 의 원소요소 : {len(data)}개, {data}')

#인물 정보 : 이름, 나이, 성별
data={'name':'박효신', 'age':35, 'gender':'남자'}
print(f'data 의 원소요소 : {len(data)}개, {type(data)}, {data}')

# 강아지 정보 : 품종, 무게, 색상, 성별, 나이
강아지정보={"품종":"골든리트리버", "무게":"10kg", "색상":"베이지색", "성별":"수컷", "나이":"5살"}
print(f'data 의 원소요소 : {len(강아지정보)}개, {type(강아지정보)}, {강아지정보}')
#데이터는 한글 써도 되는데, 파일명이나, 다른 언어에서는 영어를 권장

# 색상출력
print(f'색상 : {강아지정보["색상"]}')

# 성별 품종 출력
print(f'성별 : {강아지정보["성별"]}')
print(f'품종 : {강아지정보["품종"]}')

# [dict 원소/요소 변경] ----------------------------------
# - 변수명[키] = 새로운 값
# 나이 5살 ==>6살
강아지정보["나이"]= "6살"
print(강아지정보)

# 몸무게 증가 10kg => 11kg
강아지정보["무게"]="11kg"
print(강아지정보)

#[dict 원소/요소 삭제]
del 강아지정보["색상"]
print(강아지정보)

#[dict 원소/요소 추가됨.list[추가안됨]] : 안되는 이유는 인덱스에 번호를 지정해주기 때문임. (추가는 안되지만 다른리스트랑 합칠수 있음.)
## 변수명[새로운 키]=값 ---------------------------------
## 이름 추가 : 인덱스 번호로 값이 지정되는것이 아니기 때문에 얼마든지 추가/삭제 가능
강아지정보["이름"]="뽀삐"
print(강아지정보)
# 같은 "key"이름이 있을 경우, 값을 갱신시켜버림. 만약 "key"가 없으면 추가.