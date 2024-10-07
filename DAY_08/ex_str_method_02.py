# 문자열에서 좌우 여백 제거 메서드 -> strip(양쪽제거), lstrip(왼쪽만제거), rstrip(오른쪽만제거)
# 문자열 내부의 공백은 제거하지 않음. ex) 'HEllo hello'
msg="Good Luck"
data="              Happy New Year 2025!                     "

# 좌우 모든 공백 제거---------------------------------------------
m1=msg.strip()
print(f'원본 msg : {len(msg)}개 ---제거 m1 : {len(m1)}개') # 문자열 사이의 공백만 있어서 같음

m2=data.strip()
print(f'원본 data : {len(data)}개 ---제거 m2 : {len(m2)}개')

#왼쪽 부분 공백 제거
m3=data.lstrip()
print(f'원본 data : {len(data)}개 ---제거 m3 : {len(m3)}개')

m4=data.rstrip()
print(f'원본 data : {len(data)}개 ---제거 m4 : {len(m4)}개')

# 이름을 입력 받아서 저장하세요.
# input()함수
# name=input("이름 : ").strip()
# if len(name)>0:
#     print(f'name : {name}')
# else: print("입력을 다시하세요.")

# 입력 받은 데이터에 따라 출력을 다르게 합니다.
# input() 함수 사용
# [조건] 알파벳이면 '별', 숫자면 '하트' 나머지는 무시 ==> if
data=input("알파벳 또는 숫자 문자 1개 입력 :").strip()
if 'a'<=data<='z' or 'A'<=data<='Z':
    print("별")
elif '0'<=data<='9':
    print('하트')
else:
    print("흥!")

