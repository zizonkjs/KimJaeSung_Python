# outer =5 , inner = 5
for i in range(5): # 얘는 실행코드가 2개
    for j in range(5): # 얘는 1개
        print(f'j:{j}', end=' ')
    print(f'i:{i}\\n') # i 코드

for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()

for i in range(5):
    for j in range(i+1):
        # if j==i:
        #     print('*')
        # else:
        #     print(' ', end='')
    # print() # 반복할때마다 줄바꾸기
        print('*' if i==j else ' ', end='\n' if i==j else '')

# 19.5 연습문제
# for i in range(5):
#     for j in range(5):
#         if j < i :
#             print(' ', end='')


        