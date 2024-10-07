# 입력받은 문자가 알파벳인지 검사하기.
# 알파벳이면 코드값 출력하세요.
# 알파벳이 아니면 "잘못된 문자"라고 출력하세요.
print('a'>'A')
print('a'<='c'<='z')

ch=input("문자 한개 입력 : ").strip()
if len(ch)==1:
    if 'a'<=ch<'z':
        print(f'{ch} 코드값은 : {ord(ch)}')
    else:
        print(f'{ch}는 잘못된 문자입니다.')
else:
    print("입력된 값이 없거나 2개이상의 문자를 입력했습니다.")