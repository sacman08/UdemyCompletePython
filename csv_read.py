file = open('csv_data.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]

for line in lines:
    line_data = line.split(',')
    name = line_data[0].title()
    age = line_data[1]
    school = line_data[2].capitalize()
    degree = line_data[3].title()

    print(f"{name} is {age} years old, studying {degree} at {school}.")

sample_values = ','.join(['Thai', '19', 'Georgia Tech', 'Computer Science'])
print(sample_values)