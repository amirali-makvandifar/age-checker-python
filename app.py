
birth_year = int(input("birth year: "))
password = input("password: ")
age = 2026 - birth_year
if age >=18 and password == "1234" :
    print("Access granted")
else:
    print("Access denied")
