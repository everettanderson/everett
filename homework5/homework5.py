#1. Git is the user end with what's on your computer/saved on your hub,
#GitHub is the online collection of the many files owned by other people.

#2. The terminal is a location to interact with an app, the command line is
#where you interact with the operating system.

#3. A local repository is on the home computer, but the remote one is
#stored somewhere else.

#4. Version control is managing the version of an installation/anything
#used by a group to keep organized.

#5. The staging area is where git organizes files from the local end
#to upload to gitbash.

#6. git add puts items in the staging area

#7. git commit saves the items in the staging area

#8. git push moves the items to gitbash

#9. git status shows the status of files around git(saved, ready to push, etc)

#10. git pull downloads items off of gitbash somewhere.

#11. pwd prints the working directory (where are you)

#12. ls shows what's inside the working directory

#13. cd moves betweens directories

#14. nano opens the text editor

#15. touch opens a new py file

#16. mv renames/moves files

#17. rm removes files.

#18. cat prints a file out

#3.2

#pwd

#ls -a

#cd . then cd brianna_repo then git pull 

#mv homework.py ../judy_decal/homework

#cd ../judy_decal/homework

#cat homework.py

#git add, git commit, git push

#it seems like the directory is not matched up that we are trying to
#push to. Judy should pull first before pushing back to ensure the new
#version is uniform.

#~/Recent

def checkdatatype(input):
	return type(input)
#print(checkdatatype(True))

def evenOrOdd(num):
	if num % 2 == 0:
		return "Even"
	else: return "Odd"
#print(evenOrOdd(4))

def sumofnumbers(nums):
	x = 0
	for num in nums:
		x = x + num
	return x
#print(sumofnumbers([1,2,3,4,5]))

def duplicatelist(list):
	x = []
	for item in list:
		x.append(item)
		x.append(item)
	return x

#missing a colon.
def square(num):
	return num * num

print(duplicatelist(["a", "b", "c"]))
