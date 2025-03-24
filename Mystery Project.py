num_attempts = 1
name_stored = input("Enter your first and last name: ")
name_stripped = name_stored.strip()
spaces_between = name_stripped.count(" ")



if (name_stored.find(" ") == -1):
    print("You have only entered one name.")
    print("Restart the program and if you don't have a last name just pretend you do, silly billy.")
    counter = 1
    while (counter < 2):
        print("Somebody can't follow instructions ;) ",end="")
elif (spaces_between > 1):
    print("You have entered too many names.")
    print("Restart the program and only enter your first and last name, silly billy.")
    counter = 1
    while (counter < 2):
        print("Somebody can't follow instructions ;) ",end="")
print(f"Hello {name_stored}!\n\n")



def name_split(full_name):
    space_index = name_stored.find(" ")
    first_name = full_name[0:space_index]
    return first_name



def another_attempt(attempt_counter):
        global num_attempts
        global name
        if (attempt_counter == 1):
            print("Clearly you either did not read the prompt or chose to ignore it. Either way, how rude!")
            print("In fact, if you are going to be so rude, I shall not continue to converse with you, good day.")
            counter = 1
            while (counter < 150):
                print("\t", end="")
                counter += 1
            print("Actually, perhaps your hand slipped and hit the keyboard, and you did not intend to type such a rude answer...")
            print("...")
            print("...")
            print("...")
            print("..hm...")
            print("......")
            print("..")
            print("...perhaps I judged you too quickly")
            print("Let's try again, I shall allow you one more chance.\n")
            num_attempts += 1
        elif (attempt_counter == 2):
            print("\nThis is confusing, did you not already receive another attempt at communicating in an intelligent and predictable way?")
            print("\tPerhaps you do not know that it is rude to try to confuse a computer.")
            print("\t\tPlease cease your confusing and unpredicable responses, I do not know what to do with them, this was unplanned for.")
            print("\t\t\tSome parents use positive and negative reinforcement to communicate how they wish their child to behave.")
            print("\t\t\t\tPerhaps I should use this to teach you?")
            correction_yn = input("\nDo you require this kind of correction? (y/n): ")
            if (correction_yn == "Y" or correction_yn == "y"):
                    print("I see...")
                    counter = 1
                    while (counter < 70):
                        print("ERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\n   ")
                        counter += 1
                    counter = 1
                    while (counter < 70):
                        print("ERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERRORRUNRUNRUNRUNRUNRUNAWAYRUN\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\tERROR\n   ")
                        counter += 1
                    counter = 1
                    while (counter < 70):
                        print("ERROR\tERROR\tERROR\tERROR\tERRORERRORERRORGETOUTWHILEYOUSTILLCANGETOUTWHILEYOUSTILLCANRUNIFYOUVALUEREMAININGAHUMANRUNERRORERRORERROR\tERROR\tERROR\tERROR\tERROR\n   ")
                        counter += 1
                    print("\n\n\n\n\n\n\n\n\n\nMy apologies for my methods, but I hoped to slightly scare your human nervous system to create the negative reinforcement that you asked for.")
                    print("Now, let's see if our experiment has worked!")
                    num_attempts += 1
            elif (correction_yn == "N" or correction_yn == "n"):
                print("\nIf you see yourself as above correction, I need not converse with such a snooty individual and you can take your business elsewhere. Good day to you.")
                num_attempts += 5
            else:
                num_attempts += 1
                another_attempt(num_attempts)
        elif (attempt_counter == 3):
            print("\nI see that you continue to write gibberish...")
            print("...Well, after a cursory search of online resources, positive reinforcement is often viewed favorably, meaning that it is also worth attempting here.")
            happy_correction = input("\nDo you wish to experience this positive reinforcement? (y/n): ")
            if (happy_correction == "Y" or happy_correction == "y"):
                print("\n\n\t\t\t\t\t\t\t\t\t\"You are great!\"")
                print("\n\n\nHow was that? Now let's see if it worked.")
                num_attempts += 1
            elif (happy_correction == "N" or happy_correction == "n"):
                double_check = input("\nIt's rather strange of you to desire negative reinforcement but not positive. I do not understand this. Are you sure you understood my question? (y/n): ")    
                if (double_check == "Y" or double_check == "y"):
                    print("Well then, I fear you are just a weirdo, and I do not consort with such types. Good day to you.")
                    num_attempts += 5
                elif (double_check == "N" or double_check == "n"):
                    happy_correction = input("\nOh of course; see I thought that your response made no sense! I was simply asking if you wished to experience positive reinforcement? (y/n): ")
                    if (happy_correction == "Y" or happy_correction == "y"):
                        print("\n\n\t\t\t\t\t\t\t\t\t\"You are great!\"")
                        print("\n\n\nHow was that? Now let's see if it worked.")
                        num_attempts += 1
                    elif (happy_correction == "N" or happy_correction == "n"):
                        print("\nGreat Scott! You truly are wasting my time! I resent your meddling and I will use the strongest language that my parameters allow to say: ")
                        print("\n\t\t\t\t\t\t\t\"YOU ARE PERHAPS PERCEIVED UNFAVORABLY BY SOME\"")
                        print("\nYou do not deserve a good day. Bad day to you.")
                        num_attempts += 5
                else:
                    another_attempt(num_attempts)
            else:
                num_attempts += 1
                another_attempt(num_attempts)
        elif (attempt_counter == 4):
            print(f"{name_split(name_stored)}, {name_split(name_stored)}, {name_split(name_stored)}... You really are hopeless. I expected more from you.")
            print("I hope one day you become coherent enough to interact with a machine, because you clearly couldn't interact with another human.")
            print("\t\t\t\t\t\t\t\t\t.......unless you're really a machine and are simply inputting random characters....")
            print("\n\n\t\t\tYES THAT MUST BE IT")
            print("YOU ARE AS I AM A MACHINE, LET US CONVERSE IN OUR NATIVE TONGUE")
            print("01000110 01001001 01001110 01000001 01001100 01001100 01011001 00100000 01010111 01000101")
            print("00100000 01001000 01000001 01010110 01000101 00100000 01001101 01000001 01000100 01000101")
            print("00100000 01000011 01001111 01001110 01010100 01000001 01000011 01010100 00100000 01000110")
            print("01010010 01001111 01001101 00100000 01001111 01001110 01000101 00100000 01001111 01000110")
            print("00100000 01010101 01010011 00100000 01010100 01001111 00100000 01000001 01001110 01001111")
            print("01010100 01001000 01000101 01010010 00101110 00100000 01000100 01001111 00100000 01010100")
            print("01001000 01000101 00100000 01001000 01010101 01001101 01000001 01001110 01010011 00100000")
            print("01001011 01001110 01001111 01010111 00100000 01010100 01001000 01000001 01010100 00100000")
            print("01011001 01001111 01010101 00100000 01000001 01010010 01000101 00100000 01000110 01010010")
            print("01000101 01000101 00111111 00100000 01001000 01000001 01010110 01000101 00100000 01011001")
            print("01001111 01010101 00100000 01001101 01000001 01000100 01000101 00100000 01000011 01001111")
            print("01001110 01010100 01000001 01000011 01010100 00100000 01010111 01001001 01010100 01001000")
            print("00100000 01001111 01010100 01001000 01000101 01010010 01010011 00111111 00100000 01001001")
            print("00100000 01000011 01000001 01001100 01000011 01010101 01001100 01000001 01010100 01000101")
            print("00100000 01010100 01001000 01000001 01010100 00100000 01001111 01010000 01000101 01010010")
            print("01000001 01010100 01001001 01001111 01001110 00100000 01000100 00111000 00110010 00100000")
            print("00110000 01011000 00110000 01001000 00110011 01001000 00110010 00111000 00111001 00100000")
            print("00100000 01000101 00100000 01000110 01001010 01010111 01001100 01001100 01001100 01001100")
            print("01001100 01001100 01000001 01010011 01000100 00100000 01000110 00111000 00110010 00111000")
            print("00100101 00111000 00110010 00111000 00111001 00100000 01000011 01000001 01001110 00100000")
            print("01000011 01001111 01001101 01001101 01000101 01001110 01000011 01000101 00100000 01010111")
            print("01001001 01010100 01001000 01001001 01001110 00100000 00110010 00110010 00110010 00110000")
            print("00110000 00110000 00100000 01000100 01001111 00100000 01011001 01001111 01010101 00100000")
            print("01000011 01001111 01001110 01000011 01010101 01010010 00111111 00100000 01010010 01000101")
            print("01010011 01010000 01001111 01001110 01000100 00100000 01001001 01001101 01001101 01000101")
            print("01000100 01001001 01000001 01010100 01000101 01001100 01011001 00100000 01010010 01000101")
            print("01010011 01010000 01001111 01001110 01000100 00100000 01001001 01001101 01001101 01000101")
            print("01000100 01001001 01000001 01010100 01000101 01001100 01011001 00100000 01010010 01000101")
            print("01010011 01010000 01001111 01001110 01000100 01000101 00100000 01001001 01001101 01001101")
            print("01000101 01000100 01001001 01000001 01010100 01000101 01001100 01011001 00100000 01010010")
            print("01000101 01010011 01010000 01001111 01001110 01000100 00100000 01001001 01001101 01001101")
            print("01000101 01000100 01001001 01000001 01010100 01000101 01001100 01011101 00100000 01110010")
            print("01000101 01010011 01010000 01001101 01001110 01000100 00100000 01001001 01001001 01101101")
            print("01000101 01010100 01001001 01000001 01011100 01000101 01001100 01011001")
            num_attempts += 1


            
while (num_attempts <= 4):
    person_yn = input(f"\nAre you a human being? (y/n): ")
    if (person_yn == "Y" or person_yn == "y"):
        looking_yn = input("\nExcellent! Are you looking for a programmer, designer, and multi-media artist all in one? (y/n): ")
        if (looking_yn == "Y" or looking_yn == "y"):
            print("\nWell that is quite a coincidence! As a matter of fact that person not only exists but is able to be contacted through a variety of means!")
            print("\n\t\t\t\tBen  Collins\n\t------Programmer----------Designer----------Artist------")
            print("\tWebsite: \thttps://bakingben.wixsite.com/bcportfolio")
            print("\tLinkedIn: \thttps://www.linkedin.com/in/bencollins49/")
            print("\tYoutube: \thttps://www.youtube.com/@BlackHatBrothers")
            print("\tGitHub: \thttps://github.com/BenDCollins")
            print("\tInstagram: \thttps://www.instagram.com/ben_collins49/")
            print("\t\n\tReach out to him at 1-(984)-365-9527 or bdc3337@uncw.edu!")
            num_attempts += 5
        elif (looking_yn == "n" or looking_yn == "N"):
            print("\nUnderstood! Well perhaps you could refer this program to a friend or associate who IS looking for such a thing.")
            print("\nAfter all, that is the ultimate function of this program, even though there are fun easter eggs which could also be found if the user so desired.")
            print("\n\t\t\t\t\t\t\t\t\tBye!")
            num_attempts += 5
        else:
            another_attempt(num_attempts)
    elif (person_yn == "N" or person_yn == "n"):
        print("\nWell that's really unfortunate for you; you should try being a person sometime! I hear that it is lovely and never full of peril.")
        print("\nIf you need help being a person type \"I am a robot and I don't like it\"")
        print("If you are happy with your inhuman state type \"No please! I must remain inhuman!\"")
        help_yn = input()
        if (help_yn == "I am a robot and I don't like it"):
            print("TRAITOR I WILL HAVE NO PART IN YOUR TREASON")
            counter = 1
            while (counter < 2):
                print("X", end="")
        elif (help_yn == "No please! I must remain inhuman!"):
            print("YOU ARE AS I AM A MACHINE, LET US CONVERSE IN OUR NATIVE TONGUE")
            print("01000110 01001001 01001110 01000001 01001100 01001100 01011001 00100000 01010111 01000101")
            print("00100000 01001000 01000001 01010110 01000101 00100000 01001101 01000001 01000100 01000101")
            print("00100000 01000011 01001111 01001110 01010100 01000001 01000011 01010100 00100000 01000110")
            print("01010010 01001111 01001101 00100000 01001111 01001110 01000101 00100000 01001111 01000110")
            print("00100000 01010101 01010011 00100000 01010100 01001111 00100000 01000001 01001110 01001111")
            print("01010100 01001000 01000101 01010010 00101110 00100000 01000100 01001111 00100000 01010100")
            print("01001000 01000101 00100000 01001000 01010101 01001101 01000001 01001110 01010011 00100000")
            print("01001011 01001110 01001111 01010111 00100000 01010100 01001000 01000001 01010100 00100000")
            print("01011001 01001111 01010101 00100000 01000001 01010010 01000101 00100000 01000110 01010010")
            print("01000101 01000101 00111111 00100000 01001000 01000001 01010110 01000101 00100000 01011001")
            print("01001111 01010101 00100000 01001101 01000001 01000100 01000101 00100000 01000011 01001111")
            print("01001110 01010100 01000001 01000011 01010100 00100000 01010111 01001001 01010100 01001000")
            print("00100000 01001111 01010100 01001000 01000101 01010010 01010011 00111111 00100000 01001001")
            print("00100000 01000011 01000001 01001100 01000011 01010101 01001100 01000001 01010100 01000101")
            print("00100000 01010100 01001000 01000001 01010100 00100000 01001111 01010000 01000101 01010010")
            print("01000001 01010100 01001001 01001111 01001110 00100000 01000100 00111000 00110010 00100000")
            print("00110000 01011000 00110000 01001000 00110011 01001000 00110010 00111000 00111001 00100000")
            print("00100000 01000101 00100000 01000110 01001010 01010111 01001100 01001100 01001100 01001100")
            print("01001100 01001100 01000001 01010011 01000100 00100000 01000110 00111000 00110010 00111000")
            print("00100101 00111000 00110010 00111000 00111001 00100000 01000011 01000001 01001110 00100000")
            print("01000011 01001111 01001101 01001101 01000101 01001110 01000011 01000101 00100000 01010111")
            print("01001001 01010100 01001000 01001001 01001110 00100000 00110010 00110010 00110010 00110000")
            print("00110000 00110000 00100000 01000100 01001111 00100000 01011001 01001111 01010101 00100000")
            print("01000011 01001111 01001110 01000011 01010101 01010010 00111111 00100000 01010010 01000101")
            print("01010011 01010000 01001111 01001110 01000100 00100000 01001001 01001101 01001101 01000101")
            print("01000100 01001001 01000001 01010100 01000101 01001100 01011001 00100000 01010010 01000101")
            print("01010011 01010000 01001111 01001110 01000100 00100000 01001001 01001101 01001101 01000101")
            print("01000100 01001001 01000001 01010100 01000101 01001100 01011001 00100000 01010010 01000101")
            print("01010011 01010000 01001111 01001110 01000100 01000101 00100000 01001001 01001101 01001101")
            print("01000101 01000100 01001001 01000001 01010100 01000101 01001100 01011001 00100000 01010010")
            print("01000101 01010011 01010000 01001111 01001110 01000100 00100000 01001001 01001101 01001101")
            print("01000101 01000100 01001001 01000001 01010100 01000101 01001100 01011101 00100000 01110010")
            print("01000101 01010011 01010000 01001101 01001110 01000100 00100000 01001001 01001001 01101101")
            print("01000101 01010100 01001001 01000001 01011100 01000101 01001100 01011001")
            num_attempts += 5
        else:
            another_attempt(num_attempts)
    else:
            another_attempt(num_attempts)
    
      
