from display import main_display, course_display, ordered_items, order_display, courses, root

print('To navigate, select an option by looking at the corresponding number.')

while True:
  main_display()
  course_num = int(input('Enter a number: '))
  if course_num == 5:
    order_display()
    answer = input(('Would you like to place your order? (y/n) '))
    if answer.lower() == 'y':
      print('Your entire order has been received.')
      break
    else:
      continue
  course_display(courses[course_num - 1])
  current_items = [food.find('item').text for food in root.findall('food') if food.get('type') == courses[course_num - 1]]
  while True:
    item_select = int(input('Enter a number to place order: '))
    if item_select == len(current_items) + 1:
      break
    else:
      ordered_items.append(current_items[item_select - 1])
      print(f'Your order of {current_items[item_select - 1].lower()} has been placed.')