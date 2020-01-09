import calendar


def date():
	print("enter the year :", "\n")
	a = int(input())
	print("enter the month:","\n")
	b = int(input())

	print("here is your input:","\n",calendar.month(a, b,4))


#date()

def answer():

	ans = str()
	print("do you want to predict month:","\n","yes or no")
	ans = str(input())
	while ans == "yes":
		date()
		print("do you want to perform this again?","\n","yes or no","\n")
		ans = str(input())

		
		
answer()
print("Thanks !")
	

