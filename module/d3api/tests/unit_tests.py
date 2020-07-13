"""

"""

'''

does every thing still works
loads
is complete
'''

from datatypes import Classes
from Diablo3_webScraper import Class_Info
import os

def is_complete():

    complete = True
    for cls in Classes.items():
        _cls = Class_Info(cls)
        print(_cls.root_folder)
        if not os.path.exists(_cls.root_folder):
            complete = False
    return complete

print(is_complete())