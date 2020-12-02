class Person:
    def __init__(self, name, job, pay):
        self.name = name
        self.job = job
        self.pay = pay

    def Lastname(self):
        return self.name.split()[-1]
    def Raise(self, percent):
        self.pay = int(self.pay *  (1 + percent))

    def __repr__(self):
        return '[Person: %s, %s, %s]' % (self.name, self.job, self.pay)
    
class Manager(Person): 
    def Raise(self, percent, bonus=.10):
        Person.Raise(self, percent + bonus)

if __name__=='__main__':
    cam = Person('James Evans', 'CIO', 89)
    bob = Manager('Lisa Raye',  'Actress',  89)
    cam.Raise(.50)
    bob.Raise(.50)
    print(cam)
    print(bob)


