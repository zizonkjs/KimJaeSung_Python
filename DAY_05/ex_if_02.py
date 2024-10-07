#------------------------------------------------
# 조건부표현식
#------------------------------------------------
# 문자 1개 코드값을 저장하는 조건식
# 알파벳(a~z, A~Z) 코드값으로 변환
# 그 외 None으로 변환

alpa=input("문자열 입력 : ")
#result=None 조건부표현식이 아닐때 저장하는법
if 'a'<=alpa<='z' or 'a'<=alpa<='z':
    print(ord(alpa))
    #result=None
else:
    print(None)

결과=(ord(alpa)) if  ('a'<=alpa<='z') or ('A'<=alpa<='Z') else (None)

print(f'{alpa}의 코드값 : {결과}')

