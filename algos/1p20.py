# create a function that accepts a number as an input.  Return a new array that counts down by one, from the number (as array's 'zero'th element) down to 0 (as the last element).  How long is this array?

# def countdown(num):
  
#   array = []

#   for i in range(num, -1, -1):
#     array.append(i)

#   return array

# print countdown(10)



# your function will receive an array with two numbers. print the first value and return the second

# def printReturn(num1, num2):

#   array = [num1, num2]

#   print array[0]
#   return array[1]

# print printReturn(2, 1)






# def countdown(num1, num2, num3):

#   array = []

#   for i in range(num1, num2, num3):
#     array.append(i)
#   return array

# print countdown(10, 0, -1)


# def ranger(start, stop, step):  # this is how the range function

#   listy = []
  
#   while start != stop:
#     if step < 0:
#       if start < stop:
#         break
#     else:
#       if start > stop:
#         break
#     listy.append(start)
#     start = start + step

#   return listy

# # print ranger(1, 10, 1)

# # print ranger(9, 0, -1)

# print ranger(1, 9, 3)



# for i in range(9, 1, -1):

#   print i


# iterable = range(9, 1, -1)   # This is how a for loop works

# count = 0

# while count < len(iterable):
#   i = iterable[count]
#   print i
#   count = count + 1



# given an array, return the sum of the first value in the array, plus the array's length.  What happens if the array's first value is not a number, but a string (like 'what?') or a boolean (like false)

# def firstLength(array):

#   sum = array[0] + len(array)

#   return sum

# print firstLength([1, 2, 3, 4])



# you start with an IQ of 101.  If your IQ rises by .01 on the first day of a class and goes up .02 on the second day, .03 on the third day... how high will your IQ be on the 98th day?

# def iq(day):

#   start_iq = 101

#   increment = .01

#   for i in range(day):
#     increment = increment + .01
#     start_iq = start_iq + increment

#   return start_iq

# print iq(98)



# given two numbers (the coefficients M and B in the equation Y = MX + B), build a function that returns the X-intercept (the value of where Y equals 0)
# y = mx + b

# let y = 0, solve for x

# 0 = (m * x) + b
# 0 - b = (m * x) + b - b
# -b = (m * x) + 0
# -b = (m * x)
# -b / m = (m * x) / m
# -b / m = m / m * x
# -b / m = 1 * x
# -b / m = x

# 1000 + (500 * mo) = pay
# pay - 1000 / 500

def math(m, b):

  x = float(-b) / m

  return x

print math(88, 4)












