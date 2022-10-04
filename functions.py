
from ast import IsNot


class Student:
    def __init__(self, lName, fName, gde, croom, bs, gpa, tLname, tFname):
        self.lName = lName
        self.fName = fName 
        self.gde = gde
        self.croom = croom
        self.bs = bs
        self.gpa = gpa
        self.tLname = tLname
        self.tFname = tFname




def startMenu(studentList):
    print("Hello! Please enter any of the following choices (NOTE: Anything in brackets[] is optional input, anything in angle brackets is your input)")
    print("S[tudent]: <lastname> [B[us]]")
    myInput = list(input("Enter your option here: ").split(" "))
    option = myInput[0]
    nameNumber = myInput[1]

    
    if (option == "S:" or "Student:") and myInput[2] == "B" or "Bus":
        studentBusSearch(nameNumber, studentList)


def studentSearch(name, studentList):
    count = 0
    while count <60:
        if name != studentList[count].lName:
            count += 1
        elif name == studentList[count].lName:
            print(studentList[count].lName, studentList[count].fName, studentList[count].gde, studentList[count].croom, studentList[count].tLname, studentList[count].tFname)
            count+=1
    

def studentBusSearch(name, studentList):
    count = 60
    while count <60:
        if name != studentList[count].lName:
            count+=1
        elif name == studentList[count].lName:
            print(studentList[count].lName, studentList[count].fName, studentList[count].bs)
            count +=1



