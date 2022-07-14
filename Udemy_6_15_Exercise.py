# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:
import json

csv_file = open('csv_file.txt', 'r')
csv_lines = csv_file.readlines()

json_lines = []

for item in csv_lines:
    club, city, country = item.strip().split(',')
    json_data = {'club': club, 'city': city, 'country': country}
    json_lines.append(json_data)

csv_file.close()

json_file = open('json_file.txt', 'w')
json.dump(json_lines, json_file)
json_file.close()
