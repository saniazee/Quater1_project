import time


def countdown_timer(t):


  while t:
    mins,secs= divmod(t,60)
    timer = '{:02d}:{:02d}'.format(mins,secs)
    print(f'\r{timer}',end='')
    time.sleep(1)
    t -=1


  print("Time's up")





countdown_timer(50)