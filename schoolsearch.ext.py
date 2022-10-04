import sys
from functions import *

def main():
    count = 0
    n = 0
    array =[]
    studentList =[]
    text_file = open("students.txt", "r") 
    array = text_file.readlines()
    for line in array:
       textLine = line.split(",")
       studentList.append(Student(textLine[0], textLine[1], textLine[2], textLine[3],textLine[4], textLine[5], textLine[6], textLine[7]))
    startMenu(studentList)
    

if __name__ =="__main__":
    main()