# Variable are containers that store data values. 
number = 2024
# print(number)
name = 'Yusuf'

today = "it's a sunny day"
today2 = 'it\'s a sunny day'
# print("yusuf")
# print(today2)

# Rules for naming Python Variables

# Methods of naming:
# 1. Camel Case - using small and big case
birthDate = "10th April 2024"
pepperStew = "Fish"

# 2. Snake case - using underscore to separate two words, while all in lower case

birth_date = ""
pepper_stew = ""

# 3. pascalcase - Big case are used for the first letters

Firstname = "Yusuf"

# 4. lowercase - small case are used to derive 
lastname = "Yazir"
#A variable must start with a letter or an underscore character, not with numbers nor special characters orpython keywords.

_day = 2
# print(_day)

# Declare five variables and print them all  

food = "Punded Yam"
soup = "ewedu"
meat = "beef"
plate = 3
bottleNum = 5

# print(meat, soup, meat, plate, bottleNum)

## Concatenatiom, Input Function
# concatenation is the joinig or merging strings together

name = "Jibola"
Location = "Lagos"

# print(name, "lives in", Location)
# print(name + " lives in " + Location)


food = "Pounded Yam"
soup = "ewedu"
meat = "beef"
plate = 3
bottle = 5

# print("Sola ordered " + plate + " " + food + " with " + soup + " and " + meat + ". He also drank " + bottle + "bottles of coke")

#Casting is done to convert from one data type to another

# print("Sola ordered " + str(plate) + " " + food + " with " + soup + " and " + meat + ". He also drank " + str(bottle) + "bottles of coke")

# INPUT FUNCTION - Gives an end user the permission to interact with a program i.e to receive data value. This data is collected as String

# food = input("What is your favorite meal? ")
# print(food)

# Quick Task
## Pass a greeting message to a username supplied by an end userdd
# name = input("What is your name? ")
# print("Hello " + name + ", you are welcome to Python Class")

## Collect two numbers from end user, add them
# print("Supply two numbers")
# num1 = int(input('>>>> '))
# num2 = int(input('>>>> '))
# total = num1 + num2
# print(total)

## Quick Task: 
# --- Task: Create a program that generates Band name using city and pet name

# 

## Assignment 

### Write a simple python program rhat will request for the name of the user and the course. Take in two Values (first value as exam score and second value as test score). It will then add the two values and display the result in a simple sentence as below:

## The output should look like "Welcome Lingz, your total score in English Language is 79."

# print('Welcome to Result Portal')
# name = input('Enter your name ')
# course = input('Enter your course ')
# testScore = int(input('Enter your test score '))
# examScore = int(input('Enter your Exam score '))
# totalScore = str(testScore + examScore)
# print('Welcome ' + name + ', your total score in ' + course + ' is ' + totalScore + '.')

## 4/4/24 Types of variables, data types.

# Other means to create variables. On a straight line

name, course, level, year = "Yazir", "Python", 4, ""
# print(name, course)

## Assigning one value to multiple variables

state = place = location = "Lagos"
# print(state)
# print(place)
# print(location)

x = y = z = 10
# print(state + " is a place. Where number " + str(y) + " thrives...")
# ## f-string - to replace concatenation(+)
# print(f"{state} is a place. Where number {str(y)} thrives...")

## unpacking a collection
## Unpacking means extraction of values by using arrays

# food_items = ('rice','beans','vegetables')
# print(food_items)
# x,y,z = food_items
# print(z)

## Types of VARIABLES - Local and Global.
# Local varaibles are defind inside a function or class and are only available insode that enviroment they are declared
def variableLocal():
    numb1 = 30
    numb2 = 90
    # print(numb1 + numb2)

# variableLocal()

# numb1 = 40
# print(numb1)

## Data Types
# types of Datatypes
# 1. Text type: String (str) - name = 'Yaz' print(type(name))
# 2. Numeric type:
#  Intergers (int)
#  float - Decimal number,
#  Complex - imaginary number using j like vectors
# 3. Boolean: bool (True, False)
# 4. Array types
    # sequence type: List, Turple and range
    # names = ['kolak','pepesna','sean-k'] print(type(names)) = list
    # names1 = ('kolak','pepesna','sean-k') print(type(names1))
# 5. Mapping type Mapping keys and values - They are dictionary(Object)
    # firstDict = {'name':'Danjuma', 'age': 11} print(firstDict)

#Casting - it is the conversion of datatypes

# key1, key2 = input('Enter a number: ').split(',')
# print(int(key1) + int(key2))

# 8/04/2024
# ARRAYS
# student_name = ["Ade","Segun","Kunle","Bayo"]
# student_name[3] = "Ola"
# print(student_name)
# print(f"My name is {student_name[2]}")

# students = ["lola","bayo","seun","sola"]
# print(students[:3]) // slicing the array

# student_tuple = tuple(student_name) # casting
# print(student_tuple)

# for i in range(1,20):
#     print(i)

# Tuples: Tuples can not be modified.
#set
#frozensets
# dictionary

#task
# You created an array which contained 4names of your most trusted friends and stored in tuple, while forgot to add Buchi your bestman. Find a way to add ypour Buchi into the tuple array
# Your Final output should be tuple

# Bestmen = ("Akin","Chike","Ibrahim","Musa")
# print(Bestmen)
# Bestmen_update = list(Bestmen)
# Bestmen_update.append("Buchi")
# # print(Bestmen_update)
# Bestmen_update_final = tuple(Bestmen_update)
# print(Bestmen_update_final)
# Bestmen_list = list(Bestmen_update_final)
# Bestmen_list[4] = "Michael"
# Bestmen_tuple = tuple(Bestmen_list)
# print(Bestmen_tuple)

numre_ = {1,3,8,9,0, "poli"} # set
num_re = ({1,2,3,4,5,"Tade"}) # Frozen set
# print(num_re)

## Use set operations
val1 = [1,8,4,7,2,0,12]
val2 = [1,3,8,5,2,0,18]

val1 = set(val1) ## cast list to set
val2 = set(val2)

# intersect = val1.intersection(val2)
# print(intersect)

## ARRAY CONVERSION
# student_namez = ["Ade","Lola","Wale","Kunle"]
# student_namez.append("Ileri")
# print(student_namez)
# student_namez[0] = "Alade"
# print(student_namez)
# print(student_namez[:3])

## Range
# for i in range(1,21):
#     print(i)

## Dictionary 
student_inf = {"name":"Alani","Dept":"Computer Science","Age":29}
# print(student_inf["Dept"])

## Operations +, -, /, **(exponential) // (floor), % modulus, 
    ## Assignment operators: =, +=, -=

# a,b = 2, 3
# print(a+b)
# print(a*b)
# print(a/b)
# print(a**b)
# print(a%b)
# print(a//b)

# y = 0
# p = 0
# z = 10
# y += z
# print(y)
# y *= p
# print(y)
# y /= z
# print(y)


## Comparison operators - Based on if true or false. ==,!=,>,<,<=>=

# result = 10 == 10
# result = 10
# r = result == 10
# print(r)

# res = x >= y 
# res = x <= y
# print(res)

# x = 5
# y = 6
# resultz = x != y
# print(resultz)

# res = x > y
# res = x < y
# print(res)

# LOGICAL OPERATOR: and, or, not - used for validation. They return Boolean
# and operator - the two or more conditions must be valid
## or operator - either of the two conditions are valid
## not - negate

sval = 200
fval = 30

# print(sval != fval and sval > 50 and fval < 40)
# print(fval == 201 or fval == 10)
# print(fval >= 50 or sval >= 30) 
# print(fval == sval or sval > fval and sval <= fval) 
# print(fval != 0 and sval > 100) or (fval > 10 and fval == True)
# print(sval == True and sval > 100) or (fval > 10 or fval == False)
# print(sval == False and sval >= 100) or (fval > 10 or fval == False)
# print(sval == True or sval >= 100) or (fval > 10 or fval == True)
# print(sval == True or sval >= 100) and (fval > 10 or fval == True)

# print(not(fval <= sval))

# Identity Operator: is, is not
# print(fval is not sval)

# Membership Operators: in, not in - Works with aRRAYs
# val = ["Sola","Moodal","Woosa","Isa"]
# print("Isa" in val)
# val_dict = {"name": "Yaz", "age": 10}
# print("name" in val_dict)

## Assignment: Write a program for blogger, ask a user to supply blog content ad check if the content contains a particular word. If present, print a message that such word is present and else

# blog_content = ""
# print("Welcome to the Olofofo Blog")
# blog_content += input("Please enter your blog content >>>> ")
# # add them
# print(blog_content)
# print("olofofo" in blog_content)

## 15/ 04/ 24
## Bitwise operator: This operator works with binary, values must be firstly converted to bitwise &, | - or ,
### ^ - exclusive or, ~ negation, <<, >>
fval = 342
sval = 111
lval = 53
result1 = bin(fval)
result2 = bin(sval)

finalresult = bin(fval & sval) # set each bit to 1 if both bits are the same e.g false + false = false, true + true = true, true + false = false
finalresultor = bin(fval | sval) # set each bit to 1 if one of the two bits is 1/ Either is true, both condition invalid =false
finalresultors =bin(fval ^ sval) # set each bit to 1 if only one of the two bits is 1. T+T = F
finalresultorz = bin(~ fval) ## inverts all the bits. T to F, and F to T
# print(bin(sval << 2)) # Zero fill to the end
# print(bin(sval >> 3)) # delete values from the end
# print('The final set is: ' + finalresult)
# print('Final set for OR is: ' + finalresultor)
# print('Final set of lol is: ' + finalresultors)
# print('The final set is: ' + finalresultorz)


## Python String Methods
name = 'sodiq is a good boy'
# print(name.title())
# print(name.upper())
# print(name.capitalize())
# print(name.lower())

## indexing strings
# print(name[2])
# print(name[-3])
## slicer for range, will not return last range
# print(name[:3]) # 3 will not be printed
# print(name[-4:-1])


name2 = "shady   "
# print(len(name2))
# print(len(name2.strip()))
  
comment = """The boy is travelling to his hometown and he needs to get some thinsg done as 
            soon as he can but there are few issues along the day """

# print(comment[1:13])
# print(comment[-32:-10])
# print(comment.startswith("The")) ## returns booleans
# print(comment.endswith("Lol")) ## returns booleans

## IF Statement:
# print("Welcome to SQI")
# askAge = int(input("What's your age? "))
# if askAge < 7:
#     print("You are not allowed here")
# else:
#     print("Welcome! Happy Coding")

## Assignment: 
#write a program that will tell a user to write an article. The program will have the ffg functionalities: 
# Ask user if he/she wants to replace a word from the article
# Ask the user to supply the word to be replcaed and the word to be replaced with
# Append the changes to the article

# print("~Welcome to Bloggerz~")
# blog = input("Type your Article here: ")
# print(f" Your Article: {blog}")
# prompt = input("Press '1' to replace any word, any other key to cancel: ")
# if prompt == '1':
#     replaced = input("Enter a word you want to replace: ")
#     if replaced in blog: 
#         replacer = input("Enter the replaced word here: ")
#         edited = blog.replace(replaced, replacer)
#         print(f"Changes succesfully made: {edited}")
#     else: 
#         print(f"Sorry we can't find {replaced}")
# else:
#     print('Article Received')

## if-else-else syntax

## elif statement is another if test, which is used to evaluate more than 2 arguments, and it is ussually
### declared after the initial if, the elif is checked when the initial if failed the test

### the elif allows us to test for more than two possible situations and can be declared many times.

# req = int(input("Please neter your shoe size"))

# if req >= 30 and req <= 60:
#     print("We have them available")
######
#######
######

# print("Register fot Free Training in IT")
# print("Do you have access to a Laptop or Tablet")
# user = int(input("1. Laptop 2. Tablet 3.None.."))

# if user == 1:
#     print("Bravo.. You are ready for training.")
# elif user ==2:
#     print("okay. Tablet devices are limited, but you have an edge")
#     print("""
#           Android or iOS
#           """)
#     choice = input("For Aandroid Press1, For iOS, press 2 ")
#     if choice == "1":
#         print("is the version > 11 ")
#         choice_android = input("Y or N").upper()
#         if choice_android == "Y":
#             print("Congratulations")
#         elif choice_android == "N":
#             print("Sorry you are disqualified ")
#         else:
#             print("Invalid Input")
#     elif choice == "2":
#         print("Oh no! Apple has not made mobile device suitable for coding")
#     else:
#         print("Invalid Input")
# else:
#     print("sorry...")

## Calculator that adds, subtract,divide and multiply on supply of two vlaues

# print("Calualtor.py")
# total = 0
# fnum = int(input("Enter your first number: "))
# snum = int(input("Enter your second number: "))
# sign = input("Enter 1. Add 2. Subtract 3. Multiply 4. Divide: ")

# if sign == '1':
#     total = fnum + snum
#     print(f"{fnum} + {snum} = {total}")
# elif sign == '2':
#     total = fnum - snum
#     print(f"{fnum} - {snum} = {total}")
# elif sign == '3':
#     total = fnum * snum
#     print(f"{fnum} * {snum} = {total}")
# elif sign == '4':
#     total = fnum / snum
#     print(f"{fnum} / {snum} = {total}")
# else:
#     print("You entered an operation that does not exist")

## Computer guessing game, computer picks a number from 5 to 10 and tru to guess, print pass if
### guesed right. 

# import random

# print("==== > _ < ====")
# user_guess = int(input("Enter any number from 5-10 : "))
# comp_guess = random.randint(5,10)
# if user_guess == comp_guess:
#     print("Pass")
# else:
#     print("Retry again later")
# print(f"The Bot guess is: {comp_guess}")


# 18th of April 2024

## Task - Write a program that calculates the body mass index(BMI) of a user using weight and height

## Create a program using maths and f-strings that tell us how many days, weeks, months we have
# left if we live until 99 years old

## Write a program that works out whether a given number is odd or even number

## Class Task
## Write a program for a reverse park to handle reservations and fees mgt
## Fees Category are: Adult = 2500 Teennage(9 - 17) = 1200 Children < 7 = 0

## Note: for a group above 8, there will be a discount of 20% on total fee. 
# Coming with a media device attract extra charges of 1000.

## Breakdown 
# 1. How many people/individual
# 2. Category - Number of adults, teens, childreen
# 3.With media device?
# Calculate Cost/Price & discount


# Db_dic = {"Adult_fee":2500, "Teenage_fee":1200, "Children_fee":0, "discount":0.2, "media_device":1000}

# print("***** Amusement Park 2024 *******")
# for k, v in Db_dic.items():
#     print(k, v)

# form_adult = int(input("How many Adults are you bringing in? "))
# form_teen = int(input("How many Teens are you bringing in? "))
# form_child = int(input("How many Children are you bringing in? "))
# form_num_sum = form_teen + form_adult + form_child
# if form_num_sum != 0:
#     fee_a = form_adult * Db_dic["Adult_fee"]
#     fee_t = form_teen * Db_dic["Teenage_fee"]
#     fee_c = form_child * Db_dic["Children_fee"]
#     initial_fee = fee_c + fee_a + fee_t
#     print(f"Initial Charge is {initial_fee} follow the next prompt")
#     devices_ques = input("Are you bringing in any media devices? Y or N ").upper()
#     if devices_ques == 'Y':
#         initial_fee_two = initial_fee + 1000
#         print(f"======= Previous Charge is *{initial_fee}* =======")
#         print(f"== Device charge is 1,000: Current Charge now {initial_fee_two} ==")
#         if form_num_sum > 8:
#             print(form_num_sum)
#             final_fee = initial_fee_two * 0.2
#             print(f"Congratulations, You will get a discount of '20%' from {initial_fee_two}")
#             print(f"Generate an invoice and pay {initial_fee - final_fee} to the cashier")
#             Agree = input(f"Enter any key to agree to pay ${initial_fee - final_fee} ")
#             print("Thanks for choosing Us")

#         else: 
#             final_fee = initial_fee_two
#             print(f"Generate an invoice and pay {final_fee} to the cashier")
#             Agree = input(f"Enter any key to agree to pay ${final_fee} ")
#             print("Thanks for choosing Us")
#     elif devices_ques == 'N':
#         initial_fee_two = initial_fee
#         if form_num_sum > 8:
#             print(form_num_sum)
#             final_fee = initial_fee_two * 0.2
#             print("Congratulations, You will get a discount of 20%")
#             print(f"Generate an invoice and pay {initial_fee_two - final_fee} to the cashier")
#             Agree = input(f"Enter any key to agree to pay ${initial_fee - final_fee} ")
#             print("Thanks for choosing Us")
#         else: 
#             final_fee = initial_fee_two
#             print(f"Generate an invoice and pay {final_fee} to the cashier")
#             Agree = input(f"Enter any key to agree to pay ${final_fee} ")
#             print("Thanks for choosing Us")
#     else:
#         print("Enter a Valid Value")
# else:
#     print("No entries, Try again")


### ODD OR EVEN:
# print("Odd and Even Number Calculator: ")
# num_check = int(input("Enter a number to check >>> "))
# if num_check % 2 == 0:
#     print(f"{num_check} is an even number!")
# else:
#     print(f"{num_check} is an Odd number")


# ## BMI meter:
# print("Welcome to BMI Check Station")
# weightz = float(input("Enter your weight in Kg: "))
# heightz = float(input("Enter your height in m: "))
# height_final = heightz * heightz
# BMI_value = weightz / height_final
# print(BMI_value)


### How many days until 99years! 

# from datetime import date

# current_date = date(2024,7,2)
# future_date = date(2123,7,2)

# days = future_date - current_date
# print(days)

## Data Structure - List and Dictionary

## List - is a type of an array and data structure.. Data stored in a list are ordered,
## mutable and allows duplicate values. A list is created with a square bracker [] or list() constructor

## List can take different types of data type at once

programing = ['Pyhton','Java','C++']
programing2 = list()

## List attributes and methods
# Adding values to a list - use append, extend, insert and for loop.
# Append -- can only  take one argument.
# programing.append('Kotlin')

## INSERT - Can only add value but takes two argument at a time, position and data value. 
## It adds data to specific psotion.

# progrmax = ['Python', 'javascript', 'java', 'c++']
# # progrmax.insert(0, 'CSS')
# progrmax[1] = "CSS"

## Extend - It adds a list to another list
# lst1 = ['Funbi','Gbenga','Bolu','Bolu']
# lst3 = ['Rose','Timi','Tosin']
# lst1.extend(lst3)
# lst3.append('Bukky')
# print(lst1)
# lst1.sort(reverse=True)
# print(lst1)

## Using for loop instead of extend attribute to add values into a list
# programlangs = ["Python","Javascript","Java","C++","Kotlin"]
# otherLangs = ["Flutter","Golang","Rust"]

# for l in otherLangs:
#     programlangs.append(l)
# print(programlangs)

# color = ["white","blue","black"]
# color1 = ["dark","reddy"]

# for c in color:
#     color1.append(c)
# print(color1)

## 3. Deleting from a List:

# programlangs = ["Python","Javascript","Java","C++","Kotlin"]
# otherLangs = ["Flutter","Golang","Rust"]
# pop() auto deletes the last value from a list
# programlangs.pop()
# using pop() to delete with position
# programlangs.pop(2)

 #### You can use remove() instead of pop
# programlangs = ["Python","Javascript","Java","C++","Kotlin"]
# programlangs.remove('Java')
# print(programlangs)
#### clear() returns an empty list
# programlangs.clear()

### del() will delete the list variables completely and the loist won't exist anymore
# del programlangs

# my_list = ["shade","Biola","Bukky","Charles"]
# if "Biolaz" in my_list:
#     print("Available")
# else:
#     print("Unavailable")

# mylist = ["ajao","kolade","bola","carner"]
# mylist.sort(key=str.lower)
# print(mylist)

# my_list3 = [12,9,1,10,23,44]
# my_list3.sort(reverse=True)
# print(my_list3)

# my_pizza = ["Pepperoni", "Suya", "Chinese"]
# for i in my_pizza:
#     print(f"I like {i} Pizza")
# print(f""" I so much like {my_pizza[1]} Pizza, it is very nutritious. Sweet to the Tongue!
#       Yummy to the belly!
#           I can't do without Pizzas
#         I really love pizza!
#           """)


## studysession - check website
# #1
# Animal_type = ["Cow","Goat","Ram"]
# for a in Animal_type:
#     print(f"A {a} will make a good Meat")
# print("Any of these Animals will make a good Asun")

# #2
# import random
# num_range = []
# for i in range(1,21):
#     num_range.append(i)
# # print(num_range)
# print(random.choice(num_range))

# #3
# million_loop = []
# for l in range(1,1000001):
#     million_loop.append(l)
#     print(l)

# # 4
# million_loop2 = []
# for l in range(1,1000001):
#     million_loop2.append(l)
#     # print(l)
# print(max(million_loop2))
# print(min(million_loop2))
# print(sum(million_loop2))

# # 5
# multi3 = []
# for p in range(3,31):
#     if p % 3 == 0:
#         multi3.append(p)
# print(multi3)

## Checkout difference bwtween .deepcopy() .shallowcopy() and applicable scenario
## Copy attribute: To reuse, protect original document and prevent alteration
# ProgramLangu = ['Python','Javascript','Java','C++','Kotlin','C']
# progs = ProgramLangu.copy()
# new_progs = ['Ruby','PHP','React','Vue']
# progs.extend(new_progs)
# print(progs)


### Slicing and Indexing
## len function - it counts the number of values in an array.. It returns the lenght of the array
## as an output.
# print(len(progs))

# ## Indexing - takes a positions and returns the value of the index provided
# print(progs[0])
# print(progs[-3])
# print(progs[-1])
# print(progs[2])

# ## Slicing - To cut a part of an array
# print(progs[1:5])
# print(progs[:])
# print(progs[-1:-4])

## Slicing and Steps
# print(progs[1:6:2])
# print(progs[::2])
# print(progs[-1:-9:2])

# ## Quick drill
# lst_no = [1,2,3,4,5,6,7,8,10]
# store = []

# for z in lst_no:
#     b = z*z
#     print(f"The square of {z} is {b}")
#     store.append(b)
# print(store)

# ### List comprehension:
# lst_nol = [1,2,3,4,5,6,7,8,10]
# squares = [num ** 2 for num in lst_nol]
# print(squares)

# squarez = [num for num in range(1,10001)]
# print(squarez)

# squares = []
# for num in range(1,11):
#     squares.append(num ** 2)
# print(squares)

### NESTED List: It is a list that contains another list
# progland = ['Python','JS','C++','Kotlin']
# p_lang = ['Raspberry','Node']
# progland.insert(2, p_lang)
# print(progland)

# progland1 = ['Py','Node',[1,'IOT',3],'JS','Rb']
# print(progland1[2][1])

# redo_prog = ['Python',['a','b','c'],'Javscript','Java',[1,'IOT',3],'C++','Kotlin','C',False]
# print(f"One of the alphabets in the array is: {redo_prog[1][1]}")

### Tuples = is a collection that is ordered but immutable and allows duplicate values 
## It uses braces ("") or tuple constructor
# name = ("Banks","Jadon","Camoranesi")
# name = "Banks","Jadon","Camoranesi"
# print(type(name))
# print(name)

# ## Working with a tuple - index
# name = ["Shade","Energy","Magnet","Energy","Charles"]
# name2 = tuple((12, 14))
# for i in name2:
#     name.append(i)
# print(name)

#### Task 1
langz = tuple(('IOT','R'))
prog_lanz = ['Python','JS','Java','C++','Kotlin']

# conv_lis = list(langz)
# prog_lanz.extend(langz)
# print(prog_lanz)

## Task 2
langp = tuple(('IOT','R'))
prog_up = ('Python','js','Node','C++','kotlin')

# prog_up += langp
# print(prog_up)

## Task 3
# for q in langz:
#     prog_lanz.append(q)
# print(prog_lanz)

# ## Task 4
# langp2 = list(langp)
# for r in prog_up:
#     langp2.append(r)
# print(langp2)

# ### Packing & Unpacking - Value extraction

# items = ("Yam","Yemi","Lagos",29)
# (food, name, Location, age) = items

# print(name, age)
# print(items.count(name))
# print(Location)
# print(food,*name,Location)

## Assignment
# Write a program that collects the name, email and gender, occupation of a user. Store data in a list
# and display each values in the list...

# name = input("Enter your name: ")
# email = input("Enter your Email Address: ")
# gender = input("Enter your Gender: ")
# occupation = input("Enter your Occupation: ")

# user_details = [name, email, gender, occupation]
# print(user_details)


## 29th of April, 24
#### Set - it is a collection which is unordered and unindexed, changeable and does not allow duplicate values
my_set = {"Shade", "Energy", "Energy", "Magnet", "Energy", "Charse", "Charse"}
## Set can not be indexed due to unorderliness.
# print(len(my_set)) # no duplicate
# for i in my_set:
    # print(i + ", " + "is in set")
# print("Sarah" in my_set) ## bool

# Lets add values to our set
## my_set.add("Kassy") # add() only takes one argument..
# print(my_set)

## Looping
moreLangs = ["PHP", "Node", "Flkutter", "Dart"]

# for a in moreLangs:
#     my_set.add(a)
# print(my_set)

# for a in my_set:
#     moreLangs.append(a)
# print(moreLangs)


## Using Upadate

# moreLangs = ("PHP","Node","React","Flutter","Vue","Vue")
# moreLangs = ["PHP","Node","React","Flutter","Vue","Vue"]
# moreLangs = {"PHP","Node","React","Flutter","Vue","Vue"}

# prog_lanz.update(moreLangs)

# Delete

# ProgLang = {'c','vue','python','react','c++','javascript','kotlin','Dart','flutter','java','PHP','Node'}

# ProgLang.remove('Node')
# print(ProgLang)
# ProgLang.pop() ## will delete argument randomly

## discard()
# ProgLang.discard('C')
# print(ProgLang)

# ## clear()
# ProgLang.clear()
# print(ProgLang)

# ## delete()
# del ProgLang
# print(ProgLang)

## union - works like update
# set1 = {1,2,3,48,0}
# set2 = {98,0,1,1,3}
# set_1= {2,3,4,5,10}
# set3 = set1.union(set2)

# set3 = set1.intersection(set2)
# print(set3)

# set1.intersection_update(set2) # wanna run without setting variable name, same as intercept

# print(set1)

# set1 = {1,2,3,4,5,6,7,8,9}
# set2 = {11,123,14,5}

# set3 = set1.symmetric_difference(set2) # extract the uncommon
# print(set3)
# set1.symmetric_difference_update(set2)
# print(set1)

# set3 = set1.difference(set2) ## extract uniqyue values in set1
# print(set3)

# set2.difference_update(set1)
# print(set2)

# set4 = set1.isdisjoint(set2) # wi;; return True if there is no intersection
# print(set4)

# set1 = {1,2,3,4,5,6,7,8,9,10}
# set_1 = {2,3,4,5,10}
# print(set_1.issubset(set1))
# print(set1.issuperset(set_1))
### Remind oga of nested array next week

### Create an array that contain 10 terms that you have learned in py

# arry_term = ["append","del","list","loop","function","set","print","cast","union","concatenation","operation"]
# print(arry_term)

## 30th Of April 2024
#### Dictionary - it is a collection which is ordered, changeable but does not allow duplicate and unindexed. 
### Data is stored in key/value pair or dict(key=value)
# # data = {"name":"Yazir","Course":"Data Science","Age":12}
# # # print(data['name']) 
# # name = "Biggy"
# dict1 = {"name":name,"age":28,"gender":"male"}

# ##### Attributes
# dict1["name"] = "Bayo"

# # Give the output of the individual keys
# car = {"Producer":"Toyota","Model":"Venza 2021","Engine":"6 Engines","Color":"Black"}

# for i in car.keys():
#     print(car[i])

# ### Another way of creating a dict:
# stud_record = dict(name="Tory", course="Data Scienece")

# print(car["model"])
# print(car.get("model"))
# print(car.keys())
# print(car.values())

# # 2. How to Add to Array
# car["passengers"] = 10
# car["tyre"] = "Hyundai"
# print(car)

# # car.update({"year":2021,"country":"China","tyre":"Chuan"})
# # OR
# OPS_CARS = {"year":2021,"country":"China","tyre":"Chuan"}
# car.update(OPS_CARS)
# print(car)
# ## delete in a dict

# car.pop("model")
# car.popitem()
# print(car.clear)
# del car["model"]
# print(car)

# ## Looping over a dictionary

# ## print keys only
# for k in new_car:
#     print(k)

# ### Print values only
# for w in new_car.values():
#     print(w)

# ### Print keys and values
# for k,v in new_car.itens():
#     print(k, v)

# stduent_details = {
#     "Tony Adams":{"name":"Tony Adams","Age":22,"Occupation":"Developer"},
#     "Oye Banji":{"name":"Oye Banj","Age":12,"Occupation":"Comedian"},
#     "Kola Isolau":{"name":"Kola Isolau","Age":20,"Occupation":"Driver"}
# }

# for k, v in stduent_details.items():
#     print(k, v)

# # print Tony's occupation
# print(stduent_details["Tony"]["Occupation"])

# Another way to Nest??

# student_1 = {'name':"Tom Johnson","level":100,"location":"Turnis","depr":"Mathematics"}
# student_2 = {'name':"Jonas Cucurak","level":300,"location":"Ibadan","depr":"CSC"}

# stduent_details2 = {
#     "stud1": "student_1"

# }

# # You have been granted access to a database of student_scores in format of a dictionary: name and exam score

# student_scores = {
#     "Calistos":80,
#     "Ronky":56,
#     "Hassan":90,
#     "Kunle":67,
#     "Chukwudi":81,
#     "Collars":44,
#     "Flexos":51
# }

## Write a program that converts student scores to grades using the grading system; 70-100 = Distinction, 60 -69 = "Excellent"
## 45 - 59 = "Very Good", below 45 = "Fail"

# Output Calistos : Distinction, Ronky: Very good!

# grades_metrics = ["Distinction","Excellent","Very Good","Fail"]

# for studentz, mark in student_scores.items():
#     if mark >= 70:
#         print(studentz + ":" + grades_metrics[0])
#     elif mark > 59 and mark <= 69:
#         print(studentz + ":"+ grades_metrics[1])
#     elif mark == 45 and mark <=59:
#         print(studentz + ":"+ grades_metrics[2])
#     else:
#         print(studentz + ":" + "Failed")

## 2nd of May 2024
# Split() - By default uses space character to separate characters
# commenta = "I commented of Yemi tweet yesterday, because of I liked it. I am going to check it again today - thank you"

# commentasplit = commenta.split()
# commentasplit = commenta.split('.')
# commentasplit = commenta.split(',')
# print(commentasplit)

# nums = input("Enter set of numbers, separated by commas: ").split(",")
# print(nums)

# print(commenta.split("of"))

## Join() Function

# value = ["rice","bveans","dodo","fish"]
# print(" ".join(value))

# Capitalise()

# ywan = "i am exited"
# print(ywan.capitalize())
# print(ywan.title())

## Center() - to center or align text to the center. It takes two arguments, width and fillchar which is the character to be paded(optional)

# print(comment.center(1500))
text = "Hello World"

## Count
# print(comment.count("."))
# # print(comment.count("is"))
# # print(comment.count("week"))

# article = """   Hey, I am Yazir. You can call me Mr. Yaz, or Yaz for short. I like winning.... lol... lol... haha.hah.ahha
#                  I am excited to work on this project with you all, project .......     
#         """
# print(article.count("."))
# print(article.count("I"))
# print(article.strip())
# print(article.count(" "))

## Concatenation using Format()
# name = "Johnee"
# numq = 4
# name3 = "Ben"

# commentp = """I am {}. I have worked here for {} years. 
#                 My friend {} is also here"""
# print(commentp.format(name,numq,name2))

## check out resend.
### Send a message to first 20 users of AR-Loans, telling them they qualified for our raffle draw.
### "Hi {name}, as one of our first 20 clients, you qualified to participate in $10,000 raffle draw till the end of May"

# namz = ['Ade','John','Funmi','Sola','Alao','Akin','Funke','Tunji','Tunde','Wale','Ayo','Tobi']
# end_dat = 31
# emaip = """Hi {}, as one of our first 20 clients, you qualified to participate in $10,000 raffle draw till the end of May {} 
#          """
# for y in namz:
#     print(emaip.format(y,end_dat))

### subject = "data science"
# test_score = float(input("test score"))
# exam_score = float(input("exam score"))
# total = test_score + exam_score
# print(f"My {name} is good, my score is {total} in {subject}")

## Escape Character (\) - they special characters in python
# print('she\'s a good girl')
# print("she is the \b owner") # backspace
# print("she is the \t girl I said") ## tab
# print("she is the \r owner") ## return carriage
# print("she is the \n owner") ## next line

## Weekend Assignment:
## Write a program that will ask the user to supply two values using one variable, then perform all the set opeartion depending
## on the choice of the user - addition, substraction, division and multiplication.


# acc = input("Enter two numbers: ").split(",")
# mathz = input("Enter 1 to Add, 2 to subtract, 3 to multiply, 4 to divide: ")
# if mathz == '1':
#     final_rec = int(acc[0]) + int(acc[1])
#     print(f"{acc[0]} + {acc[1]} is equal to {final_rec}")
# elif mathz == '2':
#     final_rec = int(acc[0]) - int(acc[1])
#     print(f"{acc[0]} - {acc[1]} is equal to {final_rec}")
# elif mathz == '3':
#     final_rec = int(acc[0]) * int(acc[1])
#     print(f"{acc[0]} x {acc[1]} is equal to {final_rec}")
# elif mathz == '4':
#     final_rec = int(acc[0]) / int(acc[1])
#     print(f"{acc[0]} / {acc[1]} is equal to {final_rec}")
# else:
#     print("You entered a wrong value sir!")


## Write a program that will ask the user to supply two values using two variable, then perform all the set opeartion depending
## on the choice of the user - addition, substraction, division and multiplication

# acc1,acc2 = input("Enter two numbers: ").split(",")
# mathz = input("Enter 1 to Add, 2 to subtract, 3 to multiply, 4 to divide: ")
# if mathz == '1':
#     final_rec = int(acc1) + int(acc2)
#     print(f"{acc1} + {acc2} is equal to {final_rec}")
# elif mathz == '2':
#     final_rec = int(acc1) - int(acc2)
#     print(f"{acc1} - {acc2} is equal to {final_rec}")
# elif mathz == '3':
#     final_rec = int(acc1) * int(acc2)
#     print(f"{acc1} x {acc2} is equal to {final_rec}")
# elif mathz == '4':
#     final_rec = int(acc1) / int(acc2)
#     print(f"{acc1} / {acc2} is equal to {final_rec}")
# else:
#     print("You entered a wrong value sir!")


## Write a program that prompts the user to enter a sentence. Extract all the vowels(unique) from the sentence and store them in a set. Display the set of vowel
# vow = ['a','e','i','o','u']
# store_set = []
# sent = input("Enter your sentence to check: ").lower()
# for l in vow:
#     if l in sent:
#         store_set.append(l)

# print(set(store_set))


## LOOPS

## for loop
# For loop is for iteration of process. It is commonly used with a list.
## A for loop is a control flow statement used in programming to iterate over a sequence of elements or execute a block of code a certain
### number of times.

## A for loop statement consist of 3 parts - Initialization, condition and increment/decrement.

# for i in range(4):
#     print('Welcome to class...')


# for i in range(1,4):
#     print('Welcome to klass...')

# # for loop with a list
# n = [1,2,3,4,5]
# for v in n:
#     print(v + "is the value")

## Task
#1. Multiply numbers from 2 - 50 by 4. Expected output is (2 x 4 = 8)

# for p in range(2,51):
#     print(f"({p} x 4 = {p * 4})")

#2. Find the prime numbers between 1 and 100
# check = 0
# for prix in range(1,7):
#     prix == check
#     for m in range(prix):
#         print(type(prix))
#         m % proix
#             print("Prime")

        # if prix % m == 0:
        #     print(f"we found a prime: {pri}")

# w = 2 / 10
# print(w)

## Collect even numver betwwen 1 and 100

# for ev in range(1,101):
#      if ev % 2 == 0:
#           print(f"{ev} is an even number")

### WHILE LOOP
## while loop is a type of control flow statement that is used to repeatedly execute a block of code as long as a specific 
## code is true

## Note - For loop iterates over sequence certain number of times, while loop continues to iterate as long as a certain condition is true

# while True:
#     print('Welcome to Class')

# count = 5
# while count > 0:
#     print("Learning Loops...")
#     count = count - 1

# # Using while loop to count through a series of numbers 
# current_num = 1
# while current_num <= 5:
#     print(current_num)
#     current_num += 1

## Collect Customer Info:

# storeData = {}
# counter = 3
# while counter > 0:
#     user = input('What is your name? ')
#     number = int(input('Enter your lucky number: '))
#     storeData[user] = number
#     counter -= 1

# print(storeData)

# storeData = {}
# counter = True
# while counter:
#     user_response = input("Enter q to quit, e to continue")
#     if user_response == 'q':
#         counter = False
#     else:
#         user = input('What is your name? ')
#         number = int(input('Enter your lucky number: '))
#         storeData[user] = number 

# print(storeData)

# prompt = "Tell me something, and I will repeat back to yoy"
# prompt += "\n Enter 'quit' to exit. \n"

# message = ""

# while message != 'quit':
#     message = input(prompt)
#     print(message)

## Create a db storing list of usernames of an org, phone and email. Store in dic, then the dictionary stored in a list. 
# db_com = []
# dict_com = {}
# active = True
# while active == True:
#     username = input("\n Enter your username: ")
#     phone = int(input("\n Enter your phone number: "))
#     email = input("\n Enter your email: ")

#     dict_com['username'] = username
#     dict_com['phone'] = phone
#     dict_com['email'] = email
#     db_com.append(dict_com)
#     if len(db_com) == 3:
#         active = False
# # print(dict_com)
# print(f"\n {db_com}\n")

## 6th of May 2023
## Types of Loops:

### There can be nested for loop and nested while loop.

# counter_a = 0
# db_a = {}
# db_lst = []
# while counter_a < 3:
#     name_a = input("Enter your name: ")
#     course_a = input("Enter your course: ")
#     db_a[counter_a] = { "name": name_a, "course": course_a}
#     db_lst.append(db_a[counter_a])
#     counter_a += 1
    
# print(db_lst)

# height_lst = []

# ['3','4']


# sandwixxh_orders = ['Suya Sandwish','Pastrami Sandwish','Tuna Sandwish','Pastrami Sandwish','Shawarma Sandwish','Pastrami Sandwish']
# finished_sandwixh = []
# print("Dear customer, we just run out of your lovely Pastrami :(")

# while "Pastrami Sandwish" in sandwixxh_orders:
#     sandwixxh_orders.remove("Pastrami Sandwish")

# print(f" here is the reviewed order list: {sandwixxh_orders}")
# for sand in sandwixxh_orders:
#     print(f"I made your {sand}.")
#     finished_sandwixh.append(sand)

# for sandf in finished_sandwixh:
#     print(f"Sandwish now ready and available: {sandf}")
# # print(finished_sandwixh)

# ### 7th May, 2024
# ## Assignment - Write a simple program that generate randomly, a series of number, of 10 digits
# ## Note: Start the series integer 4.

import random
# rando_code = 4
# rando_num = "4" + str(random.randrange(000000000,999999999))
# print(f"Account Number Generated Successfully: {rando_num}")

# ## Guessing Game: 
# while True:
#     radom_guess = input("Enter your rando between 5 - 10: ")
#     comp_guess = random.randrange(5,10)
#     if radom_guess == comp_guess:
#         print(f"yOU GERRIT, computer guessed {comp_guess}")
#         break
#     else:
#         print(f"You missit, computer guessed {comp_guess}")


## Python Functions - a function is a block of organized reuseable code that perform task. It is ussualy called by its name when needed

## Why functiom:

## -- to avoid repition of code
### -- for code to run faster and easy readability
## -- for easy debugging

### Type of functions
## - Built-in function
## - User-defined function

## User defined function
### def function_name(): ## function definition
####    statement ### declaration
## function_name() ## function invocation or call

# def generate_name():
#     """Name of members of python class - dork strings"""
#     names = ['Iyanu','Yazir','Segun']
#     for name in names:
#         print(name)

# generate_name()

# Example 2
# dict1 = {}

# def user_info(): # Collects 5 names only!
#     Active = 0
#     while Active < 5:
#         name = input("Your name: ")
#         phone = int(input("11-digits: "))
#         dict1[name] = phone
#         Active += 1
#     print(dict1)

# user_info()

# dict1 = {}

# def user_info(): # Collects 5 names only!
#     for num_z in range(5):
#         name = input("Your name: ")
#         phone = int(input("11-digits: "))
#         dict1[name] = phone
#     print(dict1)

# user_info()

## Difference between print and return
## Print shows human a string representative of what is going on inside the computer

## Types of user-defined functions
## Parameterized and non-parameterized user declared function
## Parametrized functions ussually take aruments while non-paramterized function does not take any argument

### Parameterized user ceclared function declaration
#### 1. required argument
#### 2. keyword argument
#### 3. default argument
#### 4. variable lenght argument


## Required argument - the number of argument should be the same in boith d.def and f.call and position should be followed.

## example:
# def disp(a,b):
#     print(a,b)
# disp(20,10)

# def stude_name(namev,score):
#     print("The student name is - " + namev + ", scored -" + str(score))
#     stude_name("Yaz",90)

# stude_name()

## Keyword Aargument:
 ## Keyboard Argument - order/position is not required. Initialization is done based on keyword.

 ## aa = 100
 ## bb = 300
 ## cc = 40

#  def display(a,b,c):
#     print(a,c,b)

## display(aa,bb,cc)
# display(b=bb,c=cc,a=aa)

### 8th of MAY 2024
## Default argument - Number of arguments need not to be matched with both f.def and f.dcall

# def deff(name, course="Data Science"):
#     print(name)
# #     print(course)

# # deff(name='Gideon', course='Artificial Intelligence') ## The Argument in the the f-call will take precedence over the argument in f-def

# # ## Variables lenght argument - arbitrary number of arguments is passed by placing * as prefix to the argument of the f.def
# # ## * means args
# # ## ** kwargs

# # ## example
# # def displayed(name, data, *course):
# #     print(name, course)
# # displayed('Xav', 8, 'B.tech','m.tech','mica',31)

# # ### USING ARBITRARY KEYWORD ARGUMENT
# # def build_profile(first, last, **user_info):
# #     """bUILD DICTIONARY ABOUT EVERYTHING WE KNOW ABOUT A USER"""
# #     profile = {}
# #     profile['first_name'] = first
# #     profile['last_name'] = last
# #     for key, value in user_info.items():
# #         profile[key] = value
# #         # return profile # WHenever you use return assign it to a variable when calling the function

# # user_profile = build_profile('albert','eistein', location='princeton',field='physics')
# # print(user_profile)

# ### Write a program that works on args and kwargs
# ### Args *
# def scholarapplication(name, country, cert, *other_info):
#     print("Welcome to BBB Scholarhsip, see your info below")
#     print(cert, other_info)
# scholarapplication('Yaz','NG','BSC','Male',18,'Employed') 

# ##Kwargs **

# def floodvictimpackage(name, age, condition, **other_data):
#     print("Enter your details to qulify for the flood victim package")
#     info = {}
#     info[name] = name
#     info[age] = 91
#     info[condition] = condition
#     for l,k in other_data.items:

### Global and Local Variable
# def chewck():
#     global namqe ## make namqe a global variable
#     namqe = input("Your name: ")
#     pjone = input("Pjone num: ")

# chewck()
# print(namqe)



# ## Add contact number and name, search contact, delete contact
# phoneNum_Store = []
# first_store = {}

# def addPhone():
#     collect_num = input("Enter to add phone number: ")
#     collect_name = input("Enter contact name: ")
#     collect_org = input("Enter user Organization: ")
#     first_store[collect_name] = [collect_num, collect_org]
#     # first_store['User_Organiz'] = collect_org
#     # first_store['user_Name'] = collect_name
#     print(first_store)
#     # phoneNum_Store.append(first_store)

#     print(f"{collect_num} has been successfully added to your phone book as {collect_name}")
    

# def viewPhone():
#     for i,v in first_store.items():
#         if i == False:
#             print("We have no records")
#         else:
#             print(f"Name: {i} | Phone: {v[0]}")

# def deletePhone():
#     del_num = input("Enter the name of contact you want to delete ")
#     if del_num in first_store.keys():       
#         delete = first_store.pop(del_num)
#         print(f"{del_num} deleted.")

# def searchnum():
#     search_num = input("Enter the number you want to search: ")
#     for z in phoneNum_Store:
#         if z['user_Name'] == search_num:
#             print(z)


# print("Welcome to your Phone Book")
# while True:
#     actions = input("Enter - 1. View Contact 2. Add Contact 3. Delete Contact 4. Search Contact 5. Exit >>> ")
#     if actions == '1':
#         viewPhone()
#     elif actions == '2':
#         addPhone()
#     elif actions == '3':
#         deletePhone()
#     elif actions == '3':
#         searchnum()
#     else:
#         break

### Wekkend Assignment: 
##### Write a quiz app containing Objective questions. Return total score at the end of the quiz.
###(Optional - show after each answer. if the user is correcy or wromng) range the questions

# Q_Db = {1:["PDF","SQI","POP"], 2:["A. Mr Iyanu","B. Mr Seyi","C. Mr Bayo"], 3:["A. Yes","B. No","C. Maybe"], 4: ["A. Html","B. CSS","C. Python"], 5:["A. Source","B. Editor","C. Paper"]}
# Quest_box = ["What is your school name? ", "Instructor name? ","Is he a problem solvers? ","E.g of Scripting Language","Food is to plate, Code is to"]
# curr_score = 0
# print("Welcom to SQI BMAJ Exam >>-<< ")
# start_test = input("press 1 to start the test, any key to exit ")
# if start_test == "1":
#     for z,v in Q_Db.items():
#         if z == 1:
#             answer_1 = input(f"{z}. Question: {Quest_box[z-1]}: {Q_Db[z]} \nYour Answer: ").lower()
#             if answer_1 == "sqi" or answer_1 == "b":
#                 curr_score += 1
#         elif z == 2:
#             answer_1 = input(f"{z}. {Quest_box[z-1]}: {Q_Db[z]} \nYour Answer: ").lower()
#             if answer_1 == "mr iyanu" or answer_1 == "a":
#                 curr_score += 1
#         elif z == 3:
#             answer_1 = input(f"{z}. {Quest_box[z-1]}: {Q_Db[z]} \nYour Answer: ").lower()
#             if answer_1 == "yes" or answer_1 == "a":
#                 curr_score += 1
#         elif z == 4:
#             answer_1 = input(f"{z}. {Quest_box[z-1]}: {Q_Db[z]} \nYour Answer: ").lower()
#             if answer_1 == "python" or answer_1 == "c":
#                 curr_score += 1
#         elif z == 5:
#             answer_1 = input(f"{z}. {Quest_box[z-1]}: {Q_Db[z]} \nYour Answer: ").lower()
#             if answer_1 == "editor" or answer_1 == "b":
#                 curr_score += 1
#         else:
#             print("Done")
#     print("\nThanks for taking the Test ")
#     print(f">>>>>> You scored {curr_score} / 5")
# else:
#     print("See you soon, Bye!")

###  write a password generation program: letter, number and ymbles

# lez = ['A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e'
#        ,'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# num_rz = [0,1,2,3,4,5,6,7,8,9]
# symbz = ['!','@','#','$','%','^','&','*','-','+']

# fp = []
# ki = random.randint(2,5)
# le_repp = random.choices(lez,k=ki)
# # yyy = random.shuffle(le_repp) // reshuffle is for list
# # print(yyy)
# # print(le_repp)
# # lrepp = ''.join(map(str,le_repp))
# num_repp = random.choices(num_rz,k=ki)
# # print(num_repp)
# # # nrepp = ''.join(map(str,num_repp))
# symbz_repp = random.choices(symbz,k=ki)
# print(symbz_repp)

# fp = symbz_repp + num_repp + le_repp
# final_pwd = ''.join(str(po) for po in fp)
# print(final_pwd)

# # srepp = ''.join(map(str,symbz_repp))
# # shuf_io = lrepp + nrepp + srepp
# # print(shuf_io)
# # final_pass = random.shuffle(shuf_io). 

### Assignment: Park system**
### Design a software that designs recharge card e.g 1771-1017-1663-9911
    ## -> Create Dealer account/pwd/balance(wallet)
    ## -> Ask for unit you want to print and how much
    ## -> Print card #100 and sell to dealer at the rate of 80naira
    ## -> #200 card = #160, #100 = #80.

## recharge card - store, print units, price, discount.

card_stored = []
user_account = {}

def addCustomer():
    collect_name = input("Enter contact name: ")
    collect_org = input("Enter user Organization: ")
    collect_email = input("Enter your email address: ")
    collect_pass = input("Enter your password: ")
    user_account[collect_org] = [collect_name, collect_org, collect_email, collect_pass]
    # first_store['User_Organiz'] = collect_org
    # first_store['user_Name'] = collect_name
    print(user_account)
    loginCustomer()
    contd = input("Do you wanna purchase Airtime? Yes or No? ")
    if contd.lower() == 'yes':
        createCode()
    else:
        print('<<<<< Good Bye, Login when you want to buy Airtime!')
        loginCustomer()

    # phoneNum_Store.append(first_store)

#     print(f"{collect_num} has been successfully added to your phone book as {collect_name}")

# def loginCustomer():
#     collect_org = input("Login Panel >>> Enter your Organization name: ")
#     for i in user_account.keys():
#         if i == collect_org:
#             for v in user_account.values():
#                 collect_email = input("Enter your email address: ")
#                 collect_pass = input("Enter your password: ")
#                 if collect_email == user_account[collect_org][2] and collect_pass == user_account[collect_org][3]:
#                     print(f"Hello {user_account[collect_org][1]}, ")
#                 else:
#                     print("Email or Password Incorrect")
#         else:
#             print("Sorry your Organization is not registered")
    
# import random
# def createCode():
#     price = input('Price of card? ')
#     unitz = input(f'How many units of #{price} card? ')
#     if price == '200':
#         for lo in range(int(unitz)):
#             card = random.randrange(20000000000,29999999999)
#             card_stored.append(card)
#         Agreed = input(f'You will be charged {int(unitz) * 160} naira. Proceed? Y or N ')
#         print(card_stored)
#     elif price == '100':
#         for lo in range(int(unitz)):
#             card = random.randrange(10000000000,19999999999)
#             card_stored.append(card)
#         Agreed = input(f'You will be charged {int(unitz) * 80} naira. Proceed? Y or N ')
#         if Agreed.lower() == 'y':
#             print(card_stored)
#         else:
#             exit
#     else:
#         print("We don't have that price now!")
# # random.shuffle()

# while True:
#     print('<<<<<<<< Welcome to Airtime Treez >>>>>>>>>>')
#     progra = input('1. Create User 2. Login User 3. Purchase Airtime ')
#     if progra == '1':
#         addCustomer()
#     elif progra == '2':
#         loginCustomer()
#     elif progra == '3':
#         createCode()
#     else:
#         break

## 21st of May, 2024
# OBJECT ORIENTED PROGRAMMING
# In python, classes are a fundaemntal part of objct oriented programming, allowin us to create complex data structures that bundle data
# and functionalities together.

## Class: A class is made up of two things: functions and attributes(variables that hold data) They are called class members
## This class member can be accessed as object   

# class Dog():
#     """A simple attempt to model a dog"""
#     # constructor
#     def __init__(self):
#         self.name = "Bryno"
#         self.age = "5 years"
#         self.date = "21st"

#     def sit(self):
#         return (f"{self.name} is now sitting, age is {self.age}")
    
#     def roll_over(self):
#         return (f"{self.name} is now rolling")
    
# d = Dog()


# import random
# class Myclass():

#     def __init__(self, name):
#         self.name = name
#         self.id = random.randint(1000,2000)

#     def generate(self):
#         return f"{self.name} - id = {self.id}"

# m = Myclass('Iyanu')

# print(m.generate())

# class without method
# class person():
#     def __init__(self, name):
#         # CLASS attributes 
#         self.name = name
#         self.age = '26'

#     def write(self):
#         return f"My is {self.name} "

# p = person('Seqz')
# print(p.name)
# print(p.write())


# class Student_record:
#     # constructor
#     def __init__(self, name, level, course):
#         ## attributes
#         self.name = name
#         self.level = level
#         self.course = course
    
#     #method
#     def record(self):
#         print(f"My name is {self.name}, studying {self.course}. I'm in level {self.level} ")


#     def attend(self):
#         print(f"Mr {self.name} Arrived")



# ## Create Instances
# ## instance 1
# stu_rec = Student_record('Bolu','100','Information Science')

# ## instance 2:
# stu_rec2 = Student_record('Jackson','300','Web Dev')

# stu_rec3 = Student_record('Jackson','','')

# stu_rec3.attend()
# # stu_rec.record()
# # stu_rec2.record()

# ##2nd May 2024



# class Book():

#     def __init__(self, title, author, isbn, available):
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#         self.available = True

#     def borrow(self):
#        if self.available:
#            self.available = True
#            return True
#        return False
    

#     def return_booK(self) :
#         self.available = True

# book1 = Book('Goals','Brian Tracy','1234-US')
# input_author = input('')
# book2 = Book('Test Book',input_author,'1234-pol')
# print(book1.borrow())
# print(book1.author)



### Task:

# class Restaurant():

#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(f"Welcome to {self.restaurant_name}, we have {self.cuisine_type} cuisine here")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open")
    
# restaurant = Restaurant('Aroma','Yoruba')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()



## 28/05/2024

### Python Inheritance - means acquiring properties, 
##### derived class(child) depends on the Base class(parent class)
## Through the object of the drived class we can access properties of both parent and the child class.

## Types of inheritance
# 1. Single Inheritance
# 2. Multi-level Inheritance

# ## 1. Single Inheritance - Only have one base class and one derived class
# class School(object):
#     def __init__(self):
#         self.name = "SQI coding school"
#         self.numofCourses = "20"

#     def intro(self):
#         print(f"Name of School is {self.name}")

# class Department(School):
#     def course(self):
#         print('Data science')
    
# d = Department()
# d.intro()

# ## Example 2:
# class Parent(object):
#     def __init__(self):
#         self.name = "Kunle"
#     def describe(self):
#         print("My name is " + self.name)

# class Child(Parent):
#     def child(self):
#         print(f"I am the child of Mr {self.name}")

# c1 = Child()
# c1.describe()

# ### 2. Multi-level Inheritance
# # # grandparent == parent == child == grandchild == greatgrandchild

# class Grandparent(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(f"my name is Granny {self.name}, I am {self.age} years old")

# class Parent(Grandparent):
#     def parent_talk(self):
#         self.parentname = "Adedoyin"
#         print(f"My name is {self.parentname} I am the child of {self.name} ")
#         print(f"My father is {self.age} years of age")


# class Child(Parent):
#     def child_talk(self):
#         print(f"My grandpa = {self.name} is {self.age} years of age. ")

# class Grandchild(Child):
#     def talkative(self):
#         print(f"My greatgrandpa's name is {self.name}, my grandpa's name is {self.parentname} ")

# c = Child('74')
# c.parent_talk()

# class Critter(object):
    
#     def __init__(self,name):
#         self.name = name
#         print("A new critter has been born")

#     def __str__(self):
#         rep = "Critter object \n"
#         rep += "name:  " + self.name + "\n"
#         return rep
    
#     def talk(self):
#         print("Hi, I am " + self.name + ".\n")


# crit1 = Critter("Poochie") 

### Task:
## Write Quiz program using classes, expected output - print out question one by looping through the list - question_data

## Ask True or False - compare response to answer in list
## Record score amd print out final score

question_data= [
    {"text":"Tinubu is Nigeria president? ","answer":"True"},
    {"text":"We have 18 states in Nigeria? ", "answer":"False"},
    {"text":"Learning python is sweet? ","answer":"False"},
    {"text":"Human can run faster than horse? ","answer":"False"},
    {"text":"Sun is the solar system?","answer":"True"},
    {"text":"Water is the most available sustance on earth","answer":"True"}
]


        # print()


class Questions:
    def __init__(self, question_text):
        self.question_text = question_text
    
    def display(self):
        input(f" Question: {self.question_text} True or False")
           
    


for pp in question_data:
        bl = Questions(pp['text'])
        bl.display()


## With classes and module, write a program that registers members of an organization, generate ids for the member with prefix AR-****. The program should be able to view all members and add a input of an ID where it displays information of an individual users(First_name, Second_name, State of Origin)

class Organization():
     
     def __init__(self, first_name, second_name, state_origin):
          self.first_name = first_name
          self.second_name = second_name
          self.state_origin = state_origin

    # def register_member():     