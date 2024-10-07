# 숫자를 입력 받아서 0이상 큰 숫자라면 
# 해당 숫자가 홀수인지 짝수인지 검사를 하고
# 0 미만이면 잘못된 숫자라고 출력

nums=input("숫자만 입력 :").strip() 
if len(nums)==1:
    if '0' <=nums<='9':
        nums=int(nums)
        if (nums)>0:
            print("짝수") if (nums)%2 ==0 else print("홀수")
        else:
            print("잘못된 숫자")
    else:
        print("숫자만 입력가능")
else:
    print("입력값이 없거나 2개이상 입력했습니다.")


# if nums<0:
#     print("잘못됨")
# else:
#      if int(nums)%2 ==0:
#         print("짝수")
#      else:
#         print("홀수")