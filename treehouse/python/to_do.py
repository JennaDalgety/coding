list = []

def show_help():
  print('What do you want to add to your list?')
  print('''
type "SHOW" to show current list 
type "HELP" to show a list of app commands
type "DONE" to stop adding items
''')

def show_list():
  print('Here is your list:')
  for item in list:
    print(item)
    
def add_items(new_item):
  
  list.append(new_item)
  print('Added {} to list.  List now has {} items'.format(new_item, len(list)))
        

def main():
  
  show_help()
  
  while True:
    new_item = input('> ')
    
    if new_item == 'DONE':
      break
      
    elif new_item == 'HELP':
      show_help()
      continue
    elif new_item == 'SHOW':
      show_list()
      continue
    add_items(new_item)
          
    
  show_list()