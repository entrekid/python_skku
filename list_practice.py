

"""

new_list = [1,  2,3,  4,5, 6, "hello", 1.3, "hi", True, False ]

1st) 리스트 안에 몇 개가 들어있어?

2nd)리스트의 n 번째 항이 뭐야?
"""
# list 안에서 각각의 물건들을 꺼내 쓰는 방법
new_list = [1, 2, 3, 4, 5, 6, "hello", 1.3, "hi", True, False ]
#           0  1  2  3 4  5  6 .......................... 10 : length - 1
# print(new_list[0])


"""
잔기술

"""

# new_list[start : end + 1] : list에서 start 부터 end까지를 뽑아라
print(new_list[0 : 2])

# new_list : 2 ~ 7
print(new_list[2 : 8])

# new_list : [start : end + 1 : step]

new_list[2: 5 : 2]

# 2 4 


new_list[1: 10 : 3]

# 1 2 3 4 5 6 7 8 9 

# 1 4 7 


# 리스트 안에서 원하는 값을 찾아내기

new_list2 = ["hello", "min hyeok"]

# 특정한 값을 찾고 싶어
print(new_list2.index("min hyeok"))