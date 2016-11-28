# set myNumber to 42.  Set myName to your name.  Now swap myNumber into myName and vice versa

# def swap(myNumber, myName):

#   temp = myNumber
#   myNumber = myName
#   myName = temp

#   return myNumber, myName

# print swap(42, 'Jenna')



# print integers from -52 to 1066 using a for loop

# def numbers(a, b):

#   for i in range(a, b + 1):
#     print i

# numbers(-52, 1066)



# create beCheerful(). Within it, print string 'good morning!' Call it 98 times

# def beCheerful(a):

#   print a * 98

# beCheerful('good morning!')



# using FOR, print multiples of 3 from -300 to 0.  Skip -3 & -6

# def multiples(a, b):

#   for i in range(a, b + 1):
#     if (i % 3 == 0) and (i != -3) and (i != -6):
#       print i

# multiples(-300, 0)



# print integers from 2000 to 5280 using WHILE

# def numbers(a, b):

#   while a <= b:
#     print a
#     a = a + 1

# numbers(2000, 5280)



# if 2 given numbers represent your birth month and day in either order, print 'how did you know?' else print 'just another day...'

# def birthday(a, b):

#   month = 2
#   day = 1

#   if (a == month or a == day) and (b == month or b == day):
#     print 'how did you know?'   
#   else:
#     print 'just another day...'

# birthday(1,3)



# write a function that determines whether a given year is a leap year.  If a year is divisible by four, it is a leap year, unless it is divisible by 100.  However, if it is divisible by 400 then it is.

# def leapYear(year):

#   if year % 400 == 0:
#     return "leap year!"
#   elif year % 100 == 0:
#     return 'not a leap year.'
#   elif year % 4 == 0:
#     return 'leap year!'
#   else:
#     return 'not a leap year.'

# print leapYear(2016)



# print all integer multiples of 5 from 512 to 4096. Afterward, also log how many there were.

# def printCount():

#   count = 0

#   for i in range(512, 4097):
#     if i % 5 == 0:
#       print i
#       count += 1
#   print count

# printCount()



# print multiples of 6 up to 60000 using a while

# def mult():

#   i = 1

#   while i <= 60000:
#     if i % 6 == 0:
#       print i
#     i = i + 1

# mult()



# print integers 1 to 100. If divisible by 5, print 'Coding' instead.  If by 10, also print ' Dojo'.

# def dojoWay():

#   message = 'Coding'

#   for i in range(1, 101)
#     if i % 10 == 0:
#       print message + ' Dojo'
#     elif i % 5 == 0:
#       print message
#     else:
#       print i

# dojoWay()



# your function will be given an input parameter INCOMING.  Please console.log this value

# def youKnow(incoming):

#   print incoming

# youKnow('hello')



# add odd integers from -300000 to 300000 and print the final sum.  Is there a shortcut?

# def huge():

#   sum = 0

#   for i in range(-300000, 300001):
#     if i % 2 != 0:
#       sum = sum + i
#   print sum

# huge()



# log all positive numbers starting at 2016, counting down by fours (exclude 0), without a four loop

# def countdown():

#   i = 2016   
  
#   while i > 0:
#     print i
#     i -= 4

# countdown()



# given lownum, highnum, mult print multiples of mult from highnum down to lownum using a for

# def flex(lownum, highnum, mult):

#   # for i in reversed(range(lownum, highnum + 1)):
#   #   if i % mult == 0:
#   #     print i
#   #     i -= 1


#   for i in range(highnum, lownum - 1, -1):
#     if i % mult == 0:
#       print i


# flex(2,9,3)



# def finalCountdown(param1, param2, param3, param4):

#   i = param2

#   while i <= param3:
#     if i == param4:
#       pass
#     elif i % param1 == 0:
#       print i
#     i += 1


# finalCountdown(3,5,17,9)


















