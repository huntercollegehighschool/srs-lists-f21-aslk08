'''
*********
PROGRAM 4
*********
Define a function above_average that takes a list of integers or floats as an argument. The function will identify the mean of the list, identify the numbers in the list that are greater than the mean, and then return those numbers in a list.

You may define a separate function that finds the average of a list, though you don't have to.
'''
def above_average(lst):
  new = []
  av = sum(lst)/len(lst)
  for num in lst:
    if num > av:
      new.append(num)
  return new
