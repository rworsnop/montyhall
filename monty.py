#!/usr/bin/env python
from random import randint

goats = 0
cars = 0;

while 1==1:
    prizes = ['goat', 'goat', 'car'];
    doors = [];
    # Populate
    for _ in range(3):
        prize_number = randint(0, len(prizes) - 1);
        prize = prizes[prize_number];
        doors.append(prizes[prize_number]);
        del prizes[prize_number];

    print "Doors: %s" % doors;

    print "Contestant chose door 1: %s" % doors[0];

    # Have the host choose a door with a goat behind, and have the contestant
    # choose the other one.
    if doors[1] == 'goat':
        host_door = 1;
        contestant_door = 2;
    else:
        host_door = 2;
        contestant_door = 1;

    print "Host chose door %i" % (host_door + 1);

    prize = doors[contestant_door];
    print "Contestant chose door %i, winning a %s" % (contestant_door + 1, prize)

    if (prize == 'car'):
        cars += 1;
    else:
        goats += 1;

    print "Score so far: Goats: %i Cars: %i" % (goats, cars)

    raw_input("Another? Hit ENTER")
