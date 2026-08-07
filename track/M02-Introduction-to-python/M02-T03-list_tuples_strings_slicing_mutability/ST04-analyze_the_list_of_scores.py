# Hardcoded inputs from Sample Input 1
n = 5
scores = [78, 92, 61, 84, 67]
search_score = 84

# Display the highest, lowest, and total scores
print(f"Highest Score: {max(scores)}")
print(f"Lowest Score: {min(scores)}")
print(f"Total Score: {sum(scores)}")

# Display whether search_score is present
if search_score in scores:
    print("Search Result: Found")
else:
    print("Search Result: Not Found")