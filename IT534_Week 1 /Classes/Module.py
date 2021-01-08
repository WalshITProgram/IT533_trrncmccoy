class Person():

    def __init__(self, name, email, id, program, degree, institution):
        self.name = name
        self.email = email
        self.id = id
        self.program = program
        self.degree = degree
        self.institution = institution

    def displayInformation(self):
        print("Name: " + self.name)
        print("Email: " + self.name)
        print("ID: " + self.id)
