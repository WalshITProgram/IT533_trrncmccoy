from Classes.Person import Person
class Instructor(Person):


    def __init__(self, name, email , degree, institution):
        super().__init__(name, email, id)
        self.degree = degree
        self.institution = institution

    def displayInformation(self):
        print("Name:" + self.name)
        print("Email:" + self.email)
        print("ID:" + self.id)
        print("Degree: " + self.degree)
        print("Institution: " + self.institution)
    