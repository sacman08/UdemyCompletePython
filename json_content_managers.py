import json

with open('friends_json.txt', 'r') as file:
    file_contents = json.load(file)
    # with open is a auto keyword to open the file and close at the end auto instead of open/close commands.

print(file_contents['friends'][:])

cars = [
    {'make': 'BMW', 'model': '325i'},
    {'make': 'Saturn', 'model': 'Ion'},
    {'make': 'Ford', 'model': 'Ranger'}
]

with open('cars_json.txt', 'w') as file:
    json.dump(cars, file)

my_json_string = f'[{file_contents}]'
# can use dict, list or strings, no tupels


incorrect_car = json.loads(my_json_string)
print(incorrect_car)


