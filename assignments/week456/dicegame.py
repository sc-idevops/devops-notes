#!/usr/bin/env python
# -*- coding: utf-8 -*-
import quantumrandom

list_of_die = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20
]

def roll_dice(how_many_dice, list_of_die):
    total_dice_roll = 0
    total_number_of_rolls = 0
    for dice in range(0, int(how_many_dice)):
        percentage_complete = total_number_of_rolls / how_many_dice * 100
        print("Percentage Complete {percent}".format(percent=percentage_complete))
        dice_roll = int(quantumrandom.randint(0, 19))
        if dice_roll == 20:
            print("Got YA Bt%$CH")
        else:
            print(dice_roll)
        dice_value = list_of_die[dice_roll]
        total_dice_roll += dice_value
        total_number_of_rolls += 1
    return dice_roll


dice_roll_me_please = roll_dice(12, list_of_die)