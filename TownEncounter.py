__author__ = 'mroot'


import sys, os, math, random, string

os.system('cls' if os.name == 'nt' else 'clear')

while(1):

    terrain = int(raw_input("What terrain are you on?\n"
                      "  1: Safe Town\n"
                      "  2: Neutral Town\n"
                      "  3: Dangerous Town\n"
                      "  4: Safe Road\n"
                      "  5: Neutral Road\n"
                      "  6: Dangerous Road\n"
                      "  7: Neutral Waters\n"
                      "  8: Dangerous Waters\n"))

    roll = random.randrange(1,21,1)
    roll2 = -1

    print "Roll was: "+str(roll)

    if roll == 1:
        roll2 = random.randrange(1,21,1)
        print "Roll was 1, crit fail, rolling 2nd dice: "+str(roll2)
    elif roll == 20:
        roll2 = random.randrange(1,21,1)
        print "Roll was 20, crit hit, rolling 2nd dice: "+str(roll2)

    print str(roll)+" "+str(roll2)

    # Safe Road
    if terrain == 1:
        if roll == 20:
            if roll2 == 20:
                print "Crit 20 and crit 20 on rolls! A Miracle Happens!"
            else:
                print "Crit 20, there is a positive encounter with a friendly NPC"
        elif roll == 19:
            print "Random encounter with a friendly NPC"
        elif roll == 18:
            print "Stupid positive plot hook"
        elif roll == 2:
            print "Stupid neutral plot hook"
        elif roll == 1:
            print "Random Hostile encounter, re-roll doesn't matter"
        else:
            print "nothing interesting happens"

    elif terrain == 2:
        if roll == 20:
            if roll2 == 20:
                print "Crit 20 and crit 20 on rolls! Positive encounter with a friendly NPC!"
            else:
                print "Crit 20, there is a random encounter with a friendly NPC"
        elif roll == 19:
            print "Stupid positive plot hook"
        elif roll == 4:
            print "Stupid negative plot hook"
        elif roll == 3:
            print "Negative encounter with a friendly NPC"
        elif roll == 2:
            print "Negative encounter with a neutral/hostile NPC"
        elif roll == 1:
            if roll2 == 1:
                print "Crit fail and Crit fail on rolls! A Hostile plot hook happens!"
            else:
                print "Random Hostile Encounter"


    elif terrain == 3:
        print ""



    cont = raw_input("Enter 's' to exit program, anything else to enter new terrain\n")
    if cont == 's':
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
