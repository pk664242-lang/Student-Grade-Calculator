name = input("Enter Student Name: ")
marks = float(input("Enter Marks (out of 100): "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("\n----- Result -----")
print("Student Name:", name)
print("Marks:", marks)
print("Grade:", grade)