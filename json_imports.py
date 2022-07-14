import json

file = open('friends_json.txt', 'r')
file_contents = json.load(file)
file.close()

print(file_contents['friends'][:])

cars = [
    {'make': 'BMW', 'model': '325i'},
    {'make': 'Saturn', 'model': 'Ion'},
    {'make': 'Ford', 'model': 'Ranger'}
]

file = open('cars_json.txt', 'w')
json.dump(cars, file)
file.close()

my_json_string = f'[{file_contents}]'
# can use dict, list or strings, no tupels


incorrect_car = json.loads(my_json_string)
print(incorrect_car)


