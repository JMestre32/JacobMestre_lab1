import sys
from functions import *

def main():
    count = 0
    n = 0
    array =[]
    studentList =[]
    text_file = open("students.txt", "r") 
    array = text_file.read().split(',')
    while count < 60:
        studentList.append(Student(array[n], array[n+1], array[n+2], array[n+3],array[n+4], array[n+5], array[n+6], array[n+7]))
        count += 1
        n+=7
    studentSearch()
    

if __name__ =="__main__":
    main()