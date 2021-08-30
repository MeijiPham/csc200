from gasp import sleep
from random import randint
from gasp.utils import read_number, read_yesorno
import math
from rangetest import incorrect_bound

def bot_guess(num, bot):
  num_list = [i for i in range(low, high + 1)]
  tries = 0
  while True:
    bot_choice = guess_method(num_list)
    sen_list = [f'\n{bot} guesses...', bot_choice]
    print_slowly(sen_list)
    if bot_choice == num:
      print(f'\nCorrect!\nIt took {bot} {tries + 1} tries to guess the number.')
      break
    elif bot_choice < num:
      print('\nThat\'s too low!')
      tries += 1
      for i in range(bot_choice + 1):
        if i in num_list:
          num_list.remove(i)
    elif bot_choice > num:
      print('\nThat\'s too high!')
      tries += 1
      for i in range(bot_choice, num_list[-1] + 1):
        if i in num_list:
          num_list.remove(i)

def guess_method(nums):
  sum = 0
  for num in nums:
    sum += num
  return math.ceil(sum / len(nums))

def print_slowly(sentence):
  for i in range(2):
    print(sentence[i], sep=' ', end=' '); sleep(1)

while True:
  bot_name = 'Athena'
  low = read_number('\nSelect a lower bound: ')
  high = read_number('Select a higher bound: ')
  if incorrect_bound(low, high):
    continue
  num = randint(low, high)
  print(num)
  bot_guess(num, bot_name)
  ans = input(f'Have {bot_name} guess again? ')
  if read_yesorno(f'Have {bot_name} guess again? '):
    continue 
  break