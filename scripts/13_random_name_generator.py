from random import choice


def random_name_generator(first, second, x):
    """
        Generates random names.
        Arguments:
         - list of first names
         - list of last names
         - number of random names
    """
    names = []
    for i in range(x):
        names.append("{0} {1}".format(choice(first), choice(second)))
    return set(names)


first_names = ["Drew", "Mike", "Landon", "Jeremy", "Tyler", "Tom", "Avery", "James", "Hunter", "Ethan", "Bryan", "Jeff", "Ryan", "Luke", "Brad", "Jennifer", "Lola", "Isadora"]
last_names = ["Smith", "Jones", "Brighton", "Taylor", "Green", "Brown", "Scott", "Eggart", "Hunt", "Rhule"]


num = int(input("Number of names to generate: "))

names = random_name_generator(first_names, last_names, num)
print('\n'.join(names))
