"""
입력 : 30 20 30 40 50 

출력 : 결과
"""
numbers = map(int, input().split(" ")) # 30, 20, 30, 40, 50
num = 0
for number in numbers:
    num = num + 1
    if (number >= 60):
        print("{}번 학생은 {}점으로 합격입니다.".format(num, number))
    else:
        print("{}번 학생은 {}점으로 불합격입니다.".format(num, number))