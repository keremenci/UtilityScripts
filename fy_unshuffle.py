"""
    Python script for shuffling strings to be unshuffled using fisher-yates in a c program

    Author: Keremenci
"""


def shuffle(the_list, randnums):
    """
        Algorithm to shuffle a given string.

        - :param the_list: list to be shuffled.
        - :param randnums: list of numbers generated in c from a spesific seed.
            Simply generate 100 numbers using srand() and rand() and calculate second index of the swap as (j % 100) % (i + 1).
        - :returns: the shuffled list.
    """
    length = len(the_list)
    iterator = iter(randnums)
    swaps = []

    # Record swaps
    for i in range(length-1):
        rand = next(iterator)
        j = rand % (i+1)
        indices = [i, j]
        swaps.append(indices)

    # Perform the swaps backwards
    for swap in swaps[::-1]:
        the_list[swap[0]], the_list[swap[1]
                                    ] = the_list[swap[1]], the_list[swap[0]]
    return the_list


def main():
    randnums = [17, 31, 27, 27, 41, 22, 93, 66, 90, 73, 3, 88, 56, 80, 20, 14, 18, 44, 27, 25, 32, 2, 95, 25, 4, 26, 98, 20, 24, 53, 44, 41, 84, 23, 20, 77, 46, 13, 96, 36, 38, 99, 24, 47, 79, 96, 13, 49, 40,
                40, 26, 24, 42, 74, 2, 98, 0, 0, 19, 24, 53, 15, 18, 89, 38, 38, 66, 36, 52, 62, 24, 42, 14, 0, 89, 93, 96, 2, 95, 36, 42, 73, 13, 37, 47, 15, 87, 48, 67, 6, 24, 20, 73, 42, 61, 12, 33, 79, 48, 37, ]
    text = "Taxation is theft"
    print(repr("".join(shuffle(list(text), randnums))))


if __name__ == "__main__":
    main()
