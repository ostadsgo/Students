from random import randint

computer_vect = []
for i in range(10):
    random_num = randint(1, 21)
    computer_vect.append(random_num)

user_vect = []
for i in range(10):
    number = int(input("Enter a number: "))
    user_vect.append(number)


if computer_vect == user_vect:
    print("Bingo")
else:
    print("Not bingo")
