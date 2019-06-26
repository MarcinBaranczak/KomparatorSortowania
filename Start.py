import random


# Generating numbers for sorting
def data_set(count):
    tab_u = []  # unsorted tab

    for i in range(count):
        tab_u.append(random.randint(0, 1000))

    return tab_u


# Bubble
def bubble_sort(tab):
    for i in range(len(tab) - 1):
        for j in range(len(tab) - 1):
            if tab[j] > tab[j + 1]:
                temp = tab[j]
                tab[j] = tab[j + 1]
                tab[j + 1] = temp

    return tab


# TODO Insertion
def insertion_sort(tab):
    for j in range(1, len(tab)):
        for i in range(j):
            print("")


# Main
tab_unsort = data_set(10)
print(bubble_sort(tab_unsort))
