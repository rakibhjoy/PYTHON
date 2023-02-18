import os
import platform

global listStd #Making ListStd As Super Global Variable1
listStd = ["INTRODUCTION TO PROGRAMMING", "PHYSICS 1", "ALGORITHMS", "CHEMISTRY"] #List Of course
listStd2 = ["INTRODUCTION TO PROGRAMMING"]#Individual course
listStd3 =["INTRODUCTION TO PROGRAMMING", "PHYSICS 1", "ALGORITHMS", "CHEMISTRY"]#Prerequisite Course

def manageCourse(): #Function For The Course Management System

	x = "#" * 30
	y = "=" * 28
	#Printing Welcome Message And options For This Program
	print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Course Management System	========|
 |======================================================|
  ------------------------------------------------------

Enter 1 : To View Course's List 
Enter 2 : To Add New Course 
Enter 3 : To Search Course 
Enter 4 : To Remove Course
Enter 5 : To Individual course display functionality 
Enter 6 : To Prerequisite Course 
Enter 7 : To Store functionality
Enter 8 : To Prerequisite Course 

		
		""")

	try: #Using Exceptions For Validation
		userInput = int(input("Please Select An Above Option: ")) #Will Take Input From User
	except ValueError:
		exit("\nHy! That's Not A Number") #Error Message
	else:
		print("\n") #Print New Line

	#Checking Using Option	
	if(userInput == 1): #This Option Will Print List Of Students
		print("List Courses\n")
		for Courses in listStd:
			print("=> {}".format(Courses))

	elif(userInput == 2): #This Option Will Add New Student In The List
		newStd = input("Enter New Course: ")
		if(newStd in listStd): #This Condition Checking The New Student Is Already In List Ur Not
			print("\nThis Student {} Already In The Database".format(newStd))  #Error Message
		else:	
			listStd.append(newStd)
			print("\n=> New Courses {} Successfully Add \n".format(newStd))
			for Courses in listStd:
				print("=> {}".format(Courses))

	elif(userInput == 3): #This Option Will Search Student From The List
		srcStd = input("Enter Course Name To Search: ")
		if(srcStd in listStd): #This Condition Searching The Student
			print("\n=> Record Found Of Courses {}".format(srcStd))
		else:
			print("\n=> No Record Found Of Courses {}".format(srcStd)) #Error Message

	elif(userInput == 4): #This Option Will Remove Student From The List
		rmStd = input("Enter Course Name To Remove: ")
		if(rmStd in listStd): #This Condition Removing The Student From The List 
			listStd.remove(rmStd)
			print("\n=> Course {} Successfully Deleted \n".format(rmStd))
			for Courses in listStd:
				print("=> {}".format(Courses))
		else:
			print("\n=> No Record Found of This Course {}".format(rmStd)) #Error Message
	 
	elif(userInput < 1 or userInput > 4): #Validating User Option
		print("Please Enter Valid Option")	#Error Message




	if (userInput == 6):  # This Option Will Print List Of Students
			print("List Courses\n")
			for Courses in listStd3:
				print("=> {}".format(Courses))






manageCourse()

def runAgain(): #Making Runable Problem1353
	runAgn = input("\nwant To Run Again Y/n: ")
	if(runAgn.lower() == 'y'):
		if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
			print(os.system('cls')) 
		else:
			print(os.system('clear'))
		manageCourse()
		runAgain()
	else:
		quit(bye) #Print GoodBye Message And Exit The Program

runAgain()		
