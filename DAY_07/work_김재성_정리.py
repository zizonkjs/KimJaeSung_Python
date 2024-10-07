# 리스트에 요소 추가하는
# append()
# a=[10,20,30]
# a.append(500)

# 리스트 안에 리스트 추가하기 
# a=[10,20,30]
# a.append([500,600])

#리스트 확장하기
# a.extend([500,600])
# 마지막 요소에 추가됨

# 리스트에 특정인덱스 추가하기
# a.insert(2,500)
# a.insert(len(a), 500)
# 마지막요소에 추가하기

#리스트 중간에 여러요소 추가하기
# a[1:1] = [500,600,700,800]

#리스트에서 특정요소 꺼내서 저장하기
# a.app() -> 마지막요소 빼기
# b=a.app() -> 뺀요소 b에 저장하기
# a.app(1) -> 1번요소 빼기
# b=a.app(1) -> 1번요소 b에 저장하기

# 리스트에서 특정값 삭제하기
#a.remove(인덱스 값)
#처음 찾은 값을 제거

#리스트에서 특정 값의 인덱스 구하기
#a.index(20)

#특정 값의 개수 구하기
#a.count(20)

#리스트 순서 뒤집기
# a.reverse()

# 리스트의 요소를 정렬하기
#a.sort()

#리스트 슬라이스로 조작하기
# a[len(a):] = [500]
# 마지막요소에 500 저장하기

# 리스트가 비어있는지 확인하는법
# if not len(seq):
# if len(seq):

#리스트의 복사
# a=[0,0,0,0,0]
# b=a.copy()

#반복문으로 리스트의 요소를 모두 출력하기
# for 변수 in a:
#   print(a)

#인덱스와 요소 함께 출력하기
# for index, value in enumerate(a)
#   print(index, value)

# for 반복문에서 인덱스로 요소출력하기
# a=[38, 21, 53, 62, 71]
# for i in range(len(a)):
#     print(a[i])

#while 반복문으로 요소 출력하기
# i=0
# while i < len(a):
#   print(a[i])
#   i +=1

# 리스트의 가장 작은 수, 가장 큰 수, 합계 구하기
# 가장 작은수 구하기
# a= [38, 21, 53, 62, 19]
# smallest = a[0]
# for i in a:
#     if i < smallest:
#         smallest = i
# print(smallest)

# # 가장 큰수 구하기
# a= [38, 21, 53, 62, 19]
# smallest = a[0]
# for i in a:
#     if i > smallest:
#         smallest = i
# print(smallest)
# print(min(a))
# print(max(a))

#합계 구하기
# sum(a)

# 리스트 표현식구하기
# a = [i for i in range(10)]

# 리스트 포현식에서 if 조건문 구하기
# a = [i+5 for i in range(10) if i%2 ==1]

# a = [i * j for j in range(2,10) for i in range(1,10)]

# list에 map 사용하기
# list(map(함수,리스트))
# tuple(map(함수, 튜플))

# a = [1.2, 2.5, 3.7, 4.6]
# for i in range(len(a)):
#     a[i] = int(a[i])
# print(a)

# a = list(map(int, a))

# a = list(map(str, range(10)))

# a = map(int, input().split())

# tuple index
# a =38, 39, 40
# a.index(38)

#a.count(38)

# for 반복문 사용해서 출력하기
# for i in a:
#   print(i, end='')

# 튜플표현식
# a = tuple(i for i in range(10) if i%2 == 0)

# map 사용하기
# a = tuple(map(int, a))
# min(a), max(a), sum(a)

# 연습문제 : 리스트에서 특정 요소만 뽑아내기

a=['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b=[i for i in a if len(i)==5]

print(b)

# 심사문제 : 2의 거듭제곱 리스트 생성하기

a=int(input("1~20 입력 :"))
b=int(input("10~30 입력 :"))
# 2**1, 2**2,2**3,2**4,...2**10

# a=1
# b=10
c=[]
# a 값이 b 값만큼 1씩 증가하고 b값과 같아지면 중단되게 만들어야함
for num in range(a,b+1):
    c.append(2**num)
print(c)


# 딕셔너리에 키-값 쌍 추가하기
# setdefault: 키-값 쌍 추가
# update:키의 값 수정, 키가 없으면 키-값 쌍 추가

# x={'a': 10, 'b':20, 'c':30, 'd':40}
# x.setdefault('e')

# 딕셔너리에서 키의 값 수정하기
# x.update(a=90)
# x.update(e=50)
# x.update(a=900, f=60)

# 키가 숫자일 경우
# x.update({1:'ONE', 3:'THREE})
# y.update([[2, 'TWO'], [4, 'FOUR']])
# y.update(zip([1,2], ['one', 'two']))

# 딕셔너리에서 키-값 쌍 삭제하기
# x.pop('a')

# 임의의 키-값 쌍 삭제하기
# x.popitem() -> 마지막 요소 삭제로 바뀜

#딕셔너리에서 키 값 가져오기
# x = {'a':10, 'b':20, 'c':30, 'd':40}
# x.get('a')
# x.get('z', 0) -> 0을 반환함.

#키-값 쌍 가져오기
# x.items()

# x.key()
# 키를 모두 가져옴

# x.values()
# 값을 모두 가져옴

#반복문으로 딕셔너리 키:값 모두 출력하기
# x={'a':10, 'b':20, 'c':30, 'd':40}
# for i in x:
#   print(i, end=' ')
# 키만 출력됨

# for key, values in x.items():
#   print(key, values)

# 키만 출력하기
# for key in x.keys():
#   print(key, end=' ')

# 값만 출력하기
# for value in x.values():
#   print(value, end='')

# 딕셔너리 표현식사용하기
# keys = ['a', 'b', 'c', 'd']
# x = {key: value for key, value in dict.fromkeys(keys).items()}

# x = {key:value for key, value in dict.fromkeys(keys).items()}

# x = {key:value for key, value in dict.fromkeys(keys).keys()}
# 값을 키만 가져옴

# x = {key:value for key, value in {'a':10, 'b':20, 'c':30, 'd':40}.values()}
# 값을 키로 사용





    