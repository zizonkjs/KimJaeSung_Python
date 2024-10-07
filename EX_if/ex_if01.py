# 리스트에 data 가 있다 없다 확인
# 있는 경우에는 : "*" len([])>0
# 없는 경우 : "없다"
# nums=[9]

# len(nums)

# if len([nums])>0:
#     print('*')
# else:
#     print("없다")

# 데이터 : [22]
# 10보다 큰 데이터일 경우 숫자 만큼 *을 출력.
# 10 이하인 경우 : 별을 한개만 출력.

nums=[22]

if int(nums[0])>10:
    print(nums[0]*"*")
else:
    print("*")


nums=[2]

if int(nums[0])>10:
    print(nums[0]*"*")
else:
    print("*")