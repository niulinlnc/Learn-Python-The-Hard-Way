from sys import exit
from random import randint

def death():
    quips = ["You died. You kinda suck at this.",
            "Nice job,you died...jackass.",
            "Such a luser.",
            "I have a small puppy that's better at this."]
    print quips[randint(0,len(quips)-1)]
    exit(1)

def central_corridor():
    print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
    print "Your entire crew. You are the last surviving menber and your last"
    print "mission is to get the neutron destruct bomb from the Weapons Armory,"
    print "put it in the bridge,and blow the ship up after getting into an"
    print "escape pod."
    print "\n"
    print "You're running down the central corridor to the Weapons Armory when"
    print "a Gothon jumps out,red scaly skin, dark grimy teeth, and evil clown costume" 
    print "flowing around his hate filled body.He's blocking the door to the"
    print "Armory and about to pull a weapon to blast you."

    action = raw_input(">")

    if action == "shoot!":
        print "Quick on the draw you yank out your blaster and fire it at the Gothon."
        print "His clown costume is flowing and moving around his body, which throws"
        print "Off your aim. Your laser hits his costume but misses him entirely. This"
        print "completely ruins his brand new costume his mother bought him,which"
        print "makes him fly into an inscane rage and blast you repeatedly in the face until"
        print "you are dead. Then he eats you."
        return 'death'

    elif action == "dodge!":
        print "Like a world class boxer you dodge, weave,slip and slide right"
        print "as the Gothon"
        return 'death'

    elif action == "tell a joke":
        print "Lucky for you the made you "

    else:
        print "ddd"
        return 'central_corridor'

def laser_weapon_armory():
    print "You do a dive"
    



