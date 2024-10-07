# dict 반복문, 조건부표현식 결합

keys=['a','b','c','d']

x={ key:value for key, value in dict.fromkeys(keys).items()} # abcd를 키로 가지게 만들어줌
print(x)

y={ key:value for key, value in [('age',12), ('name', '홍')]}
print(y)