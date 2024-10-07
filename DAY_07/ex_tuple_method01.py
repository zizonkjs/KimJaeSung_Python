#tuple 전용 함수, 메서드
# 수정 불가, 추가, 삭제, 수정, 변경 안됨

nums=10,20,30

## method = index 확인 메서드 index(data)
idx=nums.index(20)
print(idx)

if 5 in nums:
    idx=nums.index(20)
    print(idx)

# count method

print(10, nums.count(10))
print(5, nums.count(5))