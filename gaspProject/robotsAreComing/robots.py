from gasp import *
from random import randint

begin_graphics()
finished = False

class Player:
  pass

class Robot:
  pass

def place_player():
  global player
  player = Player()
  player.x = randint(0, 63)
  player.y = randint(0, 47)

def place_robots():
  global robots
  robots = []
  while len(robots) < numbots:
    robot = Robot()
    robot.x = randint(0, 63)
    robot.y = randint(0, 47)
    if not collided(robot, robots):
      robot.shape = Box((10 * robot.x, 10 * robot.y), 10, 10)
      robots.append(robot)

def safely_place_player():
  global player
  place_player()
  while collided(player, robots):
    place_player()
  player.shape = Circle((10 * player.x + 5, 10 * player.y + 5), 5, filled=True)

def movement(direct, who, coor_x, coor_y):
  global player, robot
  if direct == 'u' and coor_y < 47:
    coor_y += 1
  elif direct == 'd' and coor_y > 0:
    coor_y -= 1
  elif direct == 'r' and coor_x < 63:
    coor_x += 1
  elif direct == 'l' and coor_x > 0:
    coor_x -= 1  
  if who == 'player':
    player.x = coor_x
    player.y = coor_y
  elif who == 'bot':
    robot.x = coor_x
    robot.y = coor_y

def move_player():
  global player
  key = update_when('key_pressed')
  moves = {
    '1': ['d', 'l'],
    '2': ['d'],
    '3': ['d', 'r'],
    '4': ['l'],
    '6': ['r'],
    '7': ['u', 'l'],
    '8': ['u'],
    '9': ['u', 'r']
  }
  while key == '5':
    remove_from_screen(player.shape)
    safely_place_player()
    key = update_when('key_pressed')
  else:
    for move in moves[key]:
      movement(move, 'player', player.x, player.y)

  move_to(player.shape, (10 * player.x + 5, 10 * player.y + 5))

def move_robots():
  global robot, player
  for robot in robots:
    if robot.x < player.x:
      movement('r', 'bot', robot.x, robot.y)
    if robot.x > player.x:
      movement('l', 'bot', robot.x, robot.y)
    if robot.y > player.y:
      movement('d', 'bot', robot.x, robot.y)
    if robot.y < player.y:
      movement('u', 'bot', robot.x, robot.y)

    move_to(robot.shape, (10 * robot.x + 5, 10 * robot.y + 5))

def robot_crashed(the_bot):
  for a_bot in robots:
    if a_bot == the_bot:
      return False
    if a_bot.x == the_bot.x and a_bot.y == the_bot.y:
      return a_bot
  return False

def collided(obj1, obj_list):
  for item in obj_list:
    if obj1.x == item.x and obj1.y == item.y:
      return True
  return False

def check_collisions():
  global finished, robots, junk
  surviving_robots = []
  for bot in robots:
    if collided(bot, junk):
      continue
    jbot = robot_crashed(bot)
    if jbot == False:
      surviving_robots.append(bot)
    else:
      remove_from_screen(jbot.shape)
      jbot.shape = Box((10 * jbot.x, 10 * jbot.y), 10, 10, filled=True)
      junk.append(jbot)
  robots = []
  for bot in surviving_robots:
    if collided(bot, junk):
      continue
    robots.append(bot)
  if collided(player, robots + junk):
    finished = True
    Text('You\'ve been caught!', (320, 240), size=80)
    sleep(3)
    return
  if not robots:
    finished = True
    Text('You win!', (320, 240), size=80)
    sleep(3)
    return

numbots = 10
junk = []

place_robots()
safely_place_player()

while not finished:
  move_player()
  move_robots()
  check_collisions()

end_graphics()
