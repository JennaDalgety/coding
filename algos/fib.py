# find every fibonacci term that does not exceed 4000000 and is even.  Return sum of terms.


# def fib(num):
  
#   a = 1
#   b = 1
#   sum = 0

#   while b < num:
#     c = a + b
#     a = b
#     b = c
#     if not b % 2:
#       sum = sum + b
#       print b



# fib(400)

# temp1 = 
# temp2 = 
# a = 0
# b = 1
# c = a + b
# d = b + c
# e = c + d

# the fibonacci sequence is that each value is the sum of the two preceding values

# find every fibonacci term that is even and does not exceed 4000000.  Return the sum of these terms.

def fib(limit):

  sum = 0

  temp1 = 0
  temp2 = 1
  temp3 = temp1 + temp2
  while temp3 <= limit:
    temp1 = temp2
    temp2 = temp3
    temp3 = temp1 + temp2
    if not (temp3 % 2):
      sum = sum + temp3

  return sum

print fib(4000000)





