name = "Everett"
print("Hello,", name)
def add(a,b):
	print(a + b)
# add(1,2)

def add(a,b):
	return a+b
c = add(a=42,b=69)
print(c)

def check_number(num):
	if num > 0:
		return "Positive"
	elif num < 0:
		return "Negative"
	else: return "0"

print(check_number(0))

def can_vote(age, is_citizen):
	if age >= 18 and is_citizen:
		print("hooray vote")
	elif age < 18 and is_citizen:
		print("wait")
	else: print("no vote for you")
can_vote(19, True)

def is_weekend(day):
	if day == "Saturday" or day == "Sunday":
		return "Weekend"
	else: return "go to work :("
print(is_weekend("Monday"))

fruits = ["Apple", "Banana", "Cherry"]
def print_fruits(fruits): 
	for fruit in fruits:
		print(fruit)
print_fruits(fruits)

def countdown(start):
	while start > 0:
		print(start)
		start = start - 1
	print("liftoff")
countdown(3)
