import random

class Hero:
    def __init__(self, name) -> None:
        self.name = name
        self.max_hp = 10
        self.hp = 10
        self.atk = 4
        self.is_alive = True
        self.crit_chance = 0

    def attack(self, enemy) -> None:
        if random.random() <= self.crit_chance:
            enemy_hp = enemy.attacked(self.atk*1.5)
        else:
            enemy_hp = enemy.attacked(self.atk)
        
        if enemy_hp == 0:
            self.killed_a_enemy()
    
    def attacked(self, atk):
        self.hp -= atk
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
    
    def killed_a_enemy(self) -> None:
        self.max_hp += 5
        self.hp = self.max_hp
        self.atk += 3
        self.crit_chance += 0.05

class Moster:
    def __init__(self, type, hp, atk) -> None:
        self.type = type
        self.hp = hp
        self.atk = atk
        self.is_alive = True

    def attack(self, enemy) -> None:
        enemy.attacked(self.atk)
    
    def attacked(self, atk) -> float:
        self.hp -= atk
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
        
        return self.hp

def fight():
    name = input('Qual é o seu nome?\n')
    player = Hero(name)
    moster = Moster('slime', 5, 1)

    while True:
        print_stats(player, moster)
        player.attack(moster)
        
        if moster.is_alive:
            moster.attack(player)
        elif not player.is_alive:
            break
        else:
            moster = new_monster(player)
            input('VOCÊ MATOU O MONSTRO\n')
    
    print('Infelizmente você morreu ;-;')

def print_stats(p, m):
    input(
        f'    {p.name:^10} | {m.type:^10}\n'
        f'HP: {p.hp:^10.4f} | {m.hp:^10.4f}\n'
        f'ATK:{p.atk:^10.4f} | {m.atk:^10.4f}\n'
    )

def new_monster(p):
    type_ = random.choice(['slime', 'morcego', 'zumbi', 'vampiro', 'fantasma', 'bruxa'])
    hp = random.uniform(1, p.hp*1.5)
    atk = random.uniform(0.5, p.atk*0.95)

    return Moster(type_, hp, atk)

if __name__ == '__main__':
    fight()
    pass








x = 5
var = True if x > 10 else False

list_ = ['1', '2', '3', '4', '5']
ret = [int(x) for x in list_]