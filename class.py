class Coursereg:
    def newcourse(course):
        print("new course is here: " + course)

Coursereg.newcourse("control system")

class Students():
    def __init__(self, name, id): #construction formula
        self.stuname= name #self.entity=var
        self.stuid= id
    def showstudent(self): #attributes
        print("New student: " + self.stuname + " ID: " + self.stuid)
jamie= Students("jamie", "s123456") #object
jamie.showstudent()

class Event():
    def __init__(self, id):
        self.urid= id
    def join(self):
        parid=["s123456","s234567","s345678"]
        if self.urid in parid:
            print("Duplicate Registration")
        else:
            print(self.urid + "Registration Successful")

lauren= Event("s123456")
lauren.join()
