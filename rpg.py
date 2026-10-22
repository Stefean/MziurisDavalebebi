class Character: 
    count = 0
    def __init__(self, name, hp=100, level=1):
        self.name = name
        self.hp = hp
        self.level = level
        Character.count += 1

    def __str__(self):
        return f"{self.name}(Lv {self.level}, HP {self.hp})"

    def take_damage(self, amount):
        self.hp = self.hp - amount
        if self.hp < 0:
            self.hp = 0

    def attack(self, target):
        target.take_damage(5)

    @classmethod
    def from_string(cls, char_str):
        parts = char_str.strip().split(";")
        if len(parts) == 2:
            return Warrior(parts[0], int(parts[1]))
        return False

    @staticmethod
    def is_valid_name(name):
        return  2<len(name)<20

    def __eq__(self, other):
        if isinstance(other, Character):
            return self.name == other.name
        else:
            return False

    @property
    def is_alive(self):
        return self.hp > 0 

class Warrior(Character):
    def __init__(self, name,hp=100, level=1, strength=10):
        super().__init__(name, hp, level)
        self.strength = strength

    def attack(self, target):
        target.take_damage(self.strength)

class Mage(Character):
    def __init__(self, name, hp=100, level=1, mana=50):
        super().__init__(name, hp, level)
        self.mana = mana

    def attack(self, target):
        if self.mana < 10:
            super().attack(target)
            return
            
        self.mana -= 10
        target.take_damage(20)

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} MP {self.mana}"

class HealerMixin:
    def heal(self, target, amount):
        target.hp += int(amount)

class Priest(HealerMixin, Mage):
    def __init__(self, name, hp=100, level=1, mana=50):
        super().__init__(name, hp, level, mana)

# a = Character("Tariel")
# b = Character("Avtandil", hp=50)
# b.take_damage(70)

# print(a)                 # Tariel (Lv 1, HP 100)
# print(b)                 # Avtandil (Lv 1, HP 0)
# print(b.is_alive)        # False
# print(Character.count)   # 2

# t = Warrior("Tariel", hp=120, strength=15)
# n = Mage("Nestan", hp=80, mana=15)

# t.attack(n)
# print(n)    # Nestan (Lv 1, HP 65) MP 15

# n.attack(t)   # 20 ზიანი, mana-ს 5 რჩება
# n.attack(t)   # mana არ ჰყოფნის: 5 ზიანი
# print(t)    # Tariel (Lv 1, HP 95)

p = Priest("Nestan", hp=60)
w = Warrior.from_string("Tariel;120")

# p.heal(w, 30)
# print(w)                                   # Tariel (Lv 1, HP 150)
# print(type(w).__name__)                    # Warrior
# print(Character.is_valid_name("T"))        # False
# print(Character("A") == Character("A"))    # True
