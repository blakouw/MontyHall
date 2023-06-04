"""Monty Hall Projekt"""
import random
from typing import Optional

from matplotlib.style import use

DOOR = """
+------+
|      |
|   {}  |
|      |
|      |
|      |
+------+"""
GOAT = """
+------+
|  ((  |
|  oo  |
| /_/|_|
|    | |
|GOAT|||
+------+"""
CAR = """
+------+
| CAR! |
|    __|
|  _/  |
| /_ __|
|   O  |
+------+"""

door_state = [False, False, False]
choices = [1, 2, 3]
car = random.choice(choices)


def print_door(is_open, car) -> None:
    doors = []
    lines = []
    for i in range(3):
        if is_open[i] == 0:
            doors.append(DOOR.format(i + 1).split("\n"))
        elif i == (car - 1):
            doors.append(CAR.split("\n"))
        else:
            doors.append(GOAT.split("\n"))
    for each in zip(doors[0], doors[1], doors[2]):
        lines.append(" ".join(each))
    for line in lines:
        print(line)


print_door(door_state, car)


def get_user_input() -> Optional[int]:
    read_input = True
    user_decision = None
    while read_input:
        user_input = input("Podaj numer bramki 1-3: ")
        if user_input == "q":
            read_input = False
        else:
            try:
                user_decision = int(user_input)
                if 3 >= user_decision >= 1:
                    read_input = False
                else:
                    print("Błąd! Musisz wybrać z zakresu 1-3!")
            except (ValueError, TypeError):
                print("Błąd! Podaj numer bramki 1-3 lub 'q' by wyjsc.")
    return user_decision


print(car)


def monty_interaction(user_choice):
    temp_set = choices
    win = True
    if user_choice == car:
        monty_decision = random.choice([x for x in temp_set if x != car])
        door_state[temp_set.index(monty_decision)] = True
        print(f"Monty wybiera drzwi numer: {monty_decision}")
        print_door(door_state, car)
        switch = input("Chcesz zmienić hehehe drzwi? wybierz miedzy ""t"" a ""n"": ")
        if switch == "n":
            door_state[temp_set.index(user_choice)] = True
            print_door(door_state, car)
            print("Brawo! Wygrałeś samochód!")
            win = True

        elif switch == "t":
            ess = random.choice([x for x in temp_set if x == user_choice])
            door_state[temp_set.index(ess)] = True
            print_door(door_state, car)
            print("Przegrałeś! Samochód był w pierwotnych drzwiach!")
            win = False
        else:
            print("Musisz wybrac jedynie między ""t"" a ""n"" !")
    else:
        monty_decision = random.choice([x for x in temp_set if x != car and x != user_choice])
        door_state[temp_set.index(monty_decision)] = True
        print(f"Monty wybiera drzwi numer: {monty_decision}")
        print_door(door_state, car)
        switch = input("Chcesz zmienić drzwi? wybierz miedzy ""t"" a ""n"": ")
        if switch == "n":
            door_state[temp_set.index(user_choice)] = True
            print_door(door_state, car)
            print("Przegrales!")
            win = False

        elif switch == "t":
            ess = random.choice([x for x in temp_set if x != monty_decision and x != user_choice])
            door_state[temp_set.index(ess)] = True
            print_door(door_state, car)
            print("BRAWO!")
            win = True
        else:
            print("Musisz wybrac jedynie między ""t"" a ""n"" !")
    return win


monty_interaction(get_user_input())

"""
def main_loop(door_state, car):
    dec = True
    monty_interaction()
    del door_state, car
    while dec:
        is_fun = input("Gramy dalej? ""t"" lub ""n"": ")
        if is_fun =="t":
            door_state = [False, False, False]
            car=random.choice(choices)
            print(car)
            print_door(door_state,car)
            print(car)
            monty_interaction()
        else:
            break
main_loop(door_state, car)
"""