"""
Lab_Python_02
Extra Credit
Solutions for Extra Credit Question 1
"""


# getting input from the user
unencrypted = int(raw_input("Enter a number to encrypt: "))

encrypted = 0

while unencrypted > 0:
	
	# multiplying the encrypted number by 10
	encrypted *= 10
	
	# adding the last digit of what is left of the unencrypted number to it
	encrypted += unencrypted % 10
	
	# shortening the unencrypted number
	unencrypted //= 10


print "The encrypted number is %d" % encrypted
