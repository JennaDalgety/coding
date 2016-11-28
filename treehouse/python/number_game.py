import random

def game():
  
  number = random.randint(1, 10)
  count = 0
  print('''
  Welcome to the number guessing game!  
  I'm thinking of a number between 1 and 10.  
  You get 3 tries.
  ''')
  
  while count < 3:
    try:
      guess = int(raw_input('> '))
      count += 1
    except ValueError:
      print('Please enter a number')
    else:
      if guess == number:
        print('You got it! The number was {}'.format(number))
        break
      elif guess < number:
        print('Too low!')
      else:
        print('Too High!')
  else:
    print('The number was {}.  You lose.'.format(number))
    
  # print('Would you like to play again? Press 1 for yes, 2 for no')
  # play_again = input('> ')
  # if play_again == int(1):
  #   game()
  # else:
  #   print('Thanks for playing!')

  print('Would you like to play again Y/N?')
  play_again = raw_input('> ')
  if play_again.lower() == 'y':
    game()
  else:
    print('Thanks for playing!')
  
  
game()