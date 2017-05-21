# bless vs advantage
import random

def getDieRoll(die):
    # generates a random die roll based on the die size
    myDie = random.randint(1, die)
    return myDie


def getAdvDieRoll(dieSize):
    twoRolls = []
    twoRolls.append(getDieRoll(dieSize))
    twoRolls.append(getDieRoll(dieSize))
    twoRolls.sort(reverse=True)
    return twoRolls[0]



def attackAdvantage(defAC, profBonus, statBonus, weaponDamage):
    roll=getAdvDieRoll(20)
    if roll == 1:
        #fumble
        return 0,0
    elif roll == 20:
        #critical hit
        return (getDieRoll(weaponDamage) + getDieRoll(weaponDamage) + statBonus ),1
    elif ((roll + statBonus + profBonus) >= defAC):
        #hit
        return (getDieRoll(weaponDamage) + statBonus ),0
    else:
        #miss
        return 0,0

def attackBless(defAC, profBonus, statBonus, weaponDamage):
    roll=getDieRoll(20)
    rollBonus=getDieRoll(4)
    if roll == 1:
        #fumble
        return 0,0
    elif roll == 20:
        #critical hit
        return (getDieRoll(weaponDamage) + getDieRoll(weaponDamage) + statBonus ),1
    elif ((roll + rollBonus + statBonus + profBonus) >= defAC):
        #hit
        return (getDieRoll(weaponDamage) + statBonus ),0
    else:
        #miss
        return 0,0


#main area
#initial stats
#DefenderAC = 20
profBonus = 2
statBonus = 4
weaponDamage = 12
maxRounds = 50000

#calculation start
for DefenderAC in range(10,40):
    print("=========================================")
    print("============== vs " + str(DefenderAC) + " AC =================")
    print("=========================================")
    blessedAttacks=0
    blessedTotalDamage=0
    blessedHits=0
    blessedAttacks=0
    blessedCrits=0
    for x in range(0,maxRounds):
        damageRoll,crit = attackBless(DefenderAC, profBonus, statBonus, weaponDamage)
        #print("The Blessed attacker did " + str(damageRoll) + " Damage!")
        if damageRoll > 0:
            blessedHits+=1
        if crit==1:
            blessedCrits+=1
        blessedAttacks+=1
        blessedTotalDamage+=damageRoll
    #print("Blessed vs " + str(DefenderAC) + " AC:")
    print("The Blessed attacker did " + str(blessedTotalDamage) + " Total Damage in " + str(blessedHits) + " hits out of " + str(blessedAttacks) + " attempts (" + str(round((blessedHits/blessedAttacks),3) * 100) + "%) with " + str(round(blessedCrits, 2)) + " Criticals " + str(round((blessedCrits/blessedHits),3) * 100) + "%!")
    print("Average damage of " + str(blessedTotalDamage/blessedAttacks) + " Or " + str(blessedTotalDamage/blessedHits) + " per hit.")


    advAttacks=0
    advTotalDamage=0
    advHits=0
    advAttacks=0
    advCrits=0
    for y in range(0,maxRounds):
        damageRoll,crit = attackAdvantage(DefenderAC, profBonus, statBonus, weaponDamage)
        #print("The Advantaged attacker did " + str(damageRoll) + " Damage!")
        if damageRoll > 0:
            advHits+=1
        if crit==1:
            advCrits+=1
        advAttacks+=1
        advTotalDamage+=damageRoll
    #print("Advantaged vs " + str(DefenderAC) + " AC: ===========================")
    print("The Advantaged attacker did " + str(advTotalDamage) + " Total Damage in " + str(advHits) + " hits out of " + str(advAttacks) + " attempts (" + str(round((advHits/advAttacks),3) * 100) + "%) with " + str(advCrits) + " Criticals "  + str(round((advCrits/advHits),3) * 100) + "%!")
    print("Average damage of " + str(advTotalDamage/blessedAttacks) + " Or " + str(advTotalDamage/advHits) + " per hit.")
    if (blessedTotalDamage > advTotalDamage):
        print("Blessed Wins! total damage is " + str(round((blessedTotalDamage/advTotalDamage),3) * 100) + "% of Advantage")
    else:
        print("Advantage Wins! total damage is " + str(round((advTotalDamage/blessedTotalDamage),3) * 100) + "% of Blessed")
