import random

def game():
  
  heads_count = 0
  tails_count = 0
  attempt = 0

  print('Welcome to the Coin Toss game!')
  print('press T to toss the coin and E to end the game')
  while attempt > -1:
    try:
      play_again = raw_input('> ')
    except ValueError:
      print('Please enter T or E')
    else:
      if play_again.lower() == 't':
        attempt += 1
        
        coin = random.randint(1,2)
        if coin == 1:
          heads_count += 1
          print("Attempt {}: Throwing a coin... It's a head!  ... Got {} head(s) so far and {} tail(s) so far".format(attempt, heads_count, tails_count))
          print('press T to toss the coin and E to end the game')
        else:
          tails_count += 1
          print("Attempt {}: Throwing a coin... It's a tail!  ... Got {} head(s) so far and {} tail(s) so far".format(attempt, heads_count, tails_count))
          print('press T to toss the coin and E to end the game')
    if play_again.lower() == 'e':
        print('Thanks for playing!')
        return
    else:
      print('Please enter T or E')
  

game()