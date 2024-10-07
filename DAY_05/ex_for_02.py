# # 반복문
# # 문자열을 기계어로(bin)으로 변환해서 출력
# # 입력 -> 'Hello' str -> ord로 변환 -> bin으로 변환
# # 출력 -> 2진수값
# msg="Hello"
# result=''
# for m in msg:
#     result=result+bin(ord(m))[2:] #-> [2:]은 2진수 코드 0b 제거해주고 출력.
#     print(result)

# # 원소/요소의 인덱스번호와 값을 함께 가져오기
# # enumerate() 내장함수
# # 전달된 반복가능한 객체에서 원소당 번호를 부여해서 튜플로 묶어줌
# # 원소의 인덱스 정보가 필요한 경우 사용함.
# nums=[11,33,55]

# #원소 데이터만 가져옴
# for n in nums:
#     print(n)

# # 인덱스와 원소데이터 가져오기

# for n in enumerate(nums):
#     print(n)
#     # 원소에 인덱스 번호 부여함.
#     # 결과값은 tuple(인덱스번호, nums값)로 묶여서 출력.

# nums=[11,22,33]

# # for n in nums:
# #     n=n*100

# # range => nums index
# for idx in range( len(nums) ):
#     print(idx, nums[idx])
#     nums[idx]=nums[idx]*100

# # 그리고 얘는 인덱스 번호와 인덱스 값을 따로 출력할 때. 즉 언패킹했을 때임.
# for idx, n in enumerate(nums):
#     print(idx, n)
#     nums[idx]=nums[n]*100 
#     print(type(n))
#      # idx-> 인덱스 번호[0],[1],[2] 언패킹 방식










