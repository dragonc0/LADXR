from .itemInfo import ItemInfo


class Toadstool(ItemInfo):
    OPTIONS = ["TOADSTOOL"]

    def patch(self, rom, option):
        pass

    def read(self, rom):
        return "TOADSTOOL"
