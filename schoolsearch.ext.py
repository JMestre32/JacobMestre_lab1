import sys

class Student:
    def __init__(self, lName, fName, gde, croom, bs, gpa, tLname, tFname):
        self.lName = lName
        self.fName = fName 
        self.gde = gde
        self.croom = croom
        self.bs = bs
        self.gpa = gpa
        self.tlName = tLname
        self.tfName = tFname


def studentSearch(stLastName, stFirstName, grade, classroom, bus, gpa, tLastName, tFirstName):
    print("check")



def main():
    count = 0
    array =[]
    studentList =[]
    text_file = open("students.txt", "r") 
    array = text_file.read().split(',')
    if count < len(array):
        studentList.append(Student(array[0], array[1], array[2], array[3],array[4], array[5], array[6], array[7]))
        count += 1

    for obj in studentList:
        print(obj.fName)  

if __name__ =="__main__":
    main()