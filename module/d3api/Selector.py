""" the discriminator """


class Selector(object):
    pass


scope = [
    r'C:\Users\rober\Google Drive\Games\Diablo\Resources.py',
    r'C:\Users\rober\Google Drive\Games\Diablo\Barbarian\items.py',
    r'C:\Users\rober\Google Drive\Games\Diablo\Barbarian\items_cache.py',
    r'C:\Users\rober\Google Drive\Games\Diablo\Rifts.py',
    r'C:\Users\rober\Google Drive\Games\Diablo\Barbarian\passives.py',
    r'C:\Users\rober\Google Drive\Games\Diablo\Barbarian\skills.py',
    r'C:\Users\rober\Google Drive\Games\Diablo\Kanai.py',
]


scope_globals = {}
scope_locals = {}

import inspect
import os

query = 'BloodShard'
for scope_file in scope:
    module = os.path.basename(scope_file)[:-len('.py')]
    subscope = __import__(module, scope_globals, scope_locals)
    # print("loaded {}".format(subscope))
    # print(dir(subscope))

    for name, cls in inspect.getmembers(subscope, inspect.isclass):
        if query in inspect.getsource(cls):
            for name, func in inspect.getmembers(cls, inspect.isfunction):
                sig = inspect.signature(func)
                if sig.return_annotation is not sig.empty:
                    return_anno = sig.return_annotation[0]
                    if query in str(return_anno):
                        print("\tclass: {}, has func '{}', returns {}".format(cls, name, query))
                        print("\tlocated in {}".format(subscope))






