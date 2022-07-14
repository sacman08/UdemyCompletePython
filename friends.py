# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to `nearby_friends.txt`

my_friends = input('Enter friend name:').split(',')

my_close_friends_data = open('data.txt', 'r')
my_close_friends = [line.strip() for line in my_close_friends_data.readlines()]
my_close_friends_data.close()

my_friends_set = set(my_friends)
my_close_friends_set = set(my_close_friends)

my_close_friends_inter = my_friends_set.intersection((my_close_friends_set))

my_close_friends_file = open('nearby_friends.txt', 'w')

for friend in my_close_friends_inter:
    print(f'{friend} is nearby!')
    my_close_friends_file.write(f'{friend}\n')

my_close_friends_file.close()



