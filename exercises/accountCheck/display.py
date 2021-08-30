import json

with open('accounts.json', 'r') as f:
  accounts = json.load(f)

def main():
  print('')
  print('1. Login')
  print('2. Create new account')
  print('3. Exit')
  print('')

def account():
  user = input('Username: ')
  password = input('Password: ')  
  for account in accounts['accounts']:
    if user.lower() == account['user'].lower() and password == account['password']:   
      print('')
      for key, value in account['playerInfo'].items():
        if key == 'skillset':
          skills = ' '.join(value)
          print(f'{key[0].upper() + key[1:]}: {skills}')
        else: 
          print(f'{key[0].upper() + key[1:]}: {value}')
      return True

def create_account(user, password, filename='accounts.json'):
  account = accounts['accounts']
  details = {
      "user": "N/A",
      "password": "N/A",
      "playerInfo": {
        "class": "N/A",
        "rank": "Unranked",
        "win": 0,
        "loss": 0,
        "skillset": ["1. None", "2. None", "3. None", "4. None"]
      }
    }
  details['user'] = user
  details['password'] = password
  account.append(details)
  with open(filename, 'w') as f:
    json.dump(accounts, f, indent=2)

while True:
  main()
  select = input('Enter a number to select that option: ')
  if select == '1':
    if not account():
      print('Username or password is invalid.')
      continue
  elif select == '2':
    user = input('New username: ')
    password = input('New password: ')
    confirm = input('Confirm password: ')
    if confirm != password:
      print('Confirmation does not match.')
      continue
    create_account(user, password)
  elif select == '3':
    break