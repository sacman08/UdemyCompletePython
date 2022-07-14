known_users = ['Jenna','Thai','Lindsey','Mckay']

while True:
    print('Hi, my name is Travis!')
    stranger = input("What is your name?").strip().capitalize()
    if stranger in known_users:
        print(f"Welcome {stranger}!")
        break
    else:
        print("Sorry, you're not a friend, stranger!")
