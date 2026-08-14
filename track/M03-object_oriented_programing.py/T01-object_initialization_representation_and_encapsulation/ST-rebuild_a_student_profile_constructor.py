class StudentProfile:
    def __init__(self, student_id, name, course, experience, skills):
        # Store all five values as instance attributes
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience
        self.skills = skills

# Read inputs
student_id = int(input().strip())
name = input().strip()
course = input().strip()
experience = int(input().strip())
skills = input().strip().split()

# Create one StudentProfile object
student = StudentProfile(student_id, name, course, experience, skills)

# Print the data stored in the object
print(f"Student ID: {student.student_id}")
print(f"Name: {student.name}")
print(f"Course: {student.course}")
print(f"Experience in Years: {student.experience}")
print(f"Skills: {', '.join(student.skills)}")