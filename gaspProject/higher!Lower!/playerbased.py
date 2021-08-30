from random import randint
from gasp.utils import read_yesorno, read_number
from os import system, name
from rangetest import incorrect_bound, out_of_bound, scenario
from gasp import sleep

def clear():
  if name == 'nt':
    _ = system('cls')

def game(guessing, entering, low_bound, high_bound):
  print(f'\nIt is {guessing}\'s turn to guess.')
  question = f'{entering}, please enter a number for {guessing}: '
  true_num = scenario(question, low_bound, high_bound)
  sleep(1)
  clear()
  tries = 0
  while True:
    question = f'\n{guessing}, what is your guess? '
    guess = scenario(question, low_bound, high_bound)
    if guess == true_num:
      print('Correct!')
      break
    else:
      if guess > true_num:
        print('That\'s too high!')
      else:
        print('That\'s too low!')
      tries += 1
  return tries + 1

p1_name = input('Player 1\'s name: ')
p2_name = input('Player 2\'s name: ')

while True:
  low = read_number('\nSelect a lower bound: ')
  high = read_number('Select a higher bound: ')
  if incorrect_bound(low, high):
    continue
  p1 = game(p1_name, p2_name, low, high)
  p2 = game(p2_name, p1_name, low, high)
  print(f'\n{p1_name}, it took you {p1} tries. {p2_name}, it took you {p2} tries.')
  if p1 < p2:
    print(f'{p1_name}, you win!')
  elif p2 < p1:
    print(f'{p2_name}, you win!')
  else:
    print('You both tied!')
  if read_yesorno('Would you like to play again? '):
    continue
  print('Thanks for playing!')
  break