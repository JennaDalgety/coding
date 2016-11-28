# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.



# def multiples(limit):

#   sum = 0

#   for i in range(limit):
#     if (i % 3 == 0) or (i % 5 == 0):
#       sum = sum + i

#   return sum

# print multiples(1000)


def fib(limit):

  sum = 0

  a = 1
  b = 2
  c = a + b

  for i in range(10):
    a = b
    b = c
    if c < 4000000:
      if i % 2 == 0:
        sum = sum + i

  return sum

print fib(4000000)