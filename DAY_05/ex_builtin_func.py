# 내장함수
# 정수 관련 내장함수
# 2진수(bin), 8진수(oct), 16진수(hex)
# 숫자표현
# 정수 -> 2진수로 변환 해주는 : bin(정수) -> 0b2진수계수(str)
print(bin(4), type(bin(4)))

# 정수 -> 8진수로 변환 해주는 : oct(정수) -> 0o8진수계수(str)
print(oct(8), type(oct(8)))

# 정수 -> 10진수 = 그냥 숫자 쓰면됨

# 정수 -> 16진수로 변환 해주는 : hex(정수) -> 0x16진수계수(str)
print(hex(17), type(hex(17)))

# 16진수 --> 10진수 변환 int()
print(int(0x12))
print(int(0b10010))
