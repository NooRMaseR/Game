from base import Weapon
from characters import Man, Woman

man1 = Man("noor", 20, Weapon.SWORD, Weapon.SHIELD)
man2 = Man("ali", 20, Weapon.BOW)

woman1 = Woman("jana", 20, Weapon.BOW, Weapon.HANDS, defense=20)

man1.attack(woman1)
man2.attack(woman1)
man1.attack(woman1)
man1.attack(woman1, used_weapon=Weapon.SHIELD)
man1.attack(woman1)
man2.attack(woman1)
man2.attack(woman1)

woman1.attack(man1, used_weapon=Weapon.BOW)
