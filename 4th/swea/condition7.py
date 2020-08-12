"""
입력 : 1 ~ 200까지의 숫자

출력 : 7의 배수이지만, 5의 배수는 아닌 것들을 출력하겠다.

2) 출력 결과를 엔터가 아니라, 콤마로 구분해서 찍어내려라
"""

numbers = range(1, 190)
for number in numbers:
    if number % 7 == 0:
        if number % 5 != 0: 
            print(number, end = ",")
    else:
        continue
print(196)