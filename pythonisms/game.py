from linked_list import LinkedList
from functools import wraps
from time import sleep, time

countdown_timer_time = 10


def countdown_timer_speed(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    sleep(.5)
    orig_val = func(*args, **kwargs)
    return orig_val 
  return wrapper

def game_timer(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    t1 = time()
    result = func(*args, **kwargs)
    t2 = time()
    print(f'What a quick game! Gameplay time was {(t2 - t1):.4f}s')
    return result
  return wrapper

@countdown_timer_speed
def aw_shucks():
  print(f'Only {countdown_timer_time} seconds remain until your computer detonates')

@game_timer
def play_game():
  print('Perfect! So now all you have to do is confirm that you are in fact ready to have fun. (y/n)')
  game_time_spender = input('> ')
  if game_time_spender == 'y':
    return
  
  if game_time_spender == 'n':
    aw_shucks()


##### Start of actual game #######

print('Hello and welcome to a goofy lil Python Game!')
print('Are you down to clown and have some fun? (y/n)')
fave_color = input('> ')

if fave_color == 'n':
  print('well thats unfortunate, on just a whole bunch of fronts')
  sleep(1)
  while countdown_timer_time > 0:
    aw_shucks()
    countdown_timer_time -= 1
  sleep(.5)
  print('boom')

if fave_color == 'y':
  play_game()


