# Read five skill names into a list
skills = [input() for _ in range(5)]

# Convert the list into a tuple named skill_record
skill_record = tuple(skills)

# Create the required slices
first_three = skill_record[:3]
last_two = skill_record[-2:]
alternate_skills = skill_record[::2]
reversed_skills = skill_record[::-1]

# Display all required results matching the exact output format
print(f"Skill Record: {skill_record}")
print(f"First Three: {first_three}")
print(f"Last Two: {last_two}")
print(f"Alternate Skills: {alternate_skills}")
print(f"Reversed Skills: {reversed_skills}")