# Initialized Variables
HeroFunds = 0
HeroFunds = int(HeroFunds)
Weapon = "None"
Armour = "None"
Lore = 0
Lore = int(Lore)
Inventory = []

# Equipment Library
rusty_scabbard = "rusty scabbard"
tainted_watchman_tunic = "tainted watchman's tunic"


# Disposition initialization
ManDis = 5 # Guard at the docks (Androl Buck)
ManDis = int(ManDis)

MorDis = 3 # Registrar (Moradron Melka)
MorDis = int(MorDis)

# Reputation initialization
GateRep = 2 # Reputation within the organization of "The Gate"
GateRep = int(GateRep)
MarindonNobility = 0
MarindonNobility = int(MarindonNobility)

# Inventory functionality

def show_inventory():
    if Inventory:
        print("Your inventory contains:")
        for item in Inventory:
            print(f"-{item}")
    else: 
        print("Your inventory is empty.")

def add_to_inventory(item): 
    Inventory.append(item)
    print(f"A {item} has been added to your inventory.")

def remove_from_inventory(item):
    if item in Inventory:
        Inventory.remove(item)
        print(f"{item} has been removed from your inventory.")
    else:
        print(f"{item} is not in your inventory.")


# Intro

print("Welcome to the world of Kiedaria. Please enter some essentials in order to start your adventure!")
Name = input("Please enter your hero's name: ")
Gender = input("Select Gender(M/F/O): ").upper()

print(" *As you step off of the old Cog-style ship, the old boards that make up the docks of Marindon creak. More creaking can be heard nearby, as the bustling dock is filled with merchants, fishermen, and shady-looking characters.* ")
print()
print(" *Headed straight towards you is a tall, moustached man, bearing the sigil of 'The Gate' on his breastplate.*")
print()
print(" *The man looks from one boat to another, as he passes through the column of bobbing vessels.*")
print()

# Armoured Man Disposition Test 1

print(f" 'I assume that you're {Name}?'")
ManQ1 = input("Y/N: ").upper()

if ManQ1 == "Y".upper():
    print("-----------------------------------------------------")
    print("'Fantastic!'")
elif ManQ1 == "N".upper():
    print("-----------------------------------------------------")
    print("'Don't try to be smart with me, dog. I know who you are!'")
    print()
    ManDis = ManDis - 2
    print("______The armoured man has lost respect for you.______*")

print()
print(" 'Let's get you to the registrar's office.'")
if Gender == "M":
    print(f"'Follow me, Mr. {Name}!'")
elif Gender == "F":
    print(f"'Follow me, Ms. {Name}!'")
elif Gender == "O":
    print(f"'Follow me, {Name}!'")
print()

# Leg1 To the Registrar

print(" *The armoured man swivels around to the direction of the shoreline of Marindon: a coastal town with the charm of an old keepsake.*")
print()
print(" *As you stroll off the rickety warf and onto the cobblestone, the man leads you down the steps into a ditch of sorts that contains one small stone building with entrance pillars that'd make one dispute its stature.*")
print()

# Armoured Man Disposition Test 2

print("'The Captain tells me you're not registered within the reaches of Kiedaria. I find that confusing, but who am I to question these sorts of things.'")
ManQ2 = input("[]Choose an option: [(1)That's correct. Let's take care of that. (2)Yes, who are you? Perhaps I don't need to be registered.]: ")
print("-----------------------------------------------------")
if ManQ2 == "1":
    print("'You'll fit right in here, citizen. You'll find the office just inside that door.")
elif ManQ2 == "2":
    print(f"I'm already sick of you, {Name}. *He scowls as he brandishes a shortsword and pokes you in the back.* 'Go through that door, or you'll be calling for a mender that you don't have' ")
    print()
    ManDis = ManDis - 2
    print("______The armoured man has lost respect for you.______")

# Leg2 The Registrar

print()
print("*As you turn the fingerprint-ridden brass doorknob and step through, you enter a well-lit, minimally-furnished room. There is a man, seated behind a grand oak desk who stares up at you as he lays his smouldering pipe down on a steel rack on the desk.*")
print()
# Judgement 1
if ManQ2 == "2":
    print("'I witnessed all that trouble that you put Mr. Androl through. I'll not stand for any of that within these walls.'")
    print()
# Race Selection

print("*The man gives you a slight nod.* 'My name is Moradron Melka, Marindon Registrar, and representative of The Gate.'")
print()
Race = input("*Moradron squints, tilts his head, and then looks you up and down.* 'I'm sorry, what are you?' (Human,Orc,Elf,Dwarf): ").upper()
print("-----------------------------------------------------")
print(f"'I see I see. Can't say I would've guessed you were of {Race} kin. *Moradron takes off his foggy, filthy spectacles and continues to clean them in a handful of his robe.*")
print()
if Race == "HUMAN":
    print(f"Of course, as a Human myself, I believe I can relate to you to a certain degree, but judging on your attire...perhaps not.")
elif Race == "ELF":
    print(f"I never did quite understand Elves. You could iron your clothes until the sun rises and they still scowl at you as if you've just burned down one of their churches *Moradron rolls his eyes upwards to close them, shaking his head.*")
elif Race == "DWARF":
    print(f" 'Though I am almost certain of the pride you hold for your race, I can assure you that us academics in Marindon tend to get annoyed with the boisterous Dwarven nature.' ")
elif Race == "ORC":
    print(f"Ah, now that my glasses are clean, I can indeed see your...rather hapless features. Plenty of your kind here.")
    Reac1 = input("[]Choose an option: [(1)Remain Silent (2) Is that an insult? How dare you?]: ")
    if Reac1 == "2":
        print("-----------------------------------------------------")
        print("*Your eyes blur, momentarily, as your jaw slams shut, involuntarily. You feel slightly disoriented from the impact.*")
        print()
        print("'I'll not be having any of this.' *Moradron sternly says, with a raised finger that looked peculiarly frosty-white.*")
        print()
        MorDis = MorDis - 2
        print("______Moradron Melka has lost respect for you.______")
        print()

    if Reac1 == "1":
        print("-----------------------------------------------------")
        print("*Moradron chuckles quietly.*")
        print()


#Class Selection

Class = input(" '...and what is it that you do?' (Fighter, Scoundrel, Mender, Magician): ").upper()
print("-----------------------------------------------------")
print(" *Moradron nods.* Fascinating! I trust that this path has been fruitful?: ")
MorQ1 = input("(Y, N): ").upper()
print("-----------------------------------------------------")
if MorQ1 == "Y":
    print("Marvelous! I trust that your positivity and spirit will carry you through this challenging life.")
elif MorQ1 == "N":
    print(" 'That's unfortunate. Often times we possess skill, but lack the corresponding passion. Alas, not everyone gets the luxury of enjoying work.' *Moradron harumphs* ")

print()
print(f" *As he looks through the window, he once-again utilizes his robe to clean his spectacles.* 'Well I'm sure we can find use for a {Race} {Class} around here.")
print()

# Origin Selection

print("Would you mind telling me a bit about yourself?")
Origin = input("[]Select an option: [(1) Recount a nobility origin (2) Recount an impoverished origin (3) Recount a nomadic origin (4) Recount a secluded origin]: ")
print("-----------------------------------------------------")
if Origin == "1":
    print("Now that you mention it, your surname does sound familiar. I'm so glad you've decided to travel to Marindon. *Moradron flashes a rather exploitative smile* ")
    print()
    MorDis = MorDis + 1
    MarindonNobility = MarindonNobility + 2
    print("______You have gained reputation with the Nobility of Marindon.______")
    print("______Moradron Melka has gained respect for you.______")
    print()
elif Origin == "2":
    print("It upsets me to hear of such struggle. *Moradron takes a long haul from his pipe, then proceeds to open a drawer, gathering something and giving it to you...almost stealthily.*")
    print()
    print("______Moradron Melka has given you 2 Bretheren.______")
    HeroFunds = HeroFunds + 1
    print()
    print("Take it. Keep it. Be wise.")
elif Origin == "3":
    print("Incredible. If there's something that the world is in dire need of right now, it's experience. Welcome to Marindon!")
    print()
    GateRep = GateRep + 2
    print("______You have gained reputation with The Gate.______")
    print()
elif Origin == "4":
    print("*Moradron nods, as he tries to minimize the wrinkle that appeared on the bridge of his nose* Fascinating. You must have had a very...peaceful upbringing.")
    print()
    Lore = Lore + 2
    print("______You have gained 2 points in Lore.______")

print()
if MorDis >= 3:
    print(f"I'm pleased to have met your acquaintance, {Name}! I hope Marindon bears the fruits you are looking for!")
elif MorDis < 3:
    print(f"Right. Let's get you through, {Name}. No need to dally.")
print()

# Beginner Gear Acquisition
print(" *Moradron Melka stands up from his desk, revealing his rather tall stature as he brushes off the knees of his grey robe. He opens the palm of his right hand, moving it insistently towards the large wooden door behind the desk.*")
print()
print("*The black, cast-iron doorknob is cold, as if no one has ever been processed through these gates. You enter a small hallway with several stools lining the wall. One other individual is skulking around the room.*")
print("")
StrangerReac = input("[]Select an option: [(1) Introduce yourself (2) Remain inconspicuous (3) Ask what they're doing here]: ")
print("-----------------------------------------------------")
if StrangerReac =="1":
    print(f"'A pleasure. My name is of no consequence. An absence of personal connection does not negate my knowledge of you, {Name}. I know of your exploits as a {Class} on the other side of the sea.")
elif StrangerReac == "2": 
    print(f"*The stranger catches you glancing at him pacing the room. He approaches you.* You are {Name}, and your exploits are known. Not every {Class} has achieved what you have in a lifetime.")
elif StrangerReac == "3":
    print(f"*The stranger's cloak swoops emphatically as he turns to meet your gaze.* 'That's none of your concern, {Name}. *He pauses and sighs* You aren't a very hard {Class} to find.'")
print()

if Class == "FIGHTER":
    print(f"I've observed you long enough to know that you know how to use these. Strike down your enemies, brave {Class}, and may you hear the lamentations of their allies.")
    print()
    add_to_inventory(rusty_scabbard)
    add_to_inventory(tainted_watchman_tunic)
    print()

print(f"*You feel as if your eyes have been squished just slightly enough to distort your vision as the outline of the stranger, and colours-within dissolve in your hazy gaze*")
print("*Your vision has returned to normal. It's as if the stranger was never here.*")


# Create a story that has The Gate as a corrupted organization that picks and chooses who they want to let in. The stranger you meet in the hallway that gives you a weapon is 
# part of a group intended to investigate The Gate





