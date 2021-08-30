from gasp import *


GRID_SIZE = 30
MARGIN = GRID_SIZE

BACKGROUND_COLOR = color.BLACK
WALL_COLOR = "#99E5E5"


class Immovable:
  pass


class Nothing(Immovable):
  pass

class Wall(Immovable):
  def __init__(self, maze, point):
    self.place = point
    self.screen_point = maze.to_screen(point)
    self.maze = maze
    self.draw()

  def draw(self):
    (screen_x, screen_y) = self.screen_point
    dot_size = GRID_SIZE * 0.2
    Circle(self.screen_point, dot_size, color=WALL_COLOR, filled=True)

class Maze:
  def __init__(self):
    self.have_window = False
    self.game_over = False
    self.get_level()
    self.height = len(self.the_layout)
    self.width = len(self.the_layout[0])
    self.make_window()

  def get_level(self):
    f = open('layout.dat')
    self.the_layout = [line.rstrip() for line in f.readlines()]

  def make_window(self):
    grid_w = (self.width - 1) * GRID_SIZE
    grid_h = (self.height - 1) * GRID_SIZE
    screen_w = 2 * MARGIN + grid_w
    screen_h = 2 * MARGIN + grid_h
    begin_graphics(screen_w, screen_h, BACKGROUND_COLOR, "Chomp")

  def make_object(self, point, character):
    (x, y) = point
    if character == '%':
      self.map[y][x] = Wall(self, point)

  def set_layout(self, layout):
    self.make_window


  def finished(self):
    return self.game_over

  def play(self):
    answered = input("Are we done yet? ")
    if answered == "y":
      self.game_over = True
    else:
      print("I'm playing")

  def done(self):
    print("I'm done, and here's the_layout:")
    [print(line) for line in self.the_layout]


the_maze = Maze()
while not the_maze.finished():
  the_maze.play()
the_maze.done()

