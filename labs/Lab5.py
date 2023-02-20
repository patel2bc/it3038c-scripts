#Take a birthday date input and calculate how many seconds old you are

import datetime

#input
birthday = input ("Enter your birthdate in mm/dd/yyyy format: ")

#set var 
birth_date = datetime.datetime.strptime(birthday, "%m/%d/%Y")
time_difference = datetime.datetime.now() - birth_date
seconds = time_difference.total_seconds()

#output 
print(f"You are {seconds:,} seconds old!")

#Take a word as input and count how many letters, how many vowels and how many consonants

#input 
word = input("Enter your word: ")

#set var
letters = 0
vowels = 0
consonants = 0

#logic 
for char in word:
    if char.isalpha():
        letters += 1
        if char in "aeiou":
            vowels += 1

        else:
                consonants += 1

#output
print(f"The word '{word}' has {letters} letters, {vowels} vowels, and {consonants} consonants.")
            
#Take a number input and calculate how many prime numbers come between it and 0

#input
number = int(input("Enter a number: "))

#var
prime_num = []

#logic
for i in range(2, number + 1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_num.append(i)

#output
print(f"There are {len(prime_num)} prime numbers between {number}.")

#Number guessing game
import random

#var
number = random.randint(1, 10)

num_guess = 0

#logic and output 
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    num_guess += 1
    if guess == number:
                print(f"Congrats, you guessed the number in {num_guess} guesses!")
                break
    elif guess < number:
        print("Too low! Try again!")
    else:
        print("Too high! Try again!")



#Bunci Patel Lab5 Submission 
