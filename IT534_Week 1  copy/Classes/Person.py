class Person():
    """Create a Class Person()
Create constructor that assigns the values to the Parameters:
1. name 
2. email
3. id
Create Display Information function:
Returns Values:
1. Name
2. Email
3. ID
    """
    def __init__(self, name, email, id):
        self.name = name
        self.email = email
        self.id = id

    def displayInformation(self):
        print("Name: " + self.name)
        print("Email: " + self.email)
        print("ID: " + self.id)
