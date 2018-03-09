#notes from running the following program
#What did you see on Line 1: Line 1 contained integers only ranging from 5 to 20
#What was the smallest number you could have seen and what was the largest? Smallest = 5, Largest = 20

#What did you see on Line 2: Line 2 to were only odd numbers.
#What was the smalles number you could have seen, what was the largest? Smallest = 3, Largest = 9

#What did you see on Line 3? Line 3 were float-point numbers with a large number of digits past the decimal point.
#What was the smallest number you could have seen, what was the largest? Smallest = 2.5, Largest = 5.5

import random

print(random.randint(5,20))     #Line 1
print(random.randrange(3,10,2)) #Line 2
print(random.uniform(2.5,5.5))  #Line 3
