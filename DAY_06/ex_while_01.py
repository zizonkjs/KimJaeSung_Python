# while 반복문

num=10 # 변수 선언
while num > 0 :
    print(num)
    num=num-1

# 리스트의 원소 읽기
# while 반복문 : 리스트 개수

nums=[11,22,33]


cnt=0
while cnt<len(nums):
    print(cnt, nums[cnt])
    cnt=cnt+1

# "Hello" 문자열의 원소를 하나씩 출력하기.

msg="Hello"

idx=0
while idx<len(msg):
    print(idx, msg[idx])
    idx=idx+1