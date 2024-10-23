from base import Weapon
from characters import Man, Woman, Child

woman: Woman = Woman("jana", 20, Weapon.BOW, Weapon.HANDS)
man: Man = Man("noor", 20, Weapon.SWORD, Weapon.SHIELD)
child: Child = Child("ali", 20)

man.attack(woman)
woman.attack(man)

man.attack(woman, used_weapon=Weapon.BOW)
woman.attack(man, used_weapon=Weapon.BOW)

woman.attack(child)
man.attack(child)
