# Keeps track of how much time you have spent on various skills
# TODO Add display of skills

# import modules
import os
fileName = "skills.txt"

# Creates file with name "fileName" if it does not exist
skillFile = open(fileName, "a")
skillFile.close()

# Creates a dictionary of skills
skills = {}

# Opens fileName to read the file into memory
skillFile = open(fileName, "r")
fileContents = skillFile.read()
skillFile.close()

# Splits the file into a multi-layer list
formattedContents = fileContents.split("\n")
for i in range(len(formattedContents)):
    formattedContents[i] = formattedContents[i].split(": ")
del formattedContents[-1]

# Formats list into the skills dictionary
for i in range(len(formattedContents)):
    skillName = formattedContents[i][0]
    startSkillTime = int(formattedContents[i][1])
    skills.update({skillName: startSkillTime})

# User input for skill name and time spent (Loops until blank skill)
while True:
    print("Enter a skill (Leave blank to exit)")
    skillName = input()

    # Exits if blank skill
    if skillName == "":
        break
    print("How much time did you spend on it? (in hours)")
    skillTime = int(input())

    # Gets the skill time from the dictionary and updates it
    totalSkillTime = skills.get(skillName, 0)
    totalSkillTime += skillTime
    skills.update({skillName: totalSkillTime})

# Updates the file
skillFile = open(fileName, "w")

for k in skills.keys():
    skillFile.write(k + ": " + str(skills[k]) + "\n")
skillFile.close()
