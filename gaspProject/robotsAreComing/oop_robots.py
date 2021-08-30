from gasp import *
from random import randint
from time import sleep

class RobotsGame:
  LEFT_KEY = "4"
  UP_LEFT_KEY = "7"
  UP_KEY = "8"
  UP_RIGHT_KEY = "9"
  RIGHT_KEY = "6"
  DOWN_RIGHT_KEY = "3"
  DOWN_KEY = "2"
  DOWN_LEFT_KEY = "1"
  TELEPORT_KEY = "5"
  RIGHT_EDGE = 63
  LEFT_EDGE = 0
  TOP_EDGE = 47
  BOTTOM_EDGE = 0
  BACKGROUND_COLOR = color.BLACK
  PLAYER_COLOR = color.YELLOW
  ROBOT_COLOR = color.ROYALBLUE
  JUNK_COLOR = color.RED
  TEXT_COLOR = color.WHITE
  FINAL_LEVEL = 5

  numbot = 4

  def __init__(self):
    begin_graphics(height=560, title='Robot Invasion', background=self.BACKGROUND_COLOR)
    self.display = RobotsDisplay()
    self.finished = False
    self.prepare_screen()

  def prepare_screen(self):
    self.robots = []
    self.junk = []
    while len(self.robots) < self.numbot:
      self.robot = Robot()
      if not self.collided (self.robot, self.robots):
        self.robots.append(self.robot)
        self.robot.safely_place_robot()
    self.player = Player(self.robots, self.display.update)

  def next_move(self):
    self.player.move()
    for bot in self.robots:
      bot.move(self.player)
    self.check_collisions()

  def robot_crashed(self, crash_bot):
    for bot in self.robots:
      if bot == crash_bot:
        return False
      if bot.x == crash_bot.x and bot.y == crash_bot.y:
        remove_from_screen(crash_bot.shape)
        return bot
    return False 

  @staticmethod
  def collided(obj, list_of_things):
    for thing in list_of_things:
      if obj.x == thing.x and obj.y == thing.y:
        return True
    return False

  def check_collisions(self):
    surviving_robots = []

    for bot in self.robots:
      if self.collided(bot, self.junk):
        remove_from_screen(bot.shape)
        self.display.score += self.display.ROBOT_JUNK
        self.display.update('score')
        continue
      jbot = self.robot_crashed(bot)
      if jbot == False:
        surviving_robots.append(bot)
      else:
        remove_from_screen(jbot.shape)
        jbot.shape = Box((10 * jbot.x, 10 * jbot.y), 10, 10, filled=True, color=self.JUNK_COLOR)
        self.display.score += self.display.ROBOT_ROBOT
        self.display.update('score')
        self.junk.append(jbot)

    self.robots = []

    for bot in surviving_robots:
      if self.collided(bot, self.junk):
        continue
      self.robots.append(bot)

    if self.collided(self.player, self.robots + self.junk):
      self.display.lives -= 1
      remove_from_screen(self.player.shape)
      self.display.update('lives')
      if self.display.lives == 0:
        self.display.mass_removal()
        Text('You lose!', (320, 530), size=80, color=self.TEXT_COLOR)
        Text(f'Final score: {self.display.score}', (320, 510), size=80, color=self.TEXT_COLOR)
        self.finished = True
        sleep(3)
      else:
        self.player.safely_place_player()

    if not self.robots:
      if self.display.level == RobotsGame.FINAL_LEVEL:
        self.display.mass_removal()
        Text('You win!', (320, 530), size=80, color=self.TEXT_COLOR)
        Text(f'Final Score: {self.display.score}', (320, 510), size=80, color=self.TEXT_COLOR)
        self.finished = True
        sleep(3)
      else:
        self.next_level()

  def next_level(self):
    self.display.level += 1
    RobotsDisplay.teleports += 5
    self.display.mass_removal()
    self.display.game_display(self.display.level, self.display.score, self.display.lives, RobotsDisplay.teleports)
    for junk in self.junk:
      remove_from_screen(junk.shape)
    remove_from_screen(self.player.shape)
    self.numbot += 2
    self.prepare_screen()

  def over(self):
    end_graphics()

class RobotsDisplay:
  ROBOT_ROBOT = 1000
  ROBOT_JUNK = 500
  level = 1
  score = 0
  lives = 3
  teleports = 10

  def __init__(self):
    self.game_display(self.level, self.score, self.lives, self.teleports)

  def game_display(self, level, score, lives, teleports):
    Line((0, 480), (640, 480), color=RobotsGame.TEXT_COLOR, thickness=1.5)

    self.lev = Text('Level', (80, 530), size=80, color=RobotsGame.TEXT_COLOR)
    self.level_text = Text(f'{str(level)}', (80, 510), size=80, color=RobotsGame.TEXT_COLOR)

    self.sco = Text('Score', (240, 530), size=80, color=RobotsGame.TEXT_COLOR)
    self.score_text = Text(f'{str(score)}', (240, 510), size=80, color=RobotsGame.TEXT_COLOR)

    self.liv = Text('Lives', (400, 530), size=80, color=RobotsGame.TEXT_COLOR)
    self.lives_text = Text(f'{str(lives)}', (400, 510), size=80, color=RobotsGame.TEXT_COLOR)

    self.tele = Text('Teleports', (540, 530), size=80, color=RobotsGame.TEXT_COLOR)
    self.teleports_text = Text(f'{str(teleports)}', (540, 510), size=80, color=RobotsGame.TEXT_COLOR)

  def update(self, item):
    if item == 'level':
      remove_from_screen(self.level_text)
      self.level_text = Text(f'{str(self.level)}', (80, 510), size=80, color=RobotsGame.TEXT_COLOR)
    elif item == 'score':
      remove_from_screen(self.score_text)
      self.score_text = Text(f'{str(self.score)}', (240, 510), size=80, color=RobotsGame.TEXT_COLOR)
    elif item == 'lives':
      remove_from_screen(self.lives_text)
      self.lives_text = Text(f'{str(self.lives)}', (400, 510), size=80, color=RobotsGame.TEXT_COLOR)
    elif item == 'teleports':
      remove_from_screen(self.teleports_text)
      self.teleports_text = Text(f'{str(self.teleports)}', (540, 510), size=80, color=RobotsGame.TEXT_COLOR)

  def mass_removal(self):
    remove_from_screen(self.lev)
    remove_from_screen(self.level_text)
    remove_from_screen(self.score_text)
    remove_from_screen(self.sco)
    remove_from_screen(self.liv)
    remove_from_screen(self.lives_text)
    remove_from_screen(self.tele)
    remove_from_screen(self.teleports_text)

class Player:
  def __init__(self, robot_list, func):
    self.update = func
    self.robot_list = robot_list
    self.safely_place_player()

  def place(self):
    self.x = randint(RobotsGame.LEFT_EDGE, RobotsGame.RIGHT_EDGE)
    self.y = randint(RobotsGame.BOTTOM_EDGE, RobotsGame.TOP_EDGE)

  def safely_place_player(self):
    self.place()
    while RobotsGame.collided(self, self.robot_list):
      self.place()
    self.shape = Circle((10 * self.x + 5, 10 * self.y + 5), 5, filled=True, color=RobotsGame.PLAYER_COLOR)

  def teleport(self):
    RobotsDisplay.teleports -= 1
    self.update('teleports')
    remove_from_screen(self.shape)
    self.safely_place_player()

  def movement(self, direct, coor_x, coor_y):
    if direct == 'u' and coor_y < RobotsGame.TOP_EDGE:
      coor_y += 1
    elif direct == 'd' and coor_y > RobotsGame.BOTTOM_EDGE:
      coor_y -= 1
    elif direct == 'r' and coor_x < RobotsGame.RIGHT_EDGE:
      coor_x += 1
    elif direct == 'l' and coor_x > RobotsGame.LEFT_EDGE:
      coor_x -= 1  
    self.x = coor_x
    self.y = coor_y

  def move(self):
    key = update_when("key_pressed")
    moves = {
    '1': ['d', 'l'],
    '2': ['d'],
    '3': ['d', 'r'],
    '4': ['l'],
    '5': [],
    '6': ['r'],
    '7': ['u', 'l'],
    '8': ['u'],
    '9': ['u', 'r']
  }
    while True:
      if key in moves:
        while key == RobotsGame.TELEPORT_KEY:
          if RobotsDisplay.teleports > 0:
            self.teleport()
          key = update_when("key_pressed")
        else:
          for move in moves[key]:
            self.movement(move, self.x, self.y)
        break
      else:
        key = update_when("key_pressed")
        continue

    move_to(self.shape, (10 * self.x, 10 * self.y))

class Robot:
  def __init__(self):
    self.place()

  def place(self):
    self.x = randint(RobotsGame.LEFT_EDGE, RobotsGame.RIGHT_EDGE)
    self.y = randint(RobotsGame.BOTTOM_EDGE, RobotsGame.TOP_EDGE)

  def safely_place_robot(self):
    self.shape = Box((10 * self.x, 10 * self.y), 10, 10, filled=True, color=RobotsGame.ROBOT_COLOR)

  def move(self, player):
    if self.x < player.x:
      self.x += 1
    elif self.x > player.x:
      self.x -= 1

    if self.y < player.y:
      self.y += 1
    elif self.y > player.y:
      self.y -= 1

    move_to(self.shape, (10 * self.x, 10 * self.y))

game = RobotsGame()

while not game.finished:
  game.next_move()

game.over()
