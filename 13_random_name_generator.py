from random import randint


def random_name_generator(first, second, x):
    """
        Generates random names.
        Arguments:
         - list of first names
         - list of last names
         - number of random names
    """
    names = []
    for i in range(0, int(x)):
        random_first = randint(0, len(first)-1)
        random_last = randint(0, len(second)-1)
        names.append("{0} {1}".format(
            first[random_first],
            second[random_last])
        )
    return set(names)


first_names = ["Drew", "Mike", "Landon", "Jeremy", "Tyler", "Tom", "Avery"]
last_names = ["Smith", "Jones", "Brighton", "Taylor"]
names = random_name_generator(first_names, last_names, 5)
print('\n'.join(names))
