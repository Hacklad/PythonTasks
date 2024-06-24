#  with classes and module, write a program that registers members of an organization, generate ids for the member with prefix AR-****. The program should be able to view all members and add a input of an ID where it displays information of an individual users(First_name, Second_name, State of Origin)

class Organization():
     
     def __init__(self, first_name, second_name, state_origin):
          self.first_name = first_name
          self.second_name = second_name
          self.state_origin = state_origin

    # def register_member():
     