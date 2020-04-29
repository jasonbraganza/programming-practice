import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"I am a {self.name} with level, {self.level}"

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    # def __init__(self, name, level):
    #     super().__init__(name, level)
    #     self.name = name
    #     self.level = level

    def __repr__(self):
        return f"I am a {self.name} with level, {self.level}"

    def attack(self, creature):
        print()
        print(f"{self.name} attacks the {creature.name}")
        player_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()
        print(
            f"{self.name} rolled {player_roll}, while the {creature.name} rolled {creature_roll}"
        )
        if player_roll >= creature_roll:
            print(
                f"The brave wizard {self.name} has mightily triumphed over the {creature.name}"
            )
            print()
            return True
        else:
            print(
                f"""It’s a sad day for humanity!
The brave wizard {self.name} been defeated!"""
            )
            print()
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breathes_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breathes_fire = breathes_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breathes_fire else base_roll
        scale_modifier = self.scaliness / 10
        return base_roll * fire_modifier * scale_modifier
