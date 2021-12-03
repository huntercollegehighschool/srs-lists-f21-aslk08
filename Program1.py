'''
*********
PROGRAM 1
*********
Define a function number_of_odds that takes a list of integers as an argument. The function returns how an integer, how many odd numbers are in the list.
'''
def number_of_odds(lst):
  tot = 0
  for num in lst:
    if num % 2 == 1:
      tot += 1
  return tot
