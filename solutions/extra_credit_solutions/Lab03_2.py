"""
Lab_Python_02
Extra Credit
Solutions for Extra Credit Question 1
"""


# getting input from the user
unencrypted = int(raw_input("Enter a number to encrypt: "))

encrypted = 0
encrypted_old = 0

while unencrypted > 0:
	
	# multiplying both the encrypted numbers by 10
	encrypted *= 10
	encrypted_old *= 10
	
	#getting the last digit of what is left of the unencrypted number
	new_digit = unencrypted % 10

	#adding the new digit to the old encryption method before we transform it
	encrypted_old += new_digit

	#transforming the new digit
	new_digit = (new_digit + 7) % 10

	#adding the new digit
	encrypted += new_digit
	
	# shortening the unencrypted number
	unencrypted //= 10


print "Using the old method, the encrypted number is %d" % encrypted_old
print "Using the new method, the encrypted number is %d" % encrypted
