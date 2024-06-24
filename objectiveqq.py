##### Write a quiz app containing Objective questions. Return total score at the end of the quiz.
###(Optional - show after each answer. if the user is correcy or wromng) range the questions

Q_Db = {1:["PDF","SQI","POP"], 2:["A. Mr Iyanu","B. Mr Seyi","C. Mr Bayo"], 3:["A. Yes","B. No","C. Maybe"], 4: ["A. Html","B. CSS","C. Python"], 5:["A. Source","B. Editor","C. Paper"]}
Quest_box = ["What is your school name? ", "Instructor name? ","Is he a problem solvers? ","E.g of Scripting Language","Food is to plate, Code is to"]
curr_score = 0
print("Welcom to SQI BMAJ Exam >>-<< ")
start_test = input("press 1 to start the test, any key to exit ")
if start_test == "1":
    for z,v in Q_Db.items():
        if z == 1:
            answer_1 = input(f"{z}. Question: {Quest_box[z-1]}: {Q_Db[z]} \nYour Answer: ").lower()
            if answer_1 == "sqi" or answer_1 == "b":
                curr_score += 1
        elif z == 2:
            answer_1 = input(f"{z}. {Quest_box[z-1]}: {Q_Db[z]} \nYour Answer: ").lower()
            if answer_1 == "mr iyanu" or answer_1 == "a":
                curr_score += 1
        elif z == 3:
            answer_1 = input(f"{z}. {Quest_box[z-1]}: {Q_Db[z]} \nYour Answer: ").lower()
            if answer_1 == "yes" or answer_1 == "a":
                curr_score += 1
        elif z == 4:
            answer_1 = input(f"{z}. {Quest_box[z-1]}: {Q_Db[z]} \nYour Answer: ").lower()
            if answer_1 == "python" or answer_1 == "c":
                curr_score += 1
        elif z == 5:
            answer_1 = input(f"{z}. {Quest_box[z-1]}: {Q_Db[z]} \nYour Answer: ").lower()
            if answer_1 == "editor" or answer_1 == "b":
                curr_score += 1
        else:
            print("Done")
    print("\nThanks for taking the Test ")
    print(f">>>>>> You scored {curr_score} / 5")
else:
    print("See you soon, Bye!")
