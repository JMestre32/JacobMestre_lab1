import sys
from functions import *

def main():
    count = 0
    n = 0
    array =[]
    studentList =[]
    text_file = open("students.txt", "r") 
    array = text_file.readlines()
    #while count < 60:
     #   studentList.append(Student(textLine[n], textLine[n+1], textLine[n+2], textLine[n+3],textLine[n+4], textLine[n+5], textLine[n+6], textLine[n+7]))
      #  count += 1
       # n+=7
    for line in array:
       textLine = line.split(",")
       studentList.append(Student(textLine[0], textLine[1], textLine[2], textLine[3],textLine[4], textLine[5], textLine[6], textLine[7]))
    print(studentList[0].tFname)
    print(studentList[1].lName)
    startMenu(studentList)
    

if __name__ =="__main__":
    main()