import random

number_to_guess = random.randint(1, 100)
while True:
 try:
     guess = int(input("Guess a  number between 1 and 100: "))

     if guess < number_to_guess:
      print("too low!")
     elif guess > number_to_guess:
      print("Too high")
     else:
       print("You win")
       break
 except ValueError:
   print("please enter a valid  number")

