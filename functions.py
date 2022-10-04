
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
    print("T[eacher]: <lastname>")
    print("B[us]: <number>")
    print("G[rade]: <number> [H[igh] or [L[ow]")
    print("A[verage]: <number>")
    print("I[nfo]")
    print("Q[uit]")
    myInput = list(input("Enter your option here: ").split(" "))
    option = myInput[0]
    while (myInput[0] != "Q" or myInput[0] != "Quit"):
        if len(myInput)==1:
            if (option == "I" or option == "Info"):
                infoFunc(studentList)
                startMenu(studentList)
            if(option == "Q" or option == "Quit"):
                quit()
        if len(myInput) ==2:
            if (option == "S:" or option == "Student:"):
                studentSearch(myInput[1], studentList)
                startMenu(studentList)
            elif (option =="T:" or option == "Teacher:"):
                teacherSearch(myInput[1], studentList)
                startMenu(studentList)
            elif(option =="B:" or option =="Bus:"):
                busSearch(myInput[1], studentList)
                startMenu(studentList)
            elif(option =="G:" or option == "Grade:"):
                gradeSearch(myInput[1], studentList)
                startMenu(studentList)
            elif(option == "A:" or option == "Average:"):
                avg = averageFunc(myInput[1], studentList)
                print(avg)
                startMenu(studentList)
        elif len(myInput) ==3:
            if(option == "S:" or option == "Student:") and (myInput[2] == "B" or myInput[2] == "Bus"):
                studentBusSearch(myInput[1], studentList)
                startMenu(studentList)
            elif(option == "G:" or option == "Grade:") and (myInput[2]== "H" or myInput[2] =="High"):
                high = gradeSearchHigh(myInput[1], studentList)
                print("Grade: ", myInput[1], "Average GPA: ", high) 
                startMenu(studentList)
            elif(option == "G:" or option == "Grade:") and (myInput[2] == "L" or myInput[2] =="Low"):
                low =gradeSearchLow(myInput[1], studentList)
                print(low)
                startMenu(studentList)




def studentSearch(name, studentList):
    count = 0
    while count <60:
        if name != studentList[count].lName:
            count += 1
        elif name == studentList[count].lName:
            print(studentList[count].lName, studentList[count].fName, studentList[count].gde, studentList[count].croom, studentList[count].tLname, studentList[count].tFname)
            count+=1
    

def studentBusSearch(name, studentList):
    count = 0
    while count <60:
        if name != studentList[count].lName:
            count+=1
        elif name == studentList[count].lName:
            print(studentList[count].lName, studentList[count].fName, studentList[count].bs)
            count +=1

def teacherSearch(name, studentList):
    count =0
    while count < 60:
        if name != studentList[count].tLname:
            count +=1
        elif name == studentList[count].tLname:
            print(studentList[count].lName, studentList[count].fName)
            count +=1


def busSearch(name, studentList):
    count = 0
    while count < 60:
        if name != studentList[count].bs:
            count+=1
        elif name == studentList[count].bs:
            print(studentList[count].lName, studentList[count].fName, studentList[count].gde, studentList[count].croom)
            count += 1

def gradeSearch(name, studentList):
    count = 0
    while count < 60:
        if name != studentList[count].gde:
            count +=1
        elif name == studentList[count].gde:
            print(studentList[count].lName, studentList[count].fName, studentList[count].gpa)
            count +=1

def gradeSearchHigh(number, studentList):
    count =0
    max = 0
    while count < 60:
        if number != studentList[count].gde:
            count +=1
        elif number == studentList[count].gde:
                num = float (studentList[count].gpa)
                if num > max:
                    max = num
                    count+=1
                elif num < max:
                        count+=1                  
    return max   
                
                    
            
                    
def gradeSearchLow(number, studentList):
    count = 0
    low = 50
    while count < 60:
        if number != studentList[count].gde:
            count += 1
        elif number == studentList[count].gde:
            num = float(studentList[count].gpa)
            if num < low:
                low = num
                count +=1
            elif num > low:
                count+=1
    return low    


def averageFunc(number, studentList):
    count =0
    occassions =0
    sum =0
    while count < 60:
        if number != studentList[count].gde:
            count +=1
        elif number == studentList[count].gde:
            sum = sum + float (studentList[count].gpa)
            occassions +=1
            count +=1
    print(occassions)
    return sum/occassions 


def infoFunc(studentList):
    count = 0
    g1 =0
    g2=0
    g3 =0
    g4 =0
    g5 = 0
    g6 = 0

    while count < 60:
        num = int(studentList[count].gde)
        if num ==1:
            g1 +=1
        elif num ==2:
            g2 +=1
        elif num == 3:
            g3 +=1
        elif num == 4:
            g4 +=1
        elif num ==5:
            g4 +=1
        elif num ==5:
            g5 += 1
        elif num ==6:
            g6 +=1
        count +=1

    print("Grade 1: ", g1, " students.")
    print ("Grade 2: ", g2, " students.")
    print ("Grade 3: ", g3, " students.")
    print ("Grade 4: ", g4, " students.")
    print ("Grade 5: ", g5, " students")
    print ("Grade 6: ", g6, " students.")
