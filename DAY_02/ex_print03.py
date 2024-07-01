#---------------------------------------------------
# - 내장함수 print()
# - file 매개변수 : 데이터를 file에 기록
#---------------------------------------------------
# 파일 읽기 & 쓰기
# - 파일열기 open()
# - 파일읽기 또는 쓰기
# - 파일닫기 close()
FILENAME='result.txt'

# 파일을 쓰기모드(w) 열기
f=open(FILENAME, mode='w')
# f.write("Hello")
# file에 데이터 출력하기
print("Good Luck", file=f)
f.close()
