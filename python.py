student_1 = {
    "name": "Jamie Brown",
    "age": 20,
    "nationality": "Canadian",
    "visa": "International Student Visa",
    "major": "Computer Science",
    "GPA": 4.0,
    "expected_graduation_year": 2030,
    "overall fees": "$50,000"
}


student_2 = {
    "name": "Kate Smith",
    "age": 19,
    "nationality": "British",
    "visa": "Independent Visa",
    "major": "Business Administration",
    "GPA": 4.0,
    "expected_graduation_year": 2029,
    "overall fees": "$61,000"
}

print( "========== JOINT STUDENT INFORMATION REPORT ==========")
print(student_1["name"] + " and " + student_2["name"] + " " + "GENERATED REPORT")
print(student_1["name"] + " is studying " + student_1["major"] + " and " + student_2["name"] + " is studying " + student_2["major"])
print(student_1["name"] + " has a GPA of " + str(student_1["GPA"]) + " and " + student_2["name"] + " has a GPA of " + str(student_2["GPA"]))
print(student_1["name"] + " is expected to graduate in " + str(student_1["expected_graduation_year"]) + " and " + student_2["name"] + " is expected to graduate in " + str(student_2["expected_graduation_year"]))
print( "========== END OF GENERATED REPORT ==========")