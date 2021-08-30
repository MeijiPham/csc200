from gasp.utils import read_number
from random import randint
from timeit import default_timer as timer
import random

right = 0
operand_list = ['plus', 'minus', 'times', 'divided by']
start = timer()
quest = read_number('How many questions would you like? ')

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return round(a / b, 2)

for i in range(quest):
  num1 = randint(0, 12)
  num2 = randint(0, 12)
  operand = random.choice(operand_list)
  option = {
    'plus': add,
    'minus': subtract,
    'times': multiply,
    'divided by': divide,
  }
  correct_answer = option[operand](num1, num2)
  if read_number(f'\nWhat\'s {num1} {operand} {num2}? ' if operand != 'divided by' else f'\nWhat\'s {num1} {operand} {num2} to the nearest hundreth? ') == correct_answer:
    print('That\'s right - well done.')
    right += 1
  else:
    print(f'No, I\'m afraid the answer is {correct_answer}.')

end = timer()

print(f'\nI asked you {quest} questions. You got {right} of them right.\nWell done!\nYour time: {end - start:.2f} seconds')