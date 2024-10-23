from base import Attacker, AliveObject, Weapon

class Man(AliveObject, Attacker):
    
    def __init__(self, name: str, age: int, *weapons: Weapon, health: int = 100, defense: int = 0) -> None:
        self.__max_weapons: int = 5
        assert self.check_weapons_limit(len(weapons)), "Man Cannot Hold More Than 5 weapons!!!!"
        self.__weapons: tuple[Weapon, ...] = weapons if len(weapons) > 0 else (Weapon.HANDS,)
        
        super().__init__(name, age, health, defense)

    @property
    def weapons(self) -> tuple[Weapon, ...]:
        return self.__weapons
    
    @weapons.setter
    def weapons(self, weapons: tuple[Weapon, ...]) -> None:
        self.__weapons = weapons

    @property
    def max_weapons(self) -> int:
        return self.__max_weapons

        

class Woman(AliveObject, Attacker):
    
    def __init__(self, name: str, age: int, *weapons: Weapon, health: int = 100, defense: int = 0) -> None:
        self.__max_weapons: int = 2
        assert self.check_weapons_limit(len(weapons)), "Woman Cannot Hold More Than 2 weapons!!!!"
        self.__weapons: tuple[Weapon, ...] = weapons if len(weapons) > 0 else (Weapon.HANDS,)
        
        super().__init__(name, age, health, defense)
        
    @property
    def weapons(self) -> tuple[Weapon, ...]:
        return self.__weapons

    @weapons.setter
    def weapons(self, weapons: tuple[Weapon, ...]) -> None:
        self.__weapons = weapons

    @property
    def max_weapons(self) -> int:
        return self.__max_weapons





    