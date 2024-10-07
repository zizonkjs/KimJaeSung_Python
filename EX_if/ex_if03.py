# 파일명을 확장자까지 입력 받아서 확인 가능한 파일인지 검사하기.
# 파일의 종류 : jpg, png, txt
# 존재할시 : "확인 가능함!"
# 존재하지 않을 시 : "확인불가능한 파일입니다."

files=['jpg', 'png', 'txt']
filename=input("파일명을 입력(예 : a.txt) : ")

if filename[-3:] in files:
    print("확인 가능함!")
else:
    print("확인불가능한 파일!")
