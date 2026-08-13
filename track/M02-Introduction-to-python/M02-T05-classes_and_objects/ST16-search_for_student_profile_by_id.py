class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


class PlacementManager:
    def __init__(self):
        self.student_profiles = []

    def add_student_profile(self, student_profile):
        self.student_profiles.append(student_profile)

    def find_student_by_id(self, student_id):
        for profile in self.student_profiles:
            if profile.student_id == student_id:
                return profile
        return None


manager = PlacementManager()

n = int(input())

for _ in range(n):
    student_id = int(input())
    name = input().strip()
    course = input().strip()

    profile = StudentProfile(student_id, name, course)
    manager.add_student_profile(profile)

search_id = int(input())
found_student = manager.find_student_by_id(search_id)

if found_student:
    print(found_student)
else:
    print(f"Student profile with ID {search_id} not found")