from Classes.Person import Person
class Student(Person):

    def __init__(self, name, email, id, program):
        super().__init__(name, email, id)
        self.program = program

    def displayInformation(self):
        print("Name:" + self.name)
        print("Email" + self.email)
        print("ID" + self.id)
        print("Program: " + self.program)