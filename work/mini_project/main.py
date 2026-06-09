


student = {}

"""
student :{
    student_id:{
        Name =
        age =
        course =
        attendance_percentage =
        marks =
        grade =
    }
}
"""

print("------STUDENT_MANAGEMENT_SYSTEM--------")
print("option[1]: STUDENT REGISTRATION")
print("option[2]: STUDENT PROFILE MANAGEMENT")
print("option[3]: COURSE ENROLLMENT")
print("option[4]: ATTENDANCE TRACKING")
print("option[5]: MARKS ENTRY AND GRADE CALCULATION")
print("option[6]: GENERATE REPORT")
print("option[7]: SHOW ALL STUDENTS")

while(True):
    option1 = int((input("enter your option: ")))
    if(option1==1):
        student_id = int(input("enter student ID: "))
        if(student_id in student):
            print("student ID already exists")
        else:
            print(f"student_id = {student_id}")
            name = input("enter student name: ")
            age = int(input("enter student age: "))

        
        student[student_id] = {
            "Name" : name,
            "age" : age,
            "course" : 0,
            "attendance_percentage" : 0,
            "marks" : 0,
            "grade" : 0
        }

        print("STUDENT REGISTERED")

    elif(option1==2):
        student_id = int(input("enter student ID: "))
    
        if(student_id in student):
            print("[21]: view profile")
            print("[22]: update name")
            print("[23]: update age")
            
            while(True):
                option2 = int(input("enter your option: "))

                if(option2==21):
                    print(student[student_id])
                elif(option2==22):
                    new_name = input("enter your new name: ")
                    student[student_id]["Name"]=new_name
                elif(option2==23):
                    new_age = input("enter your new age: ")
                    student[student_id]["age"]=new_age
                elif(option2==24):
                    break
        else:
            print("student does not exist")

    