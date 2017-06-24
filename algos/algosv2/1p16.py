# def set_swap(myNumber, myName):

#   temp = myNumber
#   myNumber = myName
#   myName = temp

#   return myNumber, myName

# print set_swap(36, 'Jenna')


# def print_int(x, y):

#   for i in range(x, (y + 1)):
#     print i

# print_int(-52, 1066)


# def beCheerful():

#   print('good morning!' * 98)

# beCheerful()


# def mult():

#   for i in range(-300, 1):
#     if i % 3 == 0:
#       if i == -3 or i == -6:
#         continue
#       else:
#         print(i)

# mult()


# def print_int():

#   i = 2000

#   while i <= 5280:
#     print i
#     i += 1

# print_int()


def birthday((x,y)):

  tupley = (4, 28)
  reversed_input = (y,x)
  
  if (x, y) == tupley or reversed_input == tupley[::-1]:
    print('How did you know?')
  else:
    print('Just another day....')

birthday((28,4))