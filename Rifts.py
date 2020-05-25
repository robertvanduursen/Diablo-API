from Resources import BloodShard


class Rift(object):
    level = 1
    greater = False

    def __init__(self):
        pass

    def source_of(self) -> [BloodShard]:
        amount = [BloodShard()] * 10
        return amount








# todo: how to express a Source-Of-<type> best?
