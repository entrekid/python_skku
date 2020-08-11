"""
for 문
반복문 : 반복을 시키는 프로그래밍 명령

1, ...., 100 출력해라

print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
...
print(100)

var = 1, ..., 100

print(var)
"""

"""
for 물건 in 상자 :
    물건
    (반복을 시키고 싶은 명령)

for element in list:
    print(element)
"""

"""
# 상자의 종류

1) list, string

2) range
range(start, end + 1, step)

range(start, end + 1)
"""

# list, string
my_list = [0, 1, 2, 3,4 ,5 ,6 ,7, 8, 9, 10]
for element in my_list:
    print(element)

print("====================")
my_range = range(11) # 0 ~ 10
for element in my_range:
    print(element)
