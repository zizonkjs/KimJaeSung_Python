# ------------------------------
# dict 연산자와 내장함수
#-------------------------------
p1={ 'name':'홍길동', 'age':20, 'job':'학생'}
dog={"품종":"골든리트리버", "무게":"10kg", "색상":"베이지색", "성별":"수컷", "나이":"5살"}
jumsu={'국어':80, '수학':78, '체육':100}

# 연산자
# 산술연산, 비교연산 안됨
# member 연산자는 가능 : in, not in
print('name' in dog)
print('name' in p1)

# value, dict type에서는 value 값을 확인할 수 없음.
print('골든리트리버' in dog)
print('5살' in dog)

# value를 추출해야 볼 수 있음.
print('골든리트리버' in dog.values())
print('5살' in dog.values())

# 내장함수
# 원소/요소 개수 확인 : len()
print(f'p1의 개수 : {len(p1)}')
print(f'p1의 개수 : {len(dog)}')

# 정렬 관련 sorted() : 사용시 key만 list정렬.
print(f'p1의 정렬 : {sorted(p1)}')
print(f'p1의 정렬 : {sorted(dog,)}')

print(f'p1의 내림차순정렬 : {sorted(p1, reverse=True)}')
print(f'dog의 내림차순정렬 : {sorted(dog, reverse=True)}')

print(f'jumsu 의 값 오름차순정렬 : {sorted(jumsu.values())}')
print(f'jumsu 의 내림차순정렬 : {sorted(jumsu, reverse=True)}')

print(f'jumsu 의 값 오름차순 items 정렬 : {sorted(jumsu.items())}')
print(f'jumsu 의 값 오름차순 items 정렬 : {sorted(jumsu.items(), key=lambda x:x[1])}')
                                                            # x(국어, 점수):x(국어, 점수)에서 [1번] 원소 기준으로 정렬

# value를 정렬 하고 싶을 때, sorted는 str와 int가 섞여 있으면 즉 type이 달라서 정렬 불가능함.
# 즉 동일한 type에서만 정렬이 가능함.


