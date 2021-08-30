from gasp.utils import read_number

def incorrect_bound(low, high):
  if high < low:
    print('Invalid bounds. Try again.')
    return True
  return False

def out_of_bound(num, low, high):
  if num > high or num < low:
    print('Please stay within the bounds.')
    return True
  return False

def scenario(question, low, high):
  while True:
    num = read_number(question)
    if out_of_bound(num, low, high):
      continue
    return num