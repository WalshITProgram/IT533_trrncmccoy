class Person():

    def __init__(self, name, email, id):
        self.name = name
        self.email = email
        self.id = id

    def displayInformation(self):
        print("Name: " + self.name)
        print("Email: " + self.email)
        print("ID: " + self.id)
