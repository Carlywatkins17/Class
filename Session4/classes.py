class Student:
    def _init_(self,name= '', ID= -1, birthdate='1/1/2000')
        self.name = name
        self.ID = ID
        self.birthdate = DOB

    def study(self):
        print(self.name + ' is studying')

    def do_homework(self, course):
        print(self.name + ' is doing homework for their ' + course + ' course.')

    def ask_question(self):
        print('Wait, what?')

cs100a = []
name = ''
while name.lower() != 'done':
    name = input('Please enter student name, or done: ')
    if name.lower != 'done' :
        id = int(input('\t') + name + 'id number: ')
   

for stud in cs100a:
        print(stud.name)
        print('\t' + str(stud.ID))
        print('\t' + stud.birthdate)

print(stud.study())
 

