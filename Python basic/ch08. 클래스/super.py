# -*- coding: EUC-KR -*-

class Unit:
    def __init__(self):
        print("Unit 持失切")

class Flyable:
    def __init__(self):
        print("Flyable 持失切")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()


dropship = FlyableUnit()