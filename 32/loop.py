# -*- coding:utf-8 -*-
the_count = [1,2,3,4,5]
fruites = ["apple", "orange", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

for numbers in the_count:
    print("This is count %d" % numbers)

for fruit in fruites:
    print("A fruit of type: %s" % fruit)

for i in change:
    print("I got %r" % i)

elements = []

for i in range(0, 6):
    print("Adding %d to the list." % i)
    elements.append(i)

for i in elements:
    print("Element was: %d" % i)