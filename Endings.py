#Endings

def endings(index):
    match index:
        case 21:
            print("\n\tSingle-handedly Beat All Their Men\n\tYou manage to kill off the Imperials that were wrecking havok on the Academy. The one who hired you is pleased, but would have been happier if you'd gotten the children out before you started the fight. That's the whole reason they hired you, after all. You get a tidy sum, anyway. Your reputation doesn't suffer either.\n\n\
            \tPress Enter to close game")
            input()
            quit()
        case 23:
            print("\n\tDog. Just Dog.\n\tSome Professors got to help, but others didn't, because you didn't feel like going through all the classrooms. The one who hired you had mixed feelings. You did get some of the children out, but you didn't get them all out before facing off with the Imperials. The left out Professors are very sour towards you. Your reputation doesn't suffer, however, and you get a tidy sum.\n\n\
            \tPress Enter to close game")
            input()
            quit()
        case 24:
            print("\n\tA Big Man with an Old Soul\n\tYou and the Professors took no prisoners. Not only did you save all the children, you cleared out the school of the invading Imperials! Your reputation skyrockets and you get a nice bonus from the student's parents. You get to keep all the stuff you picked up, too. A satisfying ending to a job that was a little more complicated than you were expecting.\n\n\
            \tPress Enter to close game")
            input()
            quit()
        case 22:
            print("\n\tDid Your Job and Went Home With No Drama\n\tYou got all the children and professors out of the Academy. You did decide against facing off with the Imperials, though. Your reputation takes no hit as a whole, but the Professors that wanted to take on the Imperials don't think much of you. The Professors still took a 'scorched earth' approach, just leveing the building since there was no on the inside to take on the Imperials. You get a tidy sum.\n\n\
            \tPress Enter to close game")
            input()
            quit()
        case 25:
            print("\n\tHow Long Have You Worked as a Merc, Anyway.\n\tYou got some children and professors out of the Academy. You did decide against facing off with the Imperials, though. Your reputation takes a small hit and the Professors that wanted to take on the Imperials don't think much of you. Not to mention the Professors and the parents of the children you didn't bother to save. The Professors come up with a plan together while you get paid a portion of what you were offered, as you didn't finish the job completely. You're ushered off the grounds and will see a dip in work for a while.\n\n\
            \tPress Enter to close game")
            input()
            quit()
        case 6:
            print("\n\tThe Little Story of a Big Merc\n\tYou step back through the teleportation circle. How are you supposed to do this with no armor or weapons? Maybe they stayed in the circle you first stepped through? Alas, they haven't. The mage is apologizing profusely and is no longer able to even hold the circle. You failed before you even started! You're reputation takes a blow, your purse takes a blow, and your self-esteem takes a blow.\n\n\
            \tPress Enter to close game")
            input()
            quit()
        case _:
            print("Out of Bounds:endings")