# Small game, so that I learn the basics of object oriented programming and
# classes.

import random  # to randomly pick a monster
import time  # to give our hero time to recover

from actors import (
    Wizard,
    Creature,
    SmallAnimal,
    Dragon,
)  # all the characters in the game are defined there. getting them over here.


def main():
    """
    Kicks things off, as usual.
    Prints our header and runs the game
    """
    header_print()
    game_loop()


def header_print():
    """
    Prints the header for the program
    """
    print("================================")
    print("Welcome to the Wizard Battle App")
    print("================================")
    print()


def game_loop():
    """
    Gets creatures from the creature module
    Picks a random creature
    Asks the user, to pick an action.
    If the hero attacks, it rolls the dice and sees who wins.  
    If the hero looks around, it presents a list of creatures left.
    If the hero decides to run away, it justs brings up another creature

    """
    creatures = [
        SmallAnimal("Toad", 1),
        Creature("Tiger", 15),
        SmallAnimal("Bat", 3),
        Dragon("Big Dragon", 50, 75, True),
        Creature("Evil Wizard", 500),
    ]
    hero = Wizard("Merlin", 75)

    while True:

        active_creature = random.choice(creatures)
        print()
        print(
            f"A {active_creature.name}, of level {active_creature.level} appears from the dark, dank, forest!"
        )
        print()

        cmd = input(
            """Do you [a]ttack, [r]un away or [l]ook around? 
Else hit any other key to quit. """
        )
        if cmd == "a":
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("Our wizard needs to retreat and recover")
                time.sleep(5)
                print(
                    "Hurrah! Our brave one returns, rejuvenated in mind, body and spirit!"
                )
                print()

        elif cmd == "r":
            print()
            print(
                f"The wizard has become unsure of his power! Best to flee! Fly, {hero.name}! Fly!"
            )
            print()
        elif cmd == "l":
            print()
            print(f"Our Wizard {hero.name}, looks around and sees: ")
            for c in creatures:
                print(f"A {c.name} of level {c.level}")
            print()
        else:
            print("Ok exiting game")
            break

        if not creatures:
            print(
                f"""You, brave {hero.name} have defeated all the creatures!
You are a true hero!
Adieu! Until we meet again!

"""
            )
            break


if __name__ == "__main__":
    main()
