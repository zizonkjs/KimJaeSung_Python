#----------------------------------------------------------
# 실습1 글자를 입력
#       입력받은 글자코드값(a~z, A~Z)을 출력
#----------------------------------------------------------

gal=input("글자를 입력 : ")

# if len(gal)>0:
#     if len(gal)==1:
#         if 'z'>=gal>='a':
#             print(f'{gal}의 코드값 : {ord(gal)}')
#         elif 'Z'>=gal>="A":
#             print(f'{gal}의 코드값 : {ord(gal)}')
#         else:
#             print("a~z, A~Z 값만 입력하세요.")
#     else:
#         print("1개 문자만 입력하세요.")
# else:
#     print("입력된 데이터가 없어요.")

if len(gal)>0 and ('z'>=gal>='a' or 'Z'>=gal>="A"):
    gal=list(map(ord, gal))
    print(f'코드값:{gal}')
else:
    print("1개의 알파벳만 입력하세요. 아니면 입력된 데이터 확인하세요.")

data="ab"
list(map(ord, data))
# ord(data[0])
# ord(data[1])

# 점수를 입력 받은 후 학점을 출력
# A+, A, A-, B+,B,B-,c+,c,c-,D+,D,D-, F

step=["A+", "A", "A-", "B+", "B" , "B-", "C+" , "C" , "C-", "D+" , "D", "D-", "F"]
jumsu=int(input("당신의 점수를 입력 :"))

if jumsu>100 or jumsu<0:
    print(f"{jumsu}은 잘못된 점수입력입니다.")
elif jumsu<=100:
    if 100>=jumsu>=96: print(f'{step[0]} 입니다.')
    elif jumsu>=90: print(f'{step[1]}, 입니다.')
    elif jumsu>=85: print(f'{step[2]}, 입니다.')
    elif jumsu>=80: print(f'{step[3]}, 입니다.')
    elif jumsu>=75: print(f'{step[4]}, 입니다.')
    elif jumsu>=70: print(f'{step[5]}, 입니다.')
    elif jumsu>=65: print(f'{step[6]}, 입니다.')
    elif jumsu>=60: print(f'{step[7]}, 입니다.')
    elif jumsu>=55: print(f'{step[8]}, 입니다.')
    elif jumsu>=50: print(f'{step[9]}, 입니다.')
    elif jumsu>=45: print(f'{step[10]}, 입니다.')
    elif jumsu>=40: print(f'{step[11]}, 입니다.')
    else:
        print(f'{step[12]}, 입니다.')

# grade=""
# jumsu=int(input("점수입력 : "))
# if jumsu>100 or jumsu<0:
#    print(f"{jumsu}은 잘못된 점수입력입니다.")    
# elif jumsu>100 or jumsu<0:
# elif jumsu>=n : grade="A"
# .....  ""     : grade="F"
# print(f'{jumsu}는 {grade} 입니다.)

