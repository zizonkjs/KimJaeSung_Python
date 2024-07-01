# 연습문제 : range로 리스트 만들기
a=list(range(5, -10, -2))
print(a)

# 심사문제 : range로 튜플 만들기
a=tuple(range(-10, 10, 2))
print(a)

b=tuple(range(-10, 10, 3))
print(b)

#연습문제 : 최근 3년간 인구 구하기
year = [2011,2013,2014,2015,2016,2017,2018]
population=[10249679, 10195318, 10143645, 10103233,10022181,9930616,9838892]
print(year[-3:])
print(population[-3:])

#연습문제 ㅣ 인덱스가 홀수인 요소 출력하기
n = -32, 75, 97, -10, 9, 32,4, -15, 0, 76, 14, 2
print(n[1::2])

#심사문제 : 리스트의 마지막 부분 삭제하기
x = [1,2,3,4,5,6,7,8,9]
del x[5:]
print(tuple(x))
v=["oven", "bat", "pony", "total", "leak", "wreck", "curl", "crop", "space", "navy", "loss", "knee"]
del v[-5:]
print(tuple(v))

#심사문제 : 문자열에서 인덱스가 홀수인 문자와 짝수인 문자 연결하기
a=input()
b=input()
print(a[1::2]+b[2::2])

c=input()
d=input()
print(c[1::2]+d[0::2])