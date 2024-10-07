# # 연습 문제 : 파일 경로에서 파일명만 가져오기
# path=r'C:\\User\\dojang\\appdata\\local\\programs\\python\\python36-32\\python.exe'.split('\\')
# print(path[-1])

# # 심사문제: 특정 단어 개수 세기
# msg='''When Python 2.7 was still supported, a lot of functionality in Python 3 was kept for backward compatibility with Python 2.7. With the end of Python 2 support, these backward compatibility layers have been removed, or will be removed soon. Most of them emitted a DeprecationWarning warning for several years. For example, using collections.Mapping instead of collections.abc.Mapping emits a DeprecationWarning since Python 3.3, released in 2012.
# Test your application with the -W default command-line option to see DeprecationWarning and PendingDeprecationWarning, or even with -W error to treat them as errors. Warnings Filter can be used to ignore warnings from third-party code.
# Python 3.9 is the last version providing those Python 2 backward compatibility layers, to give more time to Python projects maintainers to organize the removal of the Python 2 support and add support for Python 3.9.
# Aliases to Abstract Base Classes in the collections module, like collections.Mapping alias to collections.abc.Mapping, are kept for one last release for backward compatibility. They will be removed from Python 3.10.
# More generally, try to run your tests in the Python Development Mode which helps to prepare your code to make it compatible with the next Python version.
# Note: a number of pre-existing deprecations were removed in this version of Python as well. Consult the Removed section.'''

# if 'the' in msg:
#     더=msg.count('the')
#     print(더)
# elif 'them' in msg or 'there' in msg or 'their' in msg:
#     pass

# #심사문제 : 높은 가격순으로 출력하기
# #1. msg 안에 정수만 있는지 검사
# #2. 빈문자열 9개 있어야함
# #3. 천단위마다 , 가 들어가야함
# #sort() 사용 -> int로 저장시켜야함

# data='51900;158000;367500;250000;59200;128500;1304000'


# # 29장
# # 연습문제 : 몫과 나머지를 구하는 함수 만들기
# # x를 y로 나누었을 때 몫과 나머지가 출력

# x = 10
# y= 3
# def moxna(a,b):
#     return a // b, a%b



# #심사문제 : 사칙연산 함수 만들기
# # 숫자 2개 입력
# def 덧셈(num1, num2):
    
#     return num1+num2


# def 뺄셈(num1, num2):
   
#     return num1-num2


# def 나눗셈(num1, num2):
    
#     return num1/num2 if num2 else '0으로 나눌 수 없음.'


# def 곱셈(num1, num2):
    
#     return num1*num2



# user=input("연산자, 숫자1, 숫자2 :").split(',')
# if '+' in  user:
#     덧셈(int(user[1]),int(user[2]))
#     print(f'덧셈결과 : { 덧셈(int(user[1]),int(user[2]))}')
# elif '-' in user:
#     뺄셈(int(user[1]),int(user[2]))
#     print(f'뺄셈결과 : { 뺄셈(int(user[1]),int(user[2]))}')
# elif '/' in user:
#     나눗셈(int(user[1]),int(user[2]))
#     print(f'나눗셈결과 : { 나눗셈(int(user[1]),int(user[2]))}')
#     if int(user[2])==0:
#         print("0으로 나눌수 없음")
# elif '*' in user:
#     곱셈(int(user[1]),int(user[2]))
#     print(f'곱셈결과 : { 곱셈(int(user[1]),int(user[2]))}')
# else:
#     print("잘못된 데이터 +,정수,정수 로 입력하세요. \',\'도 넣으세요.")

# 30장
# 연습문제 : 가장 높은 점수를 구하는 함수 만들기
# kor, eng, math, sci= 100, 86, 81, 91

# def maxscore(*hakgo):
#     return max(*hakgo)

# print(maxscore(kor, eng, math, sci))
        

# 심사문제 : 가장 낮은 점수, 높은 점수와 평균 점수 구하는 함수 만들기

def minscore(*num):
    return min(*num)
print(minscore(10,20,30,40,50))

def highsocre(*num):
    return max(*num)
print(highsocre(10,20,30,40,50))

def aver(*nums):
    total=0
    for n in nums:
        total += n
    return total

socre=list(map(int, input("숫자 4개 입력 (예 : 10,20,30,40) : ").split(',')))




