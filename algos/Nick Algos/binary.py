# create a function that takes a number and returns its binary format as a string; create the inverse, as well; no FOR loops; variables should be ' name of whatever we name it ' _ ' type '; i.e. binary_int


def power2(num_int):  # this function will find the power of two that is one bigger than the number you're passing in to the binary function

  a_int = 1

  while (2**a_int < num_int):  # while 2 to the power of a_int is less than the num_int being evaluated:
    a_int = a_int + 1   #  a_int is added by one and then that new value gets stored back into a_int

  return a_int  #  this will allow you to pass a_int out of this function and into the binary function

def binary(num_int):

  binary_str = ''

  if num_int % 2 != 0:  # if the num_int we're passing in is odd...
    binary_str = '1' 
    num_int = num_int - 1   # calculates num_int - 1 and then stores the result of that operation back into num_int (this is how we drop the last slot) 
  else:   # if the num_int we're passing in is even...
    binary_str = '0'

  power2_int = power2(num_int)
      
  while ():
    power2_int = power2_int - 1



binary(5) # should be 0101



# what is the power of two one slot bigger than the number you're trying to hold:
# 8 (or 2 to the power of 3)
# Is 8 < 5?
# No, so it's a 0
# What is the next power of two to the next slot?
# 4 (or 2 to the power of 3 minus 1)
# Is 4 < 5?
# Yes, so it's a 1
# Then we decrease the number you're trying to hold by the number you're testing it against (4, in this case)
# 5 - 4 = 1
# what is the next power of two to the next slot?
# 2 (or 2 to the power of 2 minus 1)
# Is 2 < 1?
# No, so it's a 0
# What is the next power of 2 to the next slot?
# 1 (or 2 to the power of 1 - 1)
# When we get to the 1 slot we can stop the check and either insert a 0 or 1 depending on if the number you're trying to hold being even or odd

# 1, 2, 4, 8, 16, 32, etc.
