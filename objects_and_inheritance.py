#!/bin/env python
# -*- coding: utf-8 -*-

'''A phylogenetic hierarchy that would have made Linnaeus proud.'''


INCOMPATIBLE_SPECIES = (set(("human", "lion")),
                        set(("dog", "cat")),
                        set(("cat", "mouse")))


class Animal(object):

    """An animal from the planet Earth."""

    # This just shows that an implementing class should have these attributes.
    species = None
    bite_strength = 0
    resistance = 0

    def __repr__(self):
        return "{}('{}')".format(self.__class__.__name__, self.name)

    def __str__(self):
        description = ["Species: {}".format(self.__class__.__name__),
                       "Name: {}".format(self.name),
                       "Bite strength: {}".format(self.bite_strength),
                       "Resistance: {}".format(self.resistance)]
        return "\n".join(description)

    def __lt__(self, other):
        return self.bite_strength < other.bite_strength

    def __eq__(self, other):
        return self.bite_strength == other.bite_strength

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return self > other or self == other

    def __init__(self, name):
        """An Animal is born!"""
        self.name = name

    def introduce(self):
        """Tell the others why you're here."""
        print("My name is {} and I'm a {}.".format(self.name, self.species))

    def play(self, other):
        """Play with another Animal."""
        involved_species = set((self.species, other.species))
        for incompatible_set in INCOMPATIBLE_SPECIES:
            if involved_species == incompatible_set:
                print("I hate you! I hate you so much!")
            else:
                print("This was fun, let's do it again soon.")

    def bite(self, other):
        """You know that I could bite somebody, bite somebody like you."""
        print("{}, I'm biting you this hard: {}".format(other.name,
                                                        self.bite_strength))
        other.accept_bite(self.bite_strength)

    def accept_bite(self, bite_strength):
        """Get bitten."""
        actual_bite = bite_strength * self.resistance
        print("Ouch, that hurt this much: {}".format(actual_bite))


class Human(Animal):

    """An animal that can play with others."""

    species = "human"
    bite_strength = 2
    resistance = 2

    def play(self, other):
        """Play with another being. Overrides basic play behavior in Animal."""
        if other.species == "alien":
            print("I don't even know how to talk to you.")
        elif other.species not in ("lion", "hyena"):
            print("Oh, you're such a cute {}!".format(other.species))
        else:
            print("Help me, it's trying to eat me!! Hellllll---")

    def accept_bite(self, bite_strength):
        """React to being bitten."""
        if bite_strength < 4:
            print("That's it, no treat for you.")
        else:
            print("That was my favorite limb! :(")


class Lion(Animal):
    """A lion."""
    species = "lion"
    bite_strength = 9
    resistance = 8


class Dog(Animal):
    """A dog."""
    species = "dog"
    bite_strength = 5
    resistance = 3

class Cat(Animal):
    """A cat."""
    species = "cat"
    bite_strength = 2
    resistance = 4

class Mouse(Animal):
    """A mouse."""
    species = "mouse"
    bite_strength = 2
    resistance = 1


class Alien(object):

    """An alien."""

    def __repr__(self):
        return "Alien('{}')".format(self.name)

    def __str__(self):
        return "A mysterious - and dangerous Alien. What are his intentions?"

    def __init__(self):
        """I don't even know anything about this alien."""
        self.name = "SGOIWUZETÖLA"
        self.species = "alien"

    def introduce(self):
        """Say hi."""
        print("We come in peace.")

    def zap(self, other):
        """Zap somebody."""
        print("Alien fry ray zap! I just fried {}!".format(other.name))

    def accept_bite(self, bite_strength):
        """Get really pissed off."""
        print("Take me to your leader. I'll deal with your planet afterwards.")


def main():
    organism_list = [Dog("Fido"), Cat("Jerry"), Lion("Lambert"), Human("Joe"),
                     Alien()]
    for organism in organism_list:
        print(organism.__repr__())
        print(organism)
    dog = organism_list[0]
    cat = organism_list[1]
    lion = organism_list[2]
    human = organism_list[3]
    alien = organism_list[4]
    print("Dog > Cat? {}".format(dog > cat))
    print("Lion < Dog? {}".format(lion < dog))
    print("Cat >= Human? {}".format(cat >= human))


if __name__ == "__main__":
    main()
