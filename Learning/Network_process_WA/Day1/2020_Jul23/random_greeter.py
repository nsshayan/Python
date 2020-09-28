#!/usr/bin/env python


def greet_user(username):
    print(f"Welcome to Python {username}!")

def greet_time(time):
    try:
        hours, minutes, seconds = (int(x) for x in time.split(":"))
        if hours >= 4 and hours < 12:
            print("Good morning!")
        elif hours >= 12 and hours < 18:
            print("Good afternoon!")
        elif hours >= 18 and hours <= 23:
            print("Good evening!")
        elif hours > 0 and  hours < 4:
            print("Nighty night!")
    except:
        print("That doesn't look like time to me!")


def greet_place(place):
    print(f"Wow! {place.capitalize()} would be a nice place!")

def greet_pythonista(age_str):

    try:
        age = int(age_str)

        if age < 0:
            print("Hello ? Are you awake ?")
        elif age >=0 and age < 3:
            print("Hello Young Pythonista!")
        elif age >= 3 and age < 7:
            print("Ah! A seasoned Pythonista, I presume.")
        elif age >= 7 and age < 27:
            print("(bows down) Hail Python Guru!")
        else:
            print("Seriously ??? You meant even before Guido Van Rossum created Python ?")
    except:
        print(f"That doesn't look like a number to me!")

prompts = {
    "What is your name ? ": greet_user,
    "What time is it right now ? ": greet_time,
    "Where do you live ? ": greet_place,
    "Since how long (in years) have you used Python ? ": greet_pythonista,
}

if __name__ == '__main__':
    from random import choice, random
    from time import sleep

    while True:
        prompt, fn = choice(list(prompts.items()))
        reply = input(prompt)
        sleep(random())
        fn(reply)

