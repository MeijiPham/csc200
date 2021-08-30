import xml.etree.ElementTree as ET

tree = ET.parse('menu.xml')
root = tree.getroot()

courses = ['drink', 'appetizer', 'entree', 'dessert']
ordered_items = []

def main_display():
  num = 1
  print('')
  print('Courses: ')
  for course in courses:
    print(f'{num}. {course[0].upper() + course[1:]}')
    num += 1
  print(f'{num}. View my order')
  print('')

def course_display(course):
  num = 1
  print('')
  print(f'{course[0].upper() + course[1:]}s:')
  for food in root.findall('food'):
    if food.get('type') == course:
      item = food.find('item').text
      price = float(food.find('price').text.strip('$'))
      print(f'{num}. {item}........ ${price:.2f}')
      num += 1
  print(f'{num}. Return to main menu')
  print('')

def order_display():
  print('')
  print('Your order:')
  amount = 0
  unique_list = []
  prices_list = []
  count = 0
  for item in ordered_items:
    if item not in unique_list:
      unique_list.append(item)
  for item in unique_list:
    for food in root.findall('food'):
      if item == food.find('item').text:
        prices_list.append(float(food.find('price').text.strip('$')))
    item_count = ordered_items.count(item)
    print(f'{item_count} {item}........ ${prices_list[count] * item_count:.2f}')
    amount += prices_list[count] * item_count
    count += 1
  print('')
  print(f'Subtotal: ${amount:.2f}')
  print(f'Tax: ${amount * .06:.2f}')
  print(f'Your total amount is: ${amount * .06 + amount:.2f}')
  print('')