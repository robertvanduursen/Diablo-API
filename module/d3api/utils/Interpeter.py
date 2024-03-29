"""

an attempt of turning Item effect text into executable code and values

"""

'''
Extend item w
Damage attribute
Interpreted effect
I.e. if equipped; modifies stats if ability is also equipped

'''


class Interpeter(object):
    focus = False

    def __init__(self, tokens):
        self.tokens = tokens

    def process(self):
        print('_classes found: {}'.format(self._classes))
        print('_attributes found: {}'.format(self._attributes))
        print('_skills found: {}'.format(self._skills))
        print('_passives found: {}'.format(self._passives))

    @property
    def _classes(self):
        return set(self.tokens) & {'Necromancer', 'Barbarian', 'Wizard'}

    @property
    def _skills(self):
        import item_utils
        return set(self.tokens) & set(item_utils.all_class_skill_names())

    @property
    def _passives(self):
        return []

    @property
    def _attributes(self):
        """ look for attributes in the tokens that aid in a playstyle """
        with open(r'G:\projects\Diablo-API\module\d3api\data\attributes.txt', 'r') as token_file:
            attrs = [x[:-1] for x in token_file.readlines() if x[:-1] != '']

        return set(self.tokens) & set(attrs)

    def isClassRestricted(self):
        if self._classes:
            for cls in self._classes:
                if '{} Only'.format(cls) in self.tokens:
                    return '{} Only'.format(cls)
        return False

    @property
    def result(self):
        statements = []
        restricted = self.isClassRestricted()
        if restricted:
            statements.append("restricted to {}: requires {} class".format(restricted, restricted[:-len(' Only')]))

        return statements
