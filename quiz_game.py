# Computer Quiz Game

print("\nWelcome to my computer quiz!\n")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("\nOkay! Let's Play :)\n")
score = 0
ques = 0

answer = input("What does \"CPU\" stands for? ")
if answer.lower() == "central processing unit":
    print("Correct\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("What does \"GPU\" stands for? ").lower()
if answer == "graphics processing unit":
    print("Correct\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("What does \"RAM\" stands for? ")
if answer.lower() == "random access memory":
    print("Correct\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("What does \"PSU\" stands for? ").lower()
if answer == "power supply unit":
    print("Correct\n")
    score += 2
else:
    print("Incorrect!\n")

answer = input("What does \"NVMe SSD\" stands for? ")
if answer.lower() == "non volatile memory express solid state drive":
    print("Correct\n")
    score += 2
else:
    print("Incorrect!\n")

answer = input("What does \"SATA\" stands for? ")
if answer.lower() == "serial at attachment":
    print("Correct\n")
    score += 2
else:
    print("Incorrect!\n")

answer = input("What does \"HDD\" stands for? ")
if answer.lower() == "hard disk drive":
    print("Correct\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("What does \"DDR4 SODIMM RAM\" stands for? ")
if answer.lower() == "double data rate 4th gen small outline dual inline memory module random access memory":
    print("Correct\n")
    score += 3
else:
    print("Incorrect!\n")

answer = input("What does \"UEFI BIOS\" stands for? ")
if answer.lower() == "unified extensible firmware interface basic input output system":
    print("Correct\n")
    score += 3
else:
    print("Incorrect!\n")

answer = input("What does \"AIO\" cooler stands for? ")
if answer.lower() == "all in one cooler":
    print("Correct\n")
    score += 2
else:
    print("Incorrect!\n") 

answer = input("What does \"VRM\" stands for? ")
if answer.lower() == "voltage regulator module":
    print("Correct\n")
    score += 2
else:
    print("Incorrect!\n")

#print("You got "+str(score)+" questions correct!\n")
print("You got "+str((score/20)*100)+ "%.\n")