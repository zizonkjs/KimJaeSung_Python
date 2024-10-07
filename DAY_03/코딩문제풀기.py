# 001 print 기초
print("Hello world")

# 002 print 기초
print('marys cosmetics')

# 003
print("신씨가 소리질렀다.")
print("도둑이얌")

#004
print("C:\\Windows")

#005
print("안녕하세요.\n만나서\t\t반갑습니다.")
# \n은 줄바꿈, \t tap 만큼 띄어쓰기

#006
print("오늘은","토요일")
# 오늘은 띄우고 토요일이 출력.

#007
print("naver", "kakao", "sk", "samsung", sep=";")

#008
print("naver", "kakao", "sk", "samsung", sep="/")

#009
print("first", end="");print("second")

#010
print(5/3)

#011
samsung=50000
incom=samsung*10
print(incom)

#012
siga="298조"
huenjae=50000
per=15.79
print(siga, type(siga))
print(huenjae, type(huenjae))
print(per, type(per))

#013
s = "hello"
t = "python"
print(s,t, sep=" ")

#014
print(2+2*3)

#015
a="132"
print(type(a))

#016
num="720"
num=int(num)
print(num, type(num))

#017
num=100
num=str(num)
print(num, type(num))

#018
data="15.79"
data=float(data)
print(data, type(data))

#019
year="2020"
year=int(year)
print(year, year+1, year+2, year+3)

#020
data=48584
print(data*36)

#021
letters = 'python'
print(letters[0], letters[2])

#022
license_plate = "24가 2210"
print(license_plate[4:])

#023
string = "홀짝홀짝홀짝"
print(string[::2])

#024
string = "PYTHON"
print(string[::-1])

#025
phone_number = "010-1111-2222"
phone_number1=phone_number.replace("-", " ")
print(phone_number1)

#026
phone_number1=phone_number.replace("-", "")
print(phone_number1)

#027
url = "http://sharebook.kr"
print(url[-2:])

#028
# lang = 'python'
# lang[0] = 'P'
# print(lang)
# tuple이기 때문에 P가 0번 요소에 저장되지 않고 error 발생

#029
string = 'abcdfe2a354a32a'
string= string.replace("a", "A")
print(string)

#030
# >> string = 'abcd'
# >> string.replace('b', 'B')
# >> print(string)
# 소문자 b가 대문자 B로 변경 된 상태에서 aBcd 출력.

#031
a="3"
b="4"
print (a+b)
# str 덧셈이기 때문에 34 출력

#032
print("Hi" * 3)
# str * 3 이기 때문에 HiHiHI 가 출력

#033
print("-"*80)

#034
t1 = ' python'
t2 = ' java'
t3 = (t1+t2)*3
print(t3, )

#035
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print(f'이름 : {name1}, 나이 : {age1}')
print(f'이름 : {name2}, 나이 : {age2}')

#036
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

#037
print(f'이름 : {name1}, 나이 : {age1}')
print(f'이름 : {name2}, 나이 : {age2}')

#038
상장주식수 = "5,969,782,550"
상장주식수=int(상장주식수.replace(",", ""))
print(상장주식수)

#039
분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7])

#040
data = "   삼성전자    "
data=data.strip()
print(data)

#041
ticker = "btc_krw"
ticker=ticker.upper()
print(ticker)

#042
ticker=ticker.lower()
print(ticker)

#043
안녕='hello'
안녕=안녕.capitalize()
print(안녕)

#044
file_name = "보고서.xlsx"
file_name=file_name.endswith("xlsx")
print(file_name)

print("-"*30)

#045
file_name = "보고서.xlsx"
file=file_name.endswith(("xlsx", "xls"))
print(file)

#046
file_name = "2020_보고서.xlsx"
file=file_name.startswith("2020")
print(file)

#047
a = "hello world"
a=a.split(" ")
print(a)

#048
ticker = "btc_krw"
ticker=ticker.split("_")
print(ticker)

#049
date = "2020-05-01"
date=date.split("-")
print(date)

#050
data = "039490             "
data=data.rstrip()
print(data)

#051
movie_rank=["닥스", "스플릿", "럭키"]
print(movie_rank)

#052
movie_rank=movie_rank + ["배트맨"]
print(movie_rank)

movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.append("배트맨")
print(movie_rank)

#053
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

#054
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]
print(movie_rank)

#055
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2:]
print(movie_rank)

#056
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs=lang1+lang2
print(langs)

#057
nums = [1, 2, 3, 4, 5, 6, 7]
a=max(nums)
b=min(nums)
print(a,b)

#058
nums = [1, 2, 3, 4, 5]
c=sum(nums)
print(c)

#059
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
c= len(cook)
print(c)

#060
nums = [1, 2, 3, 4, 5]
a=sum(nums)/5
print(a)

#061
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#062
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#063
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

#064
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

#065
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

#066
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

#067
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

#068
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))

#069
string = "삼성전자/LG전자/Naver"
s=string.split("/")
print(s)

#070
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

#71
my_variable=()
print(type(my_variable))

#72
m_r=("닥스", "스플릿", "럭키")
print(m_r)

#073
one=1,
print(type(one))

#074
# 튜플 class는 원소or요소를 추가, 삭제, 변경이 불가능함.

#075
# 튜플

#076
t = ('a', 'b', 'c')
t=list(t)
t.insert(1, "A")
del t[0]
t=tuple(t)
print(t)

#077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
a=list(interest)
print(a)

#078
interest = ['삼성전자', 'LG전자', 'SK Hynix']
b=tuple(interest)
print(b)

#079
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
# aplle banana cake

#080
c=tuple(range(2, 100, 2))
print(c)

