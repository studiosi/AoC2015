import itertools
import copy

def combat(spell_ids):
    current_boss = copy.copy(boss)
    current_player = copy.copy(player)
    total_cost = 0
    # effects is a list of tuples (spell, timer)
    effects = {}
    active_effects = []
    for spell_id in spell_ids:
        # 1 Player Turn
        # 1.0 Effects Turn
        current_player[2] = 0
        current_player[3] = 0
        for effect_id in active_effects:
            effect_stats = effects[effect_id]
            effect_stats[1] -= 1            
            current_player[1] += effect_stats[0][6]
            current_player[2] += effect_stats[0][4]
            current_boss[0] -= effect_stats[0][5]
            if effect_stats[1] == 0:
#                active_effects.remove(effect_id)
                del effects[effect_id]
            active_effects = [a for a in effects]
        spell = spells[spell_id]
        # 1.2 Cast spell
        # 1.2.1 Normal spell
        if not spell[7]:
            if current_player[1] >= spell[0]:
                current_boss[0] -= (spell[1] + current_player[3])
                current_player[0] += spell[2]
                total_cost += spell[0]
                current_player[1] -= spell[0]
            else:
                return None                 
        # 1.2.2 Effect spell
        else:
            if spell_id not in active_effects:
                effects[spell_id] = [spell, spell[3]]
                active_effects.append(spell_id)
                total_cost += spell[0] 
                current_player[1] -= spell[0]
            else:
                return None
        if current_boss[0] <= 0:
            return total_cost
        # 2 Boss Turn
        # 2.0 Effects Turn
        current_player[2] = 0
        current_player[3] = 0
        for effect_id in active_effects:
            effect_stats = effects[effect_id]
            effect_stats[1] -= 1            
            current_player[1] += effect_stats[0][6]
            current_player[2] += effect_stats[0][4]
            current_boss[0] -= effect_stats[0][5]
            if effect_stats[1] == 0:
#                active_effects.remove(effect_id)
                del effects[effect_id]
            active_effects = [a for a in effects]
        if current_boss[0] <= 0:
            return total_cost
        # 2.1 Calculate damage
        real_damage = current_boss[1] - current_player[2]
        # 2.2 Deal damage
        current_player[0] -= real_damage
        # 3 Check win
        if current_player[0] <= 0:
            return None
        elif current_boss[0] <= 0:
            return total_cost

# (hit_points, damage)
boss = [58, 9]

# (hit_points, mana, armor, damage_increase)
player = [50, 500, 0, 0]

# (cost, damage, healing, effect_length, effect_increase_armor, effect_damage, effect_recharge, is_effect )
spells = {

    1: (53, 4, 0, 0, 0, 0, 0, False),
    2: (73, 2, 2, 0, 0, 0, 0, False),
    3: (113, 0, 0, 6, 7, 0, 0, True),
    4: (173, 0, 0, 6, 0, 3, 0, True),
    5: (229, 0, 0, 5, 0, 0, 101, True)

}

i = 0
end = False
min_mana = 1e100
j = 9
while True:
    for x in itertools.product([1,2,3,4,5], repeat=j):
        print(".",  end="")
        total_mana = combat(x)
        if total_mana is not None:
            min_mana = min(min_mana, total_mana) 
    if min_mana != 1e100:
        break
    else:
        j += 1
print(min_mana)
