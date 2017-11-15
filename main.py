import random
from classes.student import Student
from classes.course import Course

if __name__== "__main__":
    print "Tooooo"

with open ("courses.txt", "r") as f:
    lines = f.readlines()
    
    courses = []
    data = []
    for line in lines :
        if not line.startswith ("#"):
            data.append (line.strip() )
    for line in data:
        x = line.split('|')
        if x[0].strip() == "Course":
            name = x[1].strip()
            code = x[2].strip()
            courses.append( Course (name, code) )
        elif x[0].strip() == "Running":
            year = int (x[1])
            courses [-1].add_running(year)
    
    for course in courses:
        print course
           

   