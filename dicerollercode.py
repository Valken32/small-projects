import random
print ("Welcome to Alexander's Advanced Dice Roller! \n In this program, you will be able to input two numbers. a minimum and a maximum, and I will roll them for you!")
answer = input("What is your minimum?")
x = answer.lower().strip()
answer = input("What is your maximum?")
y = answer.lower().strip()
repeat = "true"
while repeat == "true":
    print ("Your number is", random.randint (int(x),int(y)))
    answer = input ("Would you like to roll again? Yes or No?")
    if answer.lower().strip() == "yes":
        continue
    if answer.lower().strip() == "no":
        break