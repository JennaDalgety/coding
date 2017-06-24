# make monster move
# leave breadcrumbs for rooms you've visited
# fix running into wall print function


import random

size = 8 # test size

DUNGEON = []
for x in range(size):
  for y in range(size):
    DUNGEON.append((x,y))
    


def get_locations():
  
  monster = random.choice(DUNGEON)
  door = random.choice(DUNGEON)
  player = random.choice(DUNGEON)
  
  if monster == door or monster == player or door == player:
    return get_locations()
  else:
    return monster, door, player
  
  
def move_player(player, move):
  
  x, y = player
  
  if move == 'LEFT':
    y -= 1
  elif move == 'RIGHT':
    y += 1
  elif move == 'UP':
    x -= 1
  elif move == 'DOWN':
    x += 1
  return x, y


def move_monster():
  
  monster = random.choice(DUNGEON)
  
  if monster == door:
    return move_monster()
  else:
    return monster


def get_moves(player):
  
  moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
  
  if player[1] == 0:
    moves.remove('LEFT')
  if player[0] == 0:
    moves.remove('UP')
  if player[1] == size - 1:
    moves.remove('RIGHT')
  if player[0] == size - 1:
    moves.remove('DOWN')
  return moves


def draw_map(player):
  
  dungeon_lid = ' _' * size
  print(dungeon_lid)
  tile = '|{}'
  dungeon_array = []
  
  for i in range(len(DUNGEON)):
    if (i + 1) % (size) == 0:
      dungeon_array.append(i)
  
  for idx, cell in enumerate(DUNGEON):
    if idx not in dungeon_array:
      if cell == player:
        print(tile.format('X'), end='')
      elif cell == monster:
        print(tile.format('O'), end='')
      else:
        print(tile.format('_'), end='')
      
    else:
      if cell == player:
        print(tile.format('X|'))
      elif cell == monster:
        print(tile.format('O|'))
      else:
        print(tile.format('_|'))
        
         


monster, door, player = get_locations()
print('Welcome to the dungeon!')


while True:
  moves = get_moves(player)
  print('You are currently in room {}'.format(player))
  draw_map(player)
  print('You can move {}'.format(moves))
  print('Enter QUIT to quit')
  
  move = input('> ')
  move = move.upper()
  
  if move == 'QUIT':
    break
    
  if move in moves:
    player = move_player(player, move)
    monster = move_monster()
  else:
    print('** walls are hard...stop walking into them **')
    continue
    
  if player == door:
    print("Congratulations, adventuror! You've escaped the dungeon!")
    break
  elif player == monster:
    print("You've been ripped limb from limb by the monster.  Sorry about your life.")
    break
    
