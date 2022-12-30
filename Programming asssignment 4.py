
# Name: Aayusha Kattel                Date Assigned:Nov 1, 2022

# Course: 2000-Sec 44306              Due Date: Nov 8, 2022

# File name: Programming assignment 4.py

# Program Description: > display the purpose of the program
#                      > take the race and class as integers from the user
#                      > determines the name as per the race and class choosed by the user
#                      > links with c.txt file where names are searched and printed in the program
#                      > prints the name in the program if the sequence is matched else prints "No name found"
#                      




unequalSigns = "><" * 23           ## formatting the program

def displayInstructions():         ## defining function displayInstruction to write the initial part of the program including the greeting and purpose of the program
    print("Names, Race, Classes taken from: ")
    print(
          "  https://raw.githubusercontent.com/janelleshane/DnD-characters/master/DnD_characters_May2018.txt"
    )

    
    print("\n"+unequalSigns)
    print("\n><><><><><><><><><><><><><><\n")
    print("___ ___ ___ ___ ___ ___ ___ ___ ___")
    print("|         Welcome!         |")
    print("\n><><><><><><><><><><><><><><\n")
    print("| This name generator will |")
    print("|   you name suggestions   |")
    print("|  based on a character's  |") 
    print("|      RACE and CLASS      |")
    print("\n><><><><><><><><><><><><><><\n")
   


print()


def displayRaceOptions():         ## defining a function "displayRaceOptions" to display the options of race ranging fron 1 to 9
    equalsToSign = "="*14
    print(equalsToSign)
    print(" Race Options")
    print(equalsToSign)
    print(
        "1. Human",
        "2. Elf",
        "3. Tiefling",
        "4. Gnome",
        "5. Gobline",
        "6. Dragonborn",
        "7. Halfling",
        "8. Orc",
        "9. Dwarf",
        sep="\n",
    )


print()


def displayClassOptions():       ## defining a function "displayClassOptions" to display the options of class ranging fron 1 to 9
    print()
    print()
    equalToSign = "="*15
    print(equalToSign)
    print(" Class Options")
    print(equalToSign)
    print(
        "1. Cleric",
        "2. Druid",
        "3. Wizard",
        "4. Paladin",
        "5. Bard",
        "6. Rogue",
        "7. Ranger",
        "8. Fighter",
        "9. Barbarian",
        sep="\n",
    )


def determineRace(raceNumber):       ## defining a function "raceNumber" to return a value of race as per the int given by the user
    race = ""
    if raceNumber == 1:              ## usinf if/else condition
        race = "Human"

    elif raceNumber == 2:
        race = "Elf"

    elif raceNumber == 3:
        race = "Tiefling"

    elif raceNumber == 4:
        race = "Gnome"

    elif raceNumber == 5:
        race = "Goblin"

    elif raceNumber == 6:
        race = "Dragonborn"

    elif raceNumber == 7:
        race = "Halfling"

    elif raceNumber == 8:
        race = "Orc"

    else:
        raceNumber == 9
        race = "Dwarf"

    return race





def determineClass(classNumber):         ## defining a function "classNumber" to return a value of class as per the int given by the user 
    className = ""
    if classNumber == 1:                 ## using if/else condition
        className = "Cleric"

    elif classNumber == 2:
        className = "Druid"

    elif classNumber == 3:
        className = "Wizard"

    elif classNumber == 4:
        className = "Paladin"

    elif classNumber == 5:
        className = "Bard"

    elif classNumber == 6:
        className = "Rogue"

    elif classNumber == 7:
        className = "Ranger"

    elif classNumber == 8:
        className = "Fighter"

    else:
        classNumber == 9
        className = "Barbarian"
    return className


def displayCharacters(race, className):             ## defining a function "displayCharacter(race, className)" which is used to list the names as per the race and the class
    isEqualTo = "="*24
    print()
    print(unequalSigns)
    print("\n\n"+isEqualTo)
    print(race + "/" + className + " Names")
    print(isEqualTo)
    infile = open("characters.txt", "r")                    ## using .txt document to read the data and match them with the condition as a loop 
    names = ""
    for line in infile:                            ## reding the .txt file
        line = line.rstrip()
        raceStart = line.find(",")
        raceEnd = line.rfind(",")
        raceFound = line[raceStart + 1 : raceEnd]
        classStart = line.rfind(",")
        classFound = line[classStart + 1 :]
        

   
       
        if race == raceFound and className == classFound:  ## using if/else condition for the sequence to match
            names+= line[ : line.find(",")] + "\n"
        
    if len(names) >0:                                      ## using if condition to determine if the none of the sequence matchs
        print(names)                                       ## printing the names
    else:
        print("-No names")                                 ## output if the condition doesnot match
                               
    print( "\n"+unequalSigns)
     
    

def main():                                                ## defining main function and calling all the function in programming sequence
    displayInstructions()                                  ## calling displayInstructions()  
    displayRaceOptions()                                   ## calling displayRaceOptions()
    raceChoice = int(input("\nEnter choice (1 - 9): "))    ## taking int as a race choice
    race = determineRace(raceChoice)                       ## storing race value
    

    displayClassOptions()                                  ## calling displayClassOptions()
    classChoice = int(input("\nEnter choice (1 - 9): "))   ## taking input as class choice
    className = determineClass(classChoice)                ##b storing className value
    
    
    
    displayCharacters(race, className)                     ## calling displayCharacters(race, className) 


main()

