# File: homework1.py

# --- Variables and Data Types ---

a = 10
print(a)
print(type(a)) #a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) #b is a float, a number with decimals

c = 3j
print(c)
print(type(c)) #c is a complex, a mix of numbers and letters

d = "hello"
print(d)
print(type(d)) #d is a string, a collection of letters

e = [1,2,3]
print(e)
print(type(e)) # e is a list, a collection of items

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dict, a collection of key and value pairs

g = (1,2)
print(g)
print(type(g)) # g is a tuple, a collection of numbers

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, a collection of items

i = True
print(i)
print(type(i)) # i is a boolean, a true/false value

j = None
print(j)
print(type(j)) # j is a nonetype, an empty value

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, a collection of items

l = str(14)
print(l)
print(type(l)) # l is a string, as str indicates the inside is a string

m = 1e4
print(m)
print(type(m)) #m is a float, a number that includes a decimal.
 
# 1. 9 types
# 2. integer, float, complex, string, list, dict, tuple, boolean, nonetype
# 3. e, h, k --- d,l --- b, m
# 4. l is a string because the str() function turns whatever is inside of it into a string
# 5. frozenset
set = ("one", "two")
o = frozenset(set)
print(o)
print(type(o))

print(10>9, #True
      10 == 9, #False
      10 <= 9, #False
      bool("abc"), #True
      bool(123), #True
      bool(["apple", "cherry", "banana"]), #True
      bool(True), #True
      bool(False), #False
      bool(0), #False
      bool(""), #False
      bool(" "), #True
      bool(()), #False
      bool([]), #False
      bool({}), #False
      bool (True and False), #False
      bool(True and True), #True
      bool(False and False), #False
      bool(True or False), #True
      bool(True or True), #True
      bool(False or False), #False
      bool(not(False)), #True
      bool(not(True))) #False

# 1. Expressions that have something are true and nothing are false, unless they are boolean expressions.
# 2. bool(" ") surprised me that it was true, as I didn't realize the computer was just looking for any value.
# 3. print(bool(str(False)), string function converts False from a boolean to a string
# 4. print(bool(True and True and False)), not limited to 2 inputs

print(
    10+5, #15, adds
    10-5, #5, subtracst
    2*4, #8, multiplies
    6/3, #2, divides
    5%2, #1, remainder 2
    3**2, #9, exponentiates
    15//2, #7, divides and rounds down
    5==2, #False, checks if they are equal
    10 !=10, #False, checks if they are unequal
    2<5, #True, checks if 2 is less than 5
    12>5, #True, checks if 12 is greater than 5
    5<=6, #True, checks if 5 is not greater than 6
    1>=10 #False, checks if 1 is not less than 10.
)

x = 5
x+=5 #adds 5
print(x)
x-=4 #subtracts 4
print(x)
x*=3 #multiplies by 3
print(x)

#1. And checks if both are true. bool(not(False) and True)
#2. Or checks if any are true. bool(False and not(True) and True)
#3. Not negates the value. bool(not(False))

#1. / divides, // divides and rounds down.
#2. % takes the remainer, // leaves out the remainder.
#3. Use %, 5%3 = 2.
#4. Assignment operators change the value of a variable.

mystring = "hello"
print(mystring) #hello
print (mystring[0]) #h
print (mystring[1]) #e
print (mystring[2]) #l
print (mystring[3]) #l
print (mystring[4]) #o
print (mystring[-1]) #o
print (mystring[1:3]) #el
print (mystring[0:5:2]) #hlo, goes 0 to 5 by 2s
print (len(mystring)) #5
print (mystring + "goodbye") #hellogoodbye
print (mystring * 7) #hellohellohellohellohellohellohello

#1. Slicing is taking a string in pieces and using the print to pick pieces out, used in 11 and 12.
#2. 
name = "Oski"
print("Hello, my name is", name) #Hello, my name is Oski
#3. 
print(f"Hello, my name is {name}") #Hello, my name is Oski
#4. f-strings allow for embedding.

#1 cd
# changes directories from folder to folder
#cd desktop

#2 ls
# lists the entries in a folder
# ls 

#3 ls -a
# lists all information about the contents of a folder
# ls -a

#4 mkdir
# creates a directory in a folder
#mkdir subfolder

#cat
# reads out the contents of a file
# cat myfile.txt

#pwd 
# prints where the current lines are being sent from
#pwd

#cd ..
# goes back one directory
# cd..

# cd . 
# changes to the current directory
# cd.

# cd ~
# returns to the home directory
# cd ~

#cp
# copies a file
#cp myfile.txt backupfolder

#mv 
# moves a folder
#mv myfile.txt backupfolder

#rm
# removes a file
#rm allmypasswords.txt

#clear
#clears the terminal
#clear

#grep
#finds entries with that name
#grep "chipotle password"

#1. rmdir removes empty directories, shutdown shuts down the system, ifconfig displays network information
#They are all performed by just typing them out.
#2. ls just makes the list, ls -a displays it with file/folder information
#3. They start with a . and don't display in default listings
#4. for ls, 3 other flags are -d for directories, - for regular files, -l for more information, add them to the end of ls after a space.
