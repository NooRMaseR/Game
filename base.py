from typing import LiteralString, Protocol
from frames import FULL_FIGHTING_FRAME
from abc import ABC, abstractmethod
from enum import IntEnum
import click

class Weapon(IntEnum):
    SWORD = 30
    BOW = 10
    SHIELD = 15
    HANDS = 5

    @property
    def name(self) -> LiteralString:
        return self._name_.lower()


class Dieable(Protocol):
    "a Protocol for an object to make it able to die"
    
    name: str
    
    @property
    def health(self) -> int: ...
    
    @health.setter
    def health(self, value: int) -> None: ...
    
    @property
    def armor(self) -> int: ...
    
    @armor.setter
    def armor(self, value: int) -> None: ...
    
    @property
    def is_alive(self) -> bool: ...


class AliveObject(ABC):
    "Base class for any alive object"
    
    def __init__(self, name: str, age: int, health: int = 100, armor: int = 0) -> None:
        super().__init__()
        self.name: str = name
        self.__health: int = health
        self.__armor: int = armor
        self.__age: int = age
        
    @property
    def is_alive(self) -> bool:
        "check wither the object is alive or not"
        return self.__health > 0
        
    @property
    def health(self) -> int: 
        return self.__health
    
    @health.setter
    def health(self, value: int) -> None:
        self.__health = max(value, 0)
        
    @property
    def armor(self) -> int: 
        return self.__armor
    
    @armor.setter
    def armor(self, value: int) -> None:
        self.__armor = max(value, 0)
        
    @property
    def age(self) -> int: 
        return self.__age
    
    @age.setter
    def age(self, value: int) -> None:
        assert 0 < value <= 100, "Age must be between 1 and 100"
        self.__age = value
        
    
    def __str__(self) -> str:
        return f"""
{self.__class__.__name__}(
    Name: {self.name}
    Health: {self.health}
    armor: {self.armor}
    is alive: {self.is_alive}
)"""
    
    

class Attacker(ABC):
    "Abstract class for any object that can attack"
    
    def attack(self, target: Dieable, used_weapon: Weapon | None = None) -> None: 
        """Attack `AliveObject`\n
        make sure that the object will inherit this class has `is_alive` property

        Args:
            target (Dayable): an Object that has protocol `dieable` or somthing able to die
            used_weapon (Weapon): The weapon to use to attack the target, the current object must have this weapon, otherwise will use his hands or a sword if he has one
        """
        
        if not self.is_alive:
            click.echo(f"{self.name} is already dead, can't fight...")
            return
        
        if not target.is_alive:
            click.echo(f"{target.name} is already dead...")
            return
        
        weapon: Weapon = self.select_weapon(used_weapon)
        damage: int =  self.calculate_damage(weapon, target.armor)
        click.echo(FULL_FIGHTING_FRAME)
        
        if target.armor > 0:
            if damage > target.armor:
                target.health -= (damage - target.armor)
            target.armor -= damage
        else:
            target.health -= damage
        
        click.echo(f"{target.name} has been damaged by {damage}% using {weapon.name}")
        click.echo(f"{target.name}'s health {target.health}% and armor {target.armor}%")
        
        if not target.is_alive:
            click.echo(f"{target.name} died...")
        
        click.echo("\n")
    
    
    def add_weapon(self, weapon: Weapon) -> None: 
        """a method to add an extra weapon

        Args:
            weapon (Weapon): the weapon to add
        """
        assert isinstance(weapon, Weapon), "the weapon Parameter Must Be A Weapons Instance"
        assert self.check_weapons_limit(len(self.weapons)), "You Have Reached the maximum number of weapons"
        
        self.weapons = (*self.weapons, weapon)
    
    
    def remove_weapon(self, weapon: Weapon) -> None:
        """a method to remove a weapon

        Args:
            weapon (Weapon): the weapon to remove
        """
        assert isinstance(weapon, Weapon), "the weapon Parameter Must Be A Weapons Instance"
        weapons = list(self.weapons)
        weapons.remove(weapon)
        self.weapons = tuple(weapons)
    
    
    def select_weapon(self, weapon: Weapon | None) -> Weapon:
        """a method to select a weapon if the object has it

        Args:
            weapon (Weapon | None): the weapon to select, if the weapon doesn't exists then use `hands`

        Returns:
            Weapon: the selected weapon
        """
        weapons: tuple[Weapon, ...] = self.weapons
        if weapon in weapons:
            return weapon
        elif Weapon.SWORD in weapons:
            return Weapon.SWORD
        else:
            return weapons[0] if len(weapons) > 0 else Weapon.HANDS
    
    
    def calculate_damage(self, damage: int, armor: int) -> int:
        """a method to calculate a the damage will the object takes by reducing the damage using object `armor`

        Args:
            damage (int): the weapon damage
            armor (int): the target armor

        Returns:
            int: the damage will be used
        """
        return int(max(damage - ((damage / 100) * armor), 0))
    
    
    @property
    @abstractmethod
    def weapons(self) -> tuple[Weapon, ...]:
        """a property to get the weapons

        Returns:
            tuple[Weapon]: the object weapons
        """
    
    
    @weapons.setter
    @abstractmethod
    def weapons(self, weapons: tuple[Weapon, ...]) -> None: ...
    
    
    @property
    @abstractmethod
    def max_weapons(self) -> int: ...
        
        
    def check_weapons_limit(self, length: int) -> None:
        if not length <= self.max_weapons:
            raise ValueError(f"{self.__class__.__name__} Cannot Hold More Than {self.max_weapons} weapons!!!!")
        