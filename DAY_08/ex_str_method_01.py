#--------------------------------------------------------------
# str 데이터 타입 전용 함수, 메서드 살펴보기
#--------------------------------------------------------------
msg='Hello 0705'

#[원소/요소 인덱스 찾기 메서드 - find(문자1개 or 문자열)]
# "H"의 인덱스
idx=msg.find('H')
print(f'H의 인덱스번호 : {idx}')

idx=msg.find('7')
print(f'7의 인덱스번호 : {idx}')

idx=msg.find('llo')
print(f'llo의 인덱스번호 : {idx}') # ==> llo의 시작 위치 번호 값이 2가 나왔음

idx=msg.find('llO') # -> 대소문자 일치하지 않거나 존재하지 않으면 -1출력.
print(f'llO의 인덱스번호 : {idx}')


# [원소/요소 인덱스 찾기 메서드 - index(문자 1개 or 문자열)
# H의 인덱스
idx=msg.index('H')
print(f'H의 인덱스번호 : {idx}')

#h의 인덱스 : 없으면 Error 발생
if 'h' in msg:
    idx=msg.index('h')
    print(f'h의 인덱스 : {idx}')
else:
    print('없는 문자입니다.')


#-------------------------------------------------------------------------
# 문자열의 동일한 문자가 여러개 존재하는 경우.
#-------------------------------------------------------------------------
msg="Good Luck Good"
# 알파벳 o의 인덱스 찾기 => 첫번째 'o' 인덱스
# idx=msg.find('o')
# print(idx)

# idx=msg.find('o', idx+1)
# print(f'2번째 o의 인덱스 :  {idx}')

# idx=msg.find('o', idx+1)
# print(f'2번째 o의 인덱스 :  {idx}')

# idx=msg.find('o', idx+1)
# print(f'3번째 o의 인덱스 :  {idx}')
# -> for 문으로 변경
cnt=msg.count('o')
print(f'cnt=>{cnt}')
idx=-1
for n in range(cnt):
    idx=msg.find('o', idx+1)
    print(f'{n+1}번째 o의 인덱스 : {idx}')

#--------------------------------------------------------------------
# 문자열의 뒷부분부터 찾기 -> rfind(), rindex()
#--------------------------------------------------------------------
msg="Happy"

# y index 찾기
idx=msg.rfind('y')
print(f'y의 인덱스 : {idx}')

# 첫번째 p index 찾기
idx=msg.rfind('p')
print(f'p의 인덱스 : {idx}')

# 두번째 p index 찾기 
# rfnid(문자, 시작인덱스, 끝인덱스+1) 
#               시작인덱스<=찾을str<=끝인덱스
idx=msg.rfind('p', 0, idx) #0은 시작 인덱스 그니까 0번부터 idx사이에서 찾아라
print(f'p의 인덱스 : {idx}')

# 파일명에서 확장자 txt, jpg, xlsx, zip, gz 찾기
# file 명이 'Hello.txt', 2024년상반기경제분석.doc
files=['Hello.txt', '2024년상반기경제분석.doc', 'kakao_123456780.jpg']
# 확장자만 출력해주세요.
# 일단 여러개라고 하면 반복문 사용
# 확장자마다 앞쪽에 점이 있으니까 점을 기준으로 앞에건 파일명, 뒤에껀 확장자

for file in files:
    dot_idx=file.find('.')
    print(file[dot_idx:])
# idx=files[:].find('.') 일단 이렇게 쓰면 안됨.
# if '.' in files: 굳이 if 를 쓸필요 없는 상황이였음. 검사할게 없잖아. 
# 그리고 if 는 참 거짓 기준으로 밖에 할 수 있는게 없음. 여러개를 검사해서 출력할땐 for 문 먼저쓰고 if문을 써야함.
#     idx=files.find('.')
#     print(files[:][idx:])









