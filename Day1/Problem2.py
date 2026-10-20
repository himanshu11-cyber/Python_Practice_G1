Name = input("Enter your name: ")
print (len(Name))
print (Name.count("l"))


Student_marks = int(input("Enter your marks: "))

if(Student_marks >= 90):
    print(Name + " got an A")
elif(Student_marks >= 80):
    print(Name + " got a B")
else:
    print(Name + " got a C")