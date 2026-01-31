import random

number= input("Type a number: ")

if number.isdigit():
    number = int(number)

    if number <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0,number)

while True:
    user_guess=input("make a guess: ")
    if user_guess.isdigit():
        user_guess= int(number)
    else:
        print('Please type a number next time.')
        continue
    if user_guess==random_number:
        print("U Won")
        break
    else:
        print("Wrong")
    