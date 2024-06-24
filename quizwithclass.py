#  Task:
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

