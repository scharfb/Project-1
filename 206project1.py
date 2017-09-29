import os
import filecmp
import csv
import datetime

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	with open (file) as f:
		names = []
		for row in f:
			names.append(row)
	keys = names[0]
	names = names[1:]
	people = []
	for string in names:
		dictionary = {}
		key_list = keys.strip().split(",")
		string_list = string.strip().split(",")
		for i in range(len(key_list)):
			dictionary[key_list[i]] = string_list[i]
		people.append(dictionary)
	print(people[0:3])
	return people
        
# keys - "
#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	data_sorted = sorted(data, key = lambda x: x[col])
	top_person = data_sorted[0]
	z = top_person["First"] + " " + top_person["Last"]
	return z
    

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	
	class_sizes = {"Freshman":0, "Sophomore":0, "Junior":0, "Senior":0}
	for student in data: 
		grade = student["Class"]
		class_sizes[grade] = class_sizes[grade] + 1
		class_list = class_sizes.items()
		data_sorted = sorted(class_list, key = lambda x: -1*x[1])
	return data_sorted

# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	dates = {
	    "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0,
	    "11":0, "12":0, "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0,
	    "21":0, "22":0, "23":0, "24":0, "25":0, "26":0, "27":0, "28":0, "29":0,
	    "30":0, "31":0
	}
	for student in a:
		dob = student["DOB"]
		day = dob.split("/")[1]
		dates[day] = dates[day] + 1
	dates_list = dates.items()
	days_sorted = sorted(dates_list, key = lambda x: (-1*x[1], -1*int(x[0])))
	return int(days_sorted[0][0])

# Find the average age (rounded) of the Students
def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest 
# integer.  You will need to work with the DOB to find their current age.

	dob_list = [person["DOB"] for person in a]
	age_list = []
	for dob in dob_list:
		nums = dob.split("/")
		year = int(nums[2]) 
		month = int(nums[0]) 
		day =  int(nums[1])
		dob_obj = datetime.date(year, month, day)
		today_obj = datetime.date.today()
		diff = today_obj - dob_obj
		age = diff.days/365.0
		age_list.append(age)
	average = sum(age_list)/len(age_list)
	return int(average + .5)

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	data_sorted = sorted(a, key = lambda x: x[col])
	with open(fileName, "w") as f:
		for student in data_sorted:
			first = student["First"]
			last = student["Last"]
			email = student["Email"]
			line = first + "," + last + "," + email + "\n"
			f.write(line)

################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

