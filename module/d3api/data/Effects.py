class Effect(object):
    pass


from item_utils import class_skills

spirit_spenders = [skill for skill in class_skills('Monk') if 'Generate' in skill.description and 'Spirit' in skill.description]
print(spirit_spenders)

non_spirit_spenders = set(class_skills('Monk')) - set(spirit_spenders)
print(non_spirit_spenders)

crit_hits = [skill for skill in class_skills('Monk') if 'Critical' in skill.description]
print(crit_hits)


print()

essence_spenders = [skill for skill in class_skills('Necromancer') if 'Generate' in skill.description and 'Essence' in skill.description]
print(essence_spenders)

non_essence_spenders = set(class_skills('Necromancer')) - set(essence_spenders)
print(non_essence_spenders)

crit_hits = [skill for skill in class_skills('Necromancer') if 'crit' in skill.description.lower()]
print(crit_hits)

# upping Critical hit chance -> via Enchanting -> weapon effects

