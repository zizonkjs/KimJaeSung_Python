# 메시지 입력 받기.
# 알파벳 대문자인 경우 소문자로 변경, 소문자인 경우 대문자로 변경하기 chr(정수), ord(알파벳)
# 나머지는 그대로 출력을 하세요.

msg=input("알파벳 입력 : ")


for a in msg:
    if 'A'<=a<='Z':
        print(chr(ord(a)+32), end='')
    elif 'a'<=a<='z':
        print(chr(ord(a)-32), end='')
    else:
        print(a, end='')

var_bytes=b'abcdedf'
print(var_bytes)

for i in var_bytes:
    print(i)
    
                