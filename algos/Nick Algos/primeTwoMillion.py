# find the sum of all prime numbers under 2 million (a number divisible only by one and itself)


#pseudocode

# if num % 2 != 0 or num % 3 != 0

# if(num / 1 == num) and ((num % 2 != 0) or (num % 3 != 0)):
#   print num

# if num % 2 == 0
#   num = False
# elif num % 3 == 0
#   num == False

# else:
#   num == True
# #if num is only divisible by one
# if num / 1 == 0
# #and itself
# and num / num == 0

#trial by division

def is_prime(num):
  
  if num < 2:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
  return True



def sum_prime(num):

  sum = 0

  for i in range(1, num + 1):
    if is_prime(i) == True:
      sum = sum + i

  return sum

print sum_prime(2000000)












