# ------------------------------------------------------
# 반복문 : for, while
# for 요소 in 시퀀스 객체(list, tuple, dict, set, str, range)
#---------------------------------------------------------------
#반복문 for
# 시퀀스 데이터에서 원소/요소를 하나씩 읽어 올때 사용
# for 변수명 in (list,tuple,dict,set,str,range):
#   반복할 코드
# 문자열에서 문자를 1줄에 1개씩 출력하기
msg="Merry christmas 2025"
print(len(msg))

for 변수명 in msg:
    print(변수명, ord(변수명))
print(type(변수명))

# str 타입의 원소를 가지는 리스트
# 해당 원소를 정수로 형변환 시켜서 저장
# 원래 원소의 값을 변경해야 하는 경우는 인덱스 필요!!
# 원소 개수 ===> 인덱스 범위
data=['4', '9', '2', '1', '7', '8']

print('[전]', data)
for d in data:
    d=int(d)

# 리스트의 인덱스 가져오기.
for idx in range(len(data)):
    print(f'idx => {idx}')
    data[idx]=int(data[idx])

print('[후]', data)
