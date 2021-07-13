import random

answer = 'y'

print("Welcome to the Fortune Teller Game!")
print("You'll select a number and a color(YELLOW, GREEN, BLUE AND RED) and I'll tell you what the future holds for you!")

while answer == 'y':
    color = input("Select a color [yellow, green, blue, red] : ")

    if color == "yellow" or color == "green":
        number = int(input("Select a number [1, 2, 5, 6] : "))
        if number == 1:
            print("Don't worry you have a very bright future ahead of you! Be patient.")
        elif number == 2:
            print("You will become a millionare at the age of 30!")
        elif number == 5:
            print("You will have a great and happy family.")
        elif number == 6:
            print("You will be famous and the whole world will know you!")
        else:
            print("Only numbers allowed are 1,2,5,6")

    elif color == "blue" or color == "red":
        number = int(input("Select a number [3, 4, 7, 8] : "))
        if number == 3:
            print("You will be living a happy life for 150 years!")
        elif number == 4:
            print("You will become a successful engineer one day!")
        elif number == 7:
            print("Every dream of yours will come true when you are 35 years of age!")
        elif number == 8:
            print("You are going to be a successful doctor!")
        else:
            print("Only numbers allowed are 3,4,7,8")

    else:
        print("Colors yellow, green, blue, red are only allowed")

    answer = input("Want to play again? Enter 'y' for Yes and 'n' for No : ")
