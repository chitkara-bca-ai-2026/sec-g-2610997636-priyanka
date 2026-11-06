print("==================================================")
print("             SCHOOL RESULT PROCESSING             ")
print("==================================================")

student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number :")
print("\n--- Enter Marks for 5 Subjects (0-100) ---")

total_marks = 0
failed = False

for i in range(1,6):
    marks = float(input("Enter marks for Subjects " + str(i) + ": "))

    if marks < 0 or marks > 100:
        print("Invalid Marks! Please enter between 0 and 100.")
        exit()

    total_marks = total_marks + marks

    if marks < 40:
        failed = True

percentage = (total_marks / 500) * 100
if failed == True:
    result = "FAIL"
    grade = "F"
    remarks = "Failed in one or more subjects"

else:
    result = "PASS"

    if percentage >= 90:
        grade ="A+"
        remarks = "Outstanding"

    elif percentage >= 80:
            grade ="A"
            remarks = "Excellent"

    elif percentage >= 70:
            grade ="B"
            remarks = "Very Good"

    elif percentage >= 60:
            grade ="C"
            remarks = "Good"

    elif percentage >= 50:
            grade ="D"
            remarks = "Satisfactory"

    elif percentage >= 40:
            grade ="E"
            remarks = "Pass"

    else:
          grade = "F"
          remarks = "Fail"

print("\n================================================")
print("               STUDENT REPORT CARD")
print("================================================")

print("Student Name :", student_name)
print("Roll Number  :", roll_number)

print("------------------------------------------------")
print("Total Marks :", total_marks, "/ 500.0")
print("Percentage  :", format(percentage, '.2f') + "%")
print("Result      :", result)
print("Grade       :", grade)
print("Remarks     :", remarks)

print("================================================")

    