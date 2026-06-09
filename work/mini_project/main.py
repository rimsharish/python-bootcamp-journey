


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
            "course" : "not enrolled yet",
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
                    new_name = input("enter new name: ")
                    student[student_id]["Name"]=new_name
                elif(option2==23):
                    new_age = input("enter new age: ")
                    student[student_id]["age"]=new_age
                elif(option2==24):
                    break
        else:
            print("student does not exist")

    elif(option1==3):
        student_id = int(input("enter student ID: "))
    
        if(student_id in student):
            course = input("enter course name: ")
            student[student_id]["course"]=course
            print(student[student_id])
        else:
            print("student does not exist")

    elif(option1==4):
        student_id = int(input("enter student ID: "))
    
        if(student_id in student):
            total_classes = int(input("enter total no. of classes: "))
            classes_attended = int(input("enter the no. of classes attended: "))
            att_percentage = (classes_attended/total_classes)*100
            print(f"attendance percentage: {att_percentage}%")
            student[student_id]["attendance_percentage"]=att_percentage
            print(student[student_id])
        else:
            print("student does not exist")

    elif(option1==5):
        student_id = int(input("enter student ID: "))
    
        if(student_id in student):
            marks = int(input("enter marks(10-100): "))
            student[student_id]["marks"]=marks

            if(90<=marks<=100):
                student[student_id]["grade"]="A"
            if(80<=marks<=89):
                student[student_id]["grade"]="B"
            if(70<=marks<=79):
                student[student_id]["grade"]="C"
            if(60<=marks<=69):
                student[student_id]["grade"]="D"
            if(marks<60):
                student[student_id]["grade"]="E"
            print(student[student_id])
        else:
            print("student does not exist")

    elif(option1==6):
        student_id = int(input("enter student ID: "))
    
        if(student_id in student):
            print("----STUDENT REPORT-----")
            print(f"student id: {student_id}")
            print(f"name: {student[student_id]["Name"]}")
            print(f"age: {student[student_id]["age"]}")
            print(f"course: {student[student_id]["course"]}")
            print(f"attendance percentage: {student[student_id]["attendance_percentage"]}")
            print(f"marks: {student[student_id]["marks"]}")
            print(f"grade: {student[student_id]["grade"]}")
        else:
            print("student does not exist")

    elif(option1==7):
        for student_id in student:
            print(f"{student_id} : {student[student_id]["Name"]}")

    elif(option1==8):
        break
