# -*- coding: utf-8 -*-
"""mcnugget_solver.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KXF_9gkzbDXgD72JwizIEZrWIKcsb0Uy
"""

import numpy as np
import itertools

from functools import reduce

def factors(n):
    thisSet = set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    thisSet.remove(1)
    return thisSet

def mcnugget_solver(list1):
  list1 = sorted(list1)
  minimum = list1[0]
  list2 = []
  for i in np.arange(1, len(list1)):
    list2.append(list1[i])

  list4 = []
  for number in list2:
    for i in np.arange(minimum):
      list4.append(number)

  list5 = []
  for i in np.arange(len(list4)):
    for j in list(itertools.combinations(list4, i)):
      list5.append((np.sum(j), np.sum(j) % minimum))

  list5_sorted = sorted(list5, key=lambda x: (x[0], x[1]))
  list5_sorted.sort(key=lambda x: x[0])

  list6 = []


  for j in np.arange(minimum):
    count = 0
    for i in np.arange(len(list5_sorted)):
      if list5_sorted[i][1] == j:
        count += 1
      if count == 1:
        list6.append(list5_sorted[i][0])
        count = 2




  for i in factors(min(list1)):
    count = 0
    for j in list1:
      if j % i == 0:
        count += 1
    if count == len(list1):
      return "Numbers have a common factor of " + str(i) + " when they need to be relatively prime. Result is therefore infinite."



  return max(list6) - minimum

def reverse_mcnugget_solver(x, list1):
  minimum = sorted(list1)[0]
  list2 = []
  for element in list1:
    for i in np.arange(minimum):
      list2.append(element)
  list3 = []
  for i in np.arange(len(list2)):
    for j in list(itertools.combinations(list2, i)):
      if np.sum(j) % minimum == x % minimum:
        list3.append((np.sum(j), j))
  list3.sort(key=lambda x: x[0])
  solution_tuple = list3[0]
  solution_list = []
  list1.remove(minimum)
  for element in list1:
    solution_list.append((element, solution_tuple[1].count(element)))
  if solution_tuple[0] > x:
    return "There is no solution"
  else:
    y = int((x - solution_tuple[0])/minimum)
    solution_list.append((minimum, y))
    solution_list.sort(key=lambda x: x[0])
    return solution_list

print(mcnugget_solver([5,9]))