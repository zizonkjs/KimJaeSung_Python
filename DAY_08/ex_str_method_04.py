# 문자열에서 원소요소 변경해주는 method : .replace()
msg='pithon'
msg=msg.replace('i', 'y')# 전용 method .replace() 로 변경
print(msg)

msg="Good Happy"
# 알파벳 o를 대문자로 변경하고싶다
# msg=msg.replace('o', 'O') # 지정하지 않으면 전부 변경
# print(msg)


# 알파벳 o를 한개만 대문자로 변경하고싶다
msg=msg.replace('o', 'O', 1) # 1은 conunt 몇번 바꾸꼬 싶냐 할 때 계수입력
print(msg)
