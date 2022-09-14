from linked_list import LinkedList
from functools import wraps
from time import sleep

countdown_timer_time = 10


def countdown_timer_speed(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    sleep(1)
    orig_val = func(*args, **kwargs)
    return orig_val 
  return wrapper

@countdown_timer_speed
def aw_shucks():
  print(f'Only {countdown_timer_time} seconds remain until your computer detonates')

def play_game():
  pass


##### Start of actual game #######

print('Hello and welcome to a goofy lil Python Game!')
print('Are you down to clown and have some fun? (y/n)')
fave_color = input('> ')

if fave_color == 'n':
  print('well thats unfortunate, on just a whole bunch of fronts')
  while countdown_timer_time > 0:
    aw_shucks()
    countdown_timer_time -= 1
  print('boom')
  
if fave_color == 'y':
  play_game()


