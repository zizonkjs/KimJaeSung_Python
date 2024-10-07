# 전역변수
persons=["Hong"]
gender={"H":"남자"}
year=2024

# 사용자 정의함수
def add_person(name):
    global year
    year +=1 # 얘는 데이터 값 자체가 달라지는거라 안됨 global year 없이 쓰면 
    persons.append(name) # list 는 값이 달라지는게 아니기 때문에 가능
    gender[name]="여"

def remove_person(name):
    persons.remove(name)
    gender.pop(name)

#함수호출
print(f'persons=>{persons}')
print(f'gender=>{gender}')

add_person("Park")
print(f'persons=>{persons}')
print(f'gender=>{gender}')

remove_person("Park")
print(f'persons=>{persons}')
print(f'gender=>{gender}')