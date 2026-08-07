word = input()
first = int(input())
second = int(input())
third = int(input())

numbers = [first, second, third]
record = (first, second, third)

middle_word = word[1:-1]
first_two = numbers[:2]
reversed_record = record[::-1]

print(f"Middle: {middle_word}")
print(f"First Two: {first_two}")
print(f"Reversed Tuple: {reversed_record}")