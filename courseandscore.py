## Assignment 

### Write a simple python program that will request for the name of the user and the course. Take in two Values (first value as exam score and second value as test score). It will then add the two values and display the result in a simple sentence as below:

## The output should look like "Welcome Lingz, your total score in English Language is 79."

print('Welcome to Result Portal')
name = input('Enter your name ')
course = input('Enter your course ')
testScore = int(input('Enter your test score '))
examScore = int(input('Enter your Exam score '))
totalScore = str(testScore + examScore)
print('Welcome ' + name + ', your total score in ' + course + ' is ' + totalScore + '.')
