# given a string, find every permutation of that string

# def permutation(word):
  


# print permutation('has')


# 1. create an empty master list variable
# 2. create an empty sub list variable
# 3. get the length of the string
# 4. for loop through the string
# 5. append each letter to sub list
# 6. pop beginning letter of string and append it to the end of the string
# 7. check to see if this sub list exists in the master list
# 8. if not, append this new list to a master list
# 9. else continue
# repeat steps 5 - 9


# door
# door
# doro
# droo
# rdoo
# rdoo
# rodo
# ordo
# ordo
# orod
# oord
# oodr



# perm = num * num-1 * num-2 * num-3 # this is a range of the length of the string, 0, 1, 2, 3

number = 4
x = number

while number > 0:
  x = x * number - 1
  number = number - 1 

print x

  















