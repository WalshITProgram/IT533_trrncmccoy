from Classes.Person import Person
class Student(Person):
    """Create a Student subclass 
Create constructor:
1. Inherit the constructor from the Parent Class.
Create Display Information function:
Returns Values:
1. Name
2. Email
3. ID
    """
    def __init__(self, name, email, id, program):
        super().__init__(name, email, id)
        self.program = program

    def displayInformation(self):
        print("Name:" + self.name)
        print("Email" + self.email)
        print("ID" + self.id)
        print("Program: " + self.program)