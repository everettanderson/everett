def say_goodbye(name):
	return f"Hello, {name}"
#print(say_goodbye("you"))

def circle(radius):
	return 3.14 * (radius**2)
#print(circle(2))

def subtract(a,b):
	return a -  b
def multiply(a,b):
	return a * b
def divide(a,b):
	if b == 0:
		return ":("
	else: return a / b

def weather(a):
	return min(a), max(a)
#print(weather([1,2,3,4,5,6,3,2,0]))

def is_weekend(day):
	if day == 6 or day == 7: #don't say it
		return "It's the weekend!"
	else: return "It's not the weekend."
#print(is_weekend(7))

def efficiency(miles, gallons):
	return miles / gallons
#print(efficiency(23,1))

def secret(n):
	return n // 10 + ((n%10)*10000)
#print(secret(12345))

def oski(x,y):
	temp = x
	if y >=0: 
		while y > 1:
			temp = temp * x
			y = y-1
	else: 
		while y <= 0:
			temp = temp / x
			y = y + 1
	return temp
#print(oski(2,-3))

def minimum(a):
	currentmin = a[0]
	for num in a:
		if num < currentmin:
			currentmin = num
	return currentmin
#print(minimum([8,4,7,3,6,5]))

def maximum(a):
	currentmax = a[0]
	for num in a:
		if num > currentmax:
			currentmax = num
	return currentmax
#print(maximum([5,6,3,10,2,7]))

def minwhile(a):
	counter = 0
	currentminwhile = a[0]
	while counter < len(a):
		if a[counter] < currentminwhile:
			currentminwhile = a[counter]
		counter = counter + 1
	return currentminwhile
#print(minwhile([3,4,5,2,8,6]))

def maxwhile(a):
	counter = 0
	currentmaxwhile = a[0]
	while counter < len(a):
		if a[counter] > currentmaxwhile:
			currentmaxwhile = a[counter]
		counter = counter + 1
	return currentmaxwhile
#print(maxwhile([3,4,5,2,8,6]))

def sumofnumbers(a):
	length = len(str(a))
	counter = 1
	currentsum = 0
	while counter <= length:
		currentsum = currentsum + (a%(10 ** counter))//(10 ** (counter - 1))
		counter = counter + 1
	return currentsum
#print(sumofnumbers(123))

value = 5326
result = sumofnumbers(value)

print(f"The result of Calculate the Sum (6.3) with the input {value} is {result}")
