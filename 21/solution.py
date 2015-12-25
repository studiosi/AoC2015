import itertools

# BOSS (hit points, damage, armor)
boss = (100, 8, 2)
# WEAPONS (cost, damage, armor) [ exactly one ]
weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
# ARMOR (cost, damage, armor) [ zero or one ]
armors = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
# RINGS (cost, damage, armor) [ zero, one or two ]
rings = [ (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3) ]

# (cost, damage, defense)
def getStats(weapon, armor, ringSet):
    cost = weapon[0]
    damage = weapon[1]
    defense = weapon[2]
    if (-1, -1, -1) != armor:
        cost += armor[0]
        damage += armor[1]
        defense += armor[2]
    if (-1, -1, -1) not in ringSet:
        for ring in ringSet:
            cost += ring[0]
            damage += ring[1]
            defense += ring[2]
    return (cost, damage, defense)

def getStats2(weaponSet, armorSet, ringSet):
    cost = 0
    damage = 0
    defense = 0
    if (-1, -1, -1) not in weaponSet:
        for weapon in weaponSet:
            cost += weapon[0]
            damage += weapon[1]
            defense += weapon[2]
    if (-1, -1, -1) not in armorSet:
        for armor in armorSet:
            cost += armor[0]
            damage += armor[1]
            defense += armor[2]   
    if (-1, -1, -1) not in ringSet:
        for ring in ringSet:
            cost += ring[0]
            damage += ring[1]
            defense += ring[2]                    
    return (cost, damage, defense)                    
        
# Part 1        
armors.append((-1, -1, -1))
ringSets = [ ((-1, -1, -1),) ]
for i in range(1, 3):
    for x in itertools.permutations(rings, i):
        ringSets.append(x)
p = []
for weapon in weapons:
    for armor in armors:
        for ringSet in ringSets:
            stats = getStats(weapon, armor, ringSet)
            p.append(stats)

p = [item for item in p if item[0] <= 100]
p.sort(key=lambda x: x[0])
done = False
min_attack = -1
for x in p:
    hp_char = 100
    hp_boss = boss[0]
    real_damage_char = x[1] - boss[2]
    real_damage_boss = boss[1] -x[2]               
    if real_damage_char <= 0:
        real_damage_char = 1   
    if real_damage_boss <= 0:
        real_damage_boss = 1
    while hp_char > 0 and hp_boss > 0:
        hp_boss -= real_damage_char
        if hp_boss <= 0:
            print("MIN COST: ", x[0])
            min_attack = x[1]
            done = True
        else:            
            hp_char -= real_damage_boss  
    if done:
        break                          

# Part 2  
armors.append((-1, -1, -1))
ringSets = [ ((-1, -1, -1),) ]
for i in range(1, 3):
    for x in itertools.permutations(rings, i):
        ringSets.append(x)
p = []
for weapon in weapons:
    for armor in armors:
        for ringSet in ringSets:
            stats = getStats(weapon, armor, ringSet)
            p.append(stats)

p = [item for item in p]
p.sort(key=lambda x: x[0])

done = False
min_attack = -1
goldLose = 1e-100
i = 0
for x in p:
    print(i, x)
    hp_char = 100
    hp_boss = boss[0]
    real_damage_char = x[1] - boss[2]
    real_damage_boss = boss[1] -x[2]               
    if real_damage_char <= 0:
        real_damage_char = 1   
    if real_damage_boss <= 0:
        real_damage_boss = 1
    while hp_char > 0 and hp_boss > 0:
        hp_boss -= real_damage_char
        if hp_boss <= 0:
            print("BOSS KILLED")
        else:           
            hp_char -= real_damage_boss
            if hp_char <= 0:
                goldLose = max(x[0], goldLose)
                print("DEFEAT ", goldLose)
                
    i += 1            
print(goldLose)                                       