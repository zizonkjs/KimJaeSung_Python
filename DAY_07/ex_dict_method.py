# dict method : keys(), values(), items(), clear(), get(key), get(key, defaut), member연산자 in, not in

person={'name':'홍길이', 'age':10}

# method - 값 읽어오는 메서드 get(key)
print(person['name']) 
# print(person['gender']) key error

# key 해당하는 values가 없으면 default 값을 반환
print(person.get('name', '몰라염'))
print(person.get('gender', '없음'))
print(person.get('gender')) # 안쓰면 None출력

# 키와 값 추가하기
person['gender']='남'

#수정 업데이트
person['gender']='여'

#수정및 추가 업데이트 메서드 update(k=v)
person.update({'gende':'어린', 'jo':'학'}) # --> dict 타입
person.update(gender='어린이', job='학생')
person.update(**{'weight':100, 'height':170}) # **을 사용하면 (ㅁ=ㅁ,ㅁ=ㅁ) 형태로 변경
print(person)



# msg="Hello Good Luck"
# alpha=set(msg) # -> 중복제거하고 카운팅 들어가게 할려고 선언
# save={}
# for m in alpha:
#     print(m, msg.count(m))
#     save[m]=msg.count(m)
# print(save)