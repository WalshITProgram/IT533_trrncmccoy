class Individual():
    def __init__(self, name, email, id_number):
        self.name = name
        self.email = email
        self.id_number = id_number

    def DisplayInfo(self):
        print("Name:", name)
        print("Email:", email)
        print("ID:", id_number)
        
class Student(Individual):
    def __init__(self, name, email, id_number, major):
        super().__init__(name, email, id_number)
        self.major = major

    def DisplayInfo(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("ID:", self.id_number )
        print("Current Major:", self.major)

class Instructor(Individual):
    def __init__(self, name, email, id_number, institution, Highest_degree):
        super().__init__(name, email, id_number)
        self.institution = institution
        self.Highest_degree = Highest_degree


    def DisplayInfo(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("ID:", self.id_number )
        print("Last College Enrolled:", self.institution)
        print("Highest Degree recieved:", self.Highest_degree)