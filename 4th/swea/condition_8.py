"""
입력 :100 ~ 300까지의 숫자

출력 : 단순 짝수를 출력하는게 아니에요!

각 자릿수가 모두 짝수인 애들을 지금 내가 출력하겠다.

_ _ _ : 122 : 1 2 2

"""

"""
100 ~ 300 
100 101
"""
numbers = range(100, 287)
for number in numbers: 
    number = str(number)
    number = list(number)
    
    if number[0] not in ["0", "2", "4", "6", '8']:
        continue
    if number[1] not in ["0", "2", "4", "6", "8"]:
        continue
    if number[2] not in ["0", "2", "4", "6", "8"]:
        continue
    print("".join(number), end=",")
print(288)   
