from Classes.Person import Person
class Instructor(Person):
    """Create a Instuctor subclass 
Create constructor:
1. Inherit the constructor from the Parent Class.
Create Display Information function:
Returns Values:
1. Name
2. Email
3. ID
    """
    def __init__(self, name, id, email , degree, institution):
        super().__init__(name, email, id)
        self.degree = degree
        self.institution = institution

    def displayInformation(self):
        print("Name:" + self.name)
        print("Email:" + self.email)
        print("ID:" + self.id)
        print("Degree: " + self.degree)
        print("Institution: " + self.institution)
    