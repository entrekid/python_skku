"""
입력 : 
    man1 : 
    man2 : 

출력 : 
    man1
    man2
    비겼는지
"""

man1 = input()
man2 = input()

if (man1 == "바위"):
    if (man2 == "가위"):
        print("Result: Man1 Win!")
    elif (man2 == "바위"):
        print("Result: Draw")
    else:
        print("Result: Man2 Win!")

elif (man1 == "가위"):
    if (man2 == "가위"):
        print("Result: Draw!")
    elif (man2 == "바위"):
        print("Result: Man2 Win!")
    else:
        print("Result: Man1 Win!")

else: # man1 보자기를 냈을 때:
    if (man2 == "가위"):
        print("Result: Man2 Win!")
    elif (man2 == "바위"):
        print("Result: Man1 Win!")
    else:
        print("Result: Draw!")


    
    