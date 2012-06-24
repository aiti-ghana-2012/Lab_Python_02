"""
Lab_Python_02
Solutions for Part II - Computer Exercises
"""



theInput = int(raw_input("Enter an integer: "))

## Question 5

# remember, 1 is True, and 0 is False
# so we can use the return value of the %
# operator directly as a condition
if theInput % 2:
	print 'odd'
else:
	print 'even'


## Question 6
print "--------"

# ages for my home
primarySchoolAge = 6
legalVotingAge = 18
presidentAge = 35
retirementAge = 65

givenAge = int(raw_input("Enter an age: "))

if givenAge < primarySchoolAge:
	print "Too young"

if givenAge >= legalVotingAge:
	print "Remember to vote!"

if givenAge >= presidentAge:
	print "Vote for me!"
else:
	print "You can't be president"

if givenAge >= retirementAge:
	print "Too old"


## Question 7
print "--------"

# with a for loop and range:
for i in range(39,-1,-3):
	print i

# with a while loop
i = 39
while i > -1:
	print i
	i -= 3


## Question 8
print "--------"

for i in range(6,31): #remember, the default step is 1, and the second argument is exclusive
	if i % 2 and i % 3 and  i % 5:
		print i	

## Question 9
print "--------"

n = 1
while True:
	if (79 * n) % 97 == 1:
		break #this statement exits the loop, without executing the next one
	n += 1
print n
