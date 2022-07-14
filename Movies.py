import csv

movies = [
    {'name': 'Evil Dead 2', 'director': 'Sam Raimi', 'year': '1985'},
    {'name': 'Army of Darkness', 'director': 'Sam Raimi', 'year': '1992'}
]


def write_to_file(output):
    with open('file.csv', 'w') as f:
        writer = csv.writer(f)
        f.write("name,director\n")
        writer.writerows([elem.values() for elem in output])


def read_from_file():
    with open('file.csv', 'r') as f:
        file_content = f.readlines()
        for line in file_content[1:]:
            info = line.strip().split(',')
            print(f'Movie: {info[0]} directed by {info[1]}.')

write_to_file(movies)
read_from_file()