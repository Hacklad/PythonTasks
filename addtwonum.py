## Write a program that will ask the user to supply two values using one variable, then perform all the set opeartion depending
## on the choice of the user - addition, substraction, division and multiplication.

acc = input("Enter two numbers: ").split(",")
mathz = input("Enter 1 to Add, 2 to subtract, 3 to multiply, 4 to divide: ")
if mathz == '1':
    final_rec = int(acc[0]) + int(acc[1])
    print(f"{acc[0]} + {acc[1]} is equal to {final_rec}")
elif mathz == '2':
    final_rec = int(acc[0]) - int(acc[1])
    print(f"{acc[0]} - {acc[1]} is equal to {final_rec}")
elif mathz == '3':
    final_rec = int(acc[0]) * int(acc[1])
    print(f"{acc[0]} x {acc[1]} is equal to {final_rec}")
elif mathz == '4':
    final_rec = int(acc[0]) / int(acc[1])
    print(f"{acc[0]} / {acc[1]} is equal to {final_rec}")
else:
    print("You entered a wrong value sir!")

