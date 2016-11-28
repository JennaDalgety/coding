# collatz sequence starts at any integer (n) 
# if n is even
# n = n / 2

# if odd
# n = 3n + 1

# compute a collatz sequence where n = 13

# def collatz(num):

#   listy = []
#   listy.append(num)
  
#   while num > 1:
    

#     if not num % 2:
#       num = num / 2
#     else:
#       num = (3*num) + 1

#     listy.append(num)

#   return listy

# print collatz(13)


# which starting number produces the longest sequence under 1000000? (837799)

# store each listy length in a variable
# check to see if the next listy length is longer than the preceding one
# if so, store that in a new variable
# return the num

def long_collatz():

  count = 0
  listy_length = 0
  longest_length = 0
  answer = 0

  while count < 1000000:
    print count
    num = count
    listy = []
    listy.append(num)
    while num > 1:
      if not num % 2:
        num = num / 2
      else:
        num = (3*num) + 1
      listy.append(num)
    listy_length = len(listy)
    if listy_length > longest_length:
      longest_length = listy_length
      answer = count
    count = count + 1
  return answer

print long_collatz()










