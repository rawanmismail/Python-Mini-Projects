student = {
    "name": "Jamie Brown",
    "age": 20,
    "nationality": "Canadian",
    "visa": "International Student Visa",
    "major": "Computer Science",
    "GPA": 4.0,
    "expected_graduation_year": 2030,
    "scholarship": "20% Scholarship",
    "overall fees": "$50,000"
}


student.pop("nationality") #Removes the nationality part


print("      ========= Student Information: ========= ")
print(f"This is the data regarding {student['name']} who is {student['age']} years old.")
print(f"Visa Status: {student['visa']}")
print(f"Major: {student['major']}")
print(f"GPA: {student['GPA']}")
print(f"Expected Graduation Year: {student['expected_graduation_year']}")
print(f"Scholarship Status: {student['scholarship']}" + " on Year 2 fees")
print(f"Overall Fees: {student['overall fees']}")
print("       ========= This is the end of the generated report ========= ")



# Checking if a key exists: 
if "scholarship" in student:
    print("FOUND scholarship")

if "scholarship" not in student:
    print("NOT FOUND scholarship")