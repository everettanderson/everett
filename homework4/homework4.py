foods = ["cherry", "strawberry", "pineapple", "mango", "peach"]

#print(foods[1])
#print(foods[-1])
foods.append("raspberry")
foods.insert(0, "apple")
del foods[2]
#print(len(foods))

#for food in foods:
#	print(food.upper())

foods2 = foods[0:len(foods):(len(foods) - 1)]

potatostatus = False
for food in foods2:
	if food == "potato":
		potatostatus = True
#if potatostatus == True:
#	print("A potato!")
#else: print("No potato!")

#3 errors while executing:
#NameError: name 'potatostatus' is not defined. I did not 
#define potatostatus before the if statement, so it didn't exist outside the
#if statement.
#2: AttributeError: 'list' object has no attribute 'upper'. I wrote print(foods.upper)
#I should have written food.upper because food is the traversing variable, foods
#is the entire list.
#3: TypeError: 'str' object cannot be interpreted as an integer. I wrote
#foods.insert("apple", 0) but the string and position are inverted. It should be
#foods.insert(0, "apple")

numbers = list(range(21))


def get_first_15(numbers):
	output1 = []
	i = 0
	while i < 15:
		output1.append(numbers[i])
		i = i + 1
	return output1
#print(get_first_15(numbers))

output2 = []
def get_every_5th(output1):
	i = 0 
	while i < len(output1) / 5:
		output2.append(output1[5 * i])
		i = i + 1
	return output2
#print(get_every_5th(output1))

output3 = []
def reverse_and_stride(output2):
	i = 1
	while i <= len(output2):
		output3.append(output2[len(output2) - i])
		i = i + 1
	return output3[2::3]
#print(reverse_and_stride(output2))

numbers = [[1,2,3],[4,5,6],[7,8,9]]
#print(numbers[2])
#for number in numbers:
	#print(number[1])
#numbers.append([10,11,12])

def sum_nested(numbers):
	sum = 0
	for row in numbers:
		for column in row:
			sum = sum + column
	return sum
#print(sum_nested(numbers))

emptylist = []
def createlist(inputs):
	emptylist = []
	i = 0
	while i < len(inputs):
		emptylist.append([])
		i += 5
	for entry in inputs:
		emptylist[(entry - 1) // 5].append(entry)
	return emptylist

#print(createlist(list(range(1,26))))


def messuplist(numbers):
	for row in range(len(numbers)):
		for column in range(len(numbers[row])):
			if (numbers[row][column] % 3) == 0:
				numbers[row][column] = "?"
	return numbers


newlist = messuplist(emptylist)

#print(newlist)

def sumnumbers(newlist):
	sum = 0
	for row in newlist:
		for column in row:
			if column != "?":
				sum = sum + column
	return sum
#print(sumnumbers(newlist))

ages = { "Katie": 30, "Mariam": 42, "Safia": 25, "Mira": 48}

#print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]
for age in ages:
	print(f"{age}: {ages[age]}")
