import time
# Question Function
def askuser(question):
    answer = input(question+' ')
    return answer

# Colors function
def colorgame():
    color = askuser("I'm going to rate colors, name a color.").lower()
    print('Loading', end=' ')
    time.sleep(0.5)
    print('.', end=' ')
    time.sleep(0.5)
    print('.', end=' ')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    if color == 'blue':
        print('8/10')
    elif color == 'orange':
        print('5/10')
    elif color == 'white':
        print('3/10')
    elif color == 'purple':
        print('5/10')
    elif color == 'red':
        print('8/10')
    elif color == 'green':
        print('10/10')
    elif color == 'purple':
        print('5/10')
    elif color == 'yellow':
        print('2/10')
    elif color == 'black':
        print('Not much of a color...')
    elif color == 'teal':
        print('6/10')
    elif color == 'lavender':
        print("That's basically just purple.")
    elif color == 'turquoise':
        print("3/10")
    elif color == 'magenta':
        print("7/10")
    elif color == 'cyan':
        print("8/10")
    elif color == 'brown':
        print("Definetly 1/10 ")
    else:
        print('What the heck is that?')

# Ask the user for their name
name = askuser('What is your name?')
print('Hello '+ name)


firsttime = True


# While loop
while True:
    if firsttime:
        game = askuser('Do you want to play a game?')
    else:
        game = askuser('Do you want to play again?')
    if game.lower() == 'no':
        print('Fine, be that way ' + name + ", you're no fun anyway.")
        quit()


    print('Awesome!')

    # Running the Color game function again
    colorgame()

    firsttime = False

