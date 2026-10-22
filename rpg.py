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

    @property
    def is_alive(self):
        return self.hp > 0 


a = Character("Tariel")
b = Character("Avtandil", hp=50)
b.take_damage(70)

print(a)                 # Tariel (Lv 1, HP 100)
print(b)                 # Avtandil (Lv 1, HP 0)
print(b.is_alive)        # False
print(Character.count)   # 2