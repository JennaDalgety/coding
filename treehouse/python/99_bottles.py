start = 99
while start:
  print("{} bottles of beer on the wall".format(start))
  print("{} bottles of beer.".format(start))
  print("Take one down, pass it around")
  start -= 1
  print("{} bottles of beer on the wall.".format(start))
  if start == 0:
    print('All outta beer')