numbers = [1,2,3,4,5]
#print(numbers)

fruits = ["apple", "banana", "cherry"]
#print(fruits)

mixed = ["hello", 5, True, None]

numbers.append(6)
#print(numbers)

mixed.insert(1,False)
print(mixed)
#fruits.remove("banana") fruits.pop(1) same thing
print(fruits)

for fruit in fruits:
	print(fruit)

colors = ["red", "yellow", "green"]
print(colors[1])
print(colors[-1])
colors.append("black")
for color in colors:
	print(color)

print(numbers[:3])

my_nums = [20, 40, 60, 80, 100, 120]
print(my_nums[::2])

student = {
	"name": "Everett",
	"year": 2,
	"Major": "Astro"
}
#print(student["year"])
#del(student["Major"])
print(student.keys())
#print(student.values())
#print(student.items())
student["year"] = 2.5

for key in student:
	print(f"{key} = {student}")

