# Keeps track of how much time you have spent on various skills

# import modules
import os

# TODO Load skills from file into dictionary
# Creates a dictionary of skills
skills = {}

# TODO Add loop for adding skills
# User input for skill name and time spent
print("Enter a skill")
skillName = input()
print("How much time did you spend on it? (in hours)")
skillTime = int(input())

# Gets the skill time from the dictionary and updates it
totalSkillTime = skills.get(skillName, 0)
totalSkillTime += skillTime
skills.update({skillName: totalSkillTime})

# Updates the file
skillFile = open("skills.txt", "w")

for k in skills.keys():
    skillFile.write(k + ": " + str(skills[k]))
skillFile.close()
