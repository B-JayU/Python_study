# -*- coding: EUC-KR -*-

class Unit:
    def __init__(self):
        print("Unit ������")

class Flyable:
    def __init__(self):
        print("Flyable ������")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()


dropship = FlyableUnit()