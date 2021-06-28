from pathlib import Path

file_path=Path("pi_million_digits.txt")
with open(file_path) as file_object:
    lines=file_object.readlines()
pi_string=""
for line in lines:
    pi_string+=line.strip()

birthday=input("Enter your birthday in the form ddmmyy: ")
if birthday in pi_string:
    print("Your birthdayappears in the first million digits of pi!")
else:
    print("Can't find your birthday :C")