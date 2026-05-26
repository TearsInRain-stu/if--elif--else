# The company is giving out gifts, with the following conditions:
# The employee must be an adult aged 18 or older and under 30.
# At the same time, the employee must have worked for the company for more than two years, OR have a level higher than 3 to claim the gift

age = input("Enter your age: ")
year_of_service = input("Enter your year of service: ")
level = input("Enter your level: ")

if int(age) < 18:

    if int(age) > 30:

        if int(year_of_service) > 2:
            print("Congrulate,you get the gift")
        elif int(level) > 3:
            print("Congrulate,you get the gift")
        else:
            print("Sorry,you do not get to the level")

    else:
        print("Your age cannot be more than 30")

else:
    print("Your age is less than 18")
