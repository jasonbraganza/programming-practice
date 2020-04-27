from actors import Wizard, Creature


def main():
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

    creatures = [
        Creature("Toad", 1),
        Creature("Tiger", 15),
        Creature("Bat", 3),
        Creature("Dragon", 50),
        Creature("Evil Wizard", 1000),
    ]
    hero = Wizard("Merlin", 75)

    while True:
        cmd = input("Do you [a]ttack, [r]un away or [l]ook around? ")
        if cmd == "a":
            print("AAAAKRAMAN!")
        elif cmd == "r":
            print("Run away! Run away if you want to survive!")
        elif cmd == "l":
            print("Well lookieee here")
        else:
            print("Ok exiting game")
            break


if __name__ == "__main__":
    main()
