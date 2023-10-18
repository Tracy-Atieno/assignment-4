def calculate_grade(maths, physics, geo, chem):
    if any(mark < 0 or mark > 100 for mark in (maths, physics, geo, chem)):
        return 'Unrecognized marks/avg'

    average = (maths + physics + geo + chem) / 4

    if 0 <= average <= 30:
        return 'D'
    elif 31 <= average <= 50:
        return 'C'
    elif 51 <= average <= 70:
        return 'B'
    elif 71 <= average <= 100:
        return 'A'


# Get input from the user for four subjects: maths, physics, geo, and chem
maths = int(input('Enter the marks for Math: '))
if maths < 0 or maths > 100:
    print('Marks must be between 0 and 100. Please correct the value for Math.')
    exit()

physics = int(input('Enter the marks for Physics: '))
if physics < 0 or physics > 100:
    print('Marks must be between 0 and 100. Please correct the value for Physics.')
    exit()

geo = int(input('Enter the marks for Geography: '))
if geo < 0 or geo > 100:
    print('Marks must be between 0 and 100. Please correct the value for Geography.')
    exit()

chem = int(input('Enter the marks for Chemistry: '))
if chem < 0 or chem > 100:
    print('Marks must be between 0 and 100. Please correct the value for Chemistry.')
    exit()

# Calculate the grade based on the entered marks
grade = calculate_grade(maths, physics, geo, chem)

# Display the result
print(f'Grade: {grade}')
