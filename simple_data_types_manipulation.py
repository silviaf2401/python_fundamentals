#print even numbers from 1 to 1000
for count in range(1,1001):
	if count%2 != 0:
		print count
#print multiple of 5 from 5 to 10^6
for count in range(5,1000001):
	if count%5 ==0:
		print count

#print all values in list a
a = [1,2,5,10,255,3]
for value in a:
	print value

#print the averate of values in list a
sum = 0
for value in a:
	sum +=value
average = sum/len(a)
print "The average is {}".format(average)

# Create a function that counts from 1 to 2000. 
#As it loops through each number, have your program generate the number 
#and specify whether it's an odd or even number.
def odd_or_even(a,b):
	for count in range(a,b+1):
		if count%2 !=0:
			print "Number is {}. This is an odd number.".format(count)
		else:
			print "Number is {}. This is an even number.".format(count)

odd_or_even(1,2000)

#Create a function called 'multiply' that reads each value in the list (e.g. a = [2, 4, 10, 16]) 
#and returns a list where each value has been multiplied by 5. (e.g. b = [10,20,50, 80])
def multiply(a,b):
	c=[]
	for element in a:
		c.append(element*b)
	print c

multiply([1,2,3,4,5],2)

#Create a program that prompts the user 5 times for a test score between 60 and 100. 
#Each time a score is generated, your program should display what is the grade of that score. 
#Here is the grade table:
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

counter =0
while counter <5:
	user_input = input("What is your test score? Enter a value between 60 and 100"+ "\n")
	if user_input in range (90,101):
		print "Score {}. Your grade is an A.".format(user_input)
		counter +=1
	elif user_input in range (80,90):
		print "Score {}. Your grade is a B.".format(user_input)
		counter +=1
	elif user_input in range (70,80):
		print "Score {}. Your grade is a C.".format(user_input)
		counter +=1
	elif user_input in range (60,70):
		print "Score {}. Your grade is a D.".format(user_input)
		counter +=1
	else:
		print "The score you entered is not between 60 and 100, please try again"

#Create a program that simulates tossing a coin 10 times. Your program should display how many times the head/tail appears.
# Sample output should be like the following:

#           Starting the program...

# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far 
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far 
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far 
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ........
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far 

# Ending the program, thank you!

import random
heads = 0
tails = 0
print "Starting the program..."
for counter in range(1,11):
	result = random.randint(0,1)
	if result ==1:
		heads +=1
		print "Attempt #{}: Throwing a coin ... It's a head!... Got {} head(s) so far and {} tail(s) so far".format(counter,heads, tails)
	else:
		tails+=1
		print "Attempt #{}: Throwing a coin... It's a tail!.. Got {} head(s) so far and {} tail(s) so far".format(counter, heads, tails)
print "Ending the program, thank you!"



# Part1
# Create a function called  draw_stars() that takes a list of numbers and prints out  *.
# For example:
# x = [4, 6, 1, 3, 5, 7, 25]
# draw_stars(x) should print the following in when invoked:
# **** 
# ****** 
# * 
# *** 
# ***** 
# ******* 
# *************************

def draw_stars(my_list):
	for element in my_list:
		print element*'*'+'\n'

draw_stars([1,2,3])

# Part 2

# Modify the function above. Allow a list containing integers and strings to be passed to the  draw_stars() function. 
#When a string is passed, instead of  displaying *, display the first letter of the string according to the example below.
# For example:
#  x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
# draw_stars(x) should print the following in the terminal:
# **** 
# ttt 
# * 
# mmmmmmm 
# ***** 
# ******* 
# jjjjjjjjjjj


def draw_stars_two(my_list):
	for element in my_list:
			if type(element)==int:
				print element*'*'+'\n'
			elif type(element)==str:
				print element[0].lower()*len(element)+'\n'
			else:
				continue

draw_stars_two([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])

