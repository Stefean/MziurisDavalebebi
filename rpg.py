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

    @property
    def is_alive(self):
        return self.hp > 0 

class Warrior(Character):
    def __init__(self, name,hp=100, level=1, strength=10):
        super().__init__(name, hp, level)
        self.strenght = strength

    def attack(self, target):
        target.take_damage(self.strenght)

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

a = Character("Tariel")
b = Character("Avtandil", hp=50)
b.take_damage(70)

print(a)                 # Tariel (Lv 1, HP 100)
print(b)                 # Avtandil (Lv 1, HP 0)
print(b.is_alive)        # False
print(Character.count)   # 2

t = Warrior("Tariel", hp=120, strength=15)
n = Mage("Nestan", hp=80, mana=15)

t.attack(n)
print(n)    # Nestan (Lv 1, HP 65) MP 15

n.attack(t)   # 20 ზიანი, mana-ს 5 რჩება
n.attack(t)   # mana არ ჰყოფნის: 5 ზიანი
print(t)    # Tariel (Lv 1, HP 95)
