class Member:
    def __init__(self,firstName,lastName,email,mobileNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.mobileNumber = mobileNumber
    
    def getFullName(self):
        print(self.firstName+" "+self.lastName)
        
    def changeNumber(self,newNumber):
        self.mobileNumber=newNumber
        print("Mobile number changed successfully")
        
    def changeEmail(self,newEmai):
        self.email=newEmai
        print('Email changed successfully')
        

class Faculty(Member):
    def __init__(self,firstName,lastName,email,mobileNumber,salary):
        self.salary = salary
        Member.__init__(self,firstName,lastName,email,mobileNumber)
        
    def getSalary(self):
        print('your salary:',self.salary)


class Student(Member):
    def __init__(self,firstName,lastName,email,mobileNumber,GPA):
        self.GPA=GPA
        Member.__init__(self,firstName,lastName,email,mobileNumber)
        
    def getGPA(self):
        print('get your GPA:',self.GPA)
        

std1=Student('ABC',' DEF','test_email','12345','93.9')
print(std1.email)
print(std1.firstName)
print(std1.lastName)
print(std1.mobileNumber)

std1.changeEmail('changed_email')
std1.changeNumber('9999999_changed_Number')


print('\n',std1.mobileNumber)
print(std1.email)