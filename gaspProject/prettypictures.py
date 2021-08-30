from gasp import *

begin_graphics()

def draw_person(x, y):
  Circle((x, y), 40) # face
  Circle((x - 15, y + 10), 5) # left eye
  Line((x - 25, y + 20), (x - 10, y + 25)) # left brow
  Circle((x + 15, y + 15), 5) # right eye
  Line((x + 5, y + 25), (x + 20, y + 30)) # right brow
  Arc((x, y), 30, 225, 90) # mouth
  Line((x - 15, y - 10), (x + 3, y), thickness=1) # nose top
  Line((x - 15, y - 10), (x + 5, y - 10), thickness=1) # nose bottom
  Arc((x + 30, y), 15, 298, 125)# right ear
  Arc((x - 30, y), 15, 128, 118) # left ear
  Arc((x, y + 20), 50, 328, 238) # hair
  Line((x, y - 40), (x, y - 120), thickness=1) # body
  Line((x, y - 60), (x + 40, y - 100), thickness=1) # right arm
  Line((x, y - 60), (x - 40, y - 100), thickness=1) # left arm
  Line((x, y - 120), (x + 20, y - 170), thickness=1) # right leg
  Line((x, y - 120), (x - 20, y - 170), thickness=1) # left leg
  Line((x - 60, y + 60), (x + 60, y + 60)) # hat
  Box((x - 25, y + 60), 50, 70, filled=True) # hat

draw_person(300, 240)
draw_person(480, 240)
draw_person(120, 240)

update_when('key_pressed')

end_graphics()