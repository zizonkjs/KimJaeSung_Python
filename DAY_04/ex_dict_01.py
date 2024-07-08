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


