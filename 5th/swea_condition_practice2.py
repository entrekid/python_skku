"""
입력 :
약수를 구하고자 하는 숫자가 등장

출력 : 
이 숫자의 약수
"""


"""
9
3
1
"""


num = int(input())

# 1 ~ num : 나누기 시작할 것

# range(start, end + 1, step)

numbers = range(1, num + 1)
for number in numbers:
    if (num % number == 0):
        print("{}(은)는 {}의 약수입니다.".format(number, num))
