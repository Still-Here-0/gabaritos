import random
import os

class Ser:
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False

class Hero(Ser):
    def __init__(self, name:str) -> None:
        self.name = name
        self.max_hp = 5
        self.hp = 5
        self.atk = 3
        self.spd = 2
        self.level = 0
        self.exp = 0
        self.is_alive = True
    
    def set_stats_by_level(self):
        self.max_hp = 5*(1 + self.level)
        self.hp = self.max_hp
        self.atk = 3*(1 + self.level)
        self.spd = 2*(1 + self.level)

    def gain_exp(self, enemy):
        self.exp += enemy.exp_from_kill
        self.hp += enemy.atk
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        
        if int(self.exp/(40)) != self.level:
            self.level_up(int(self.exp/40) - self.level)

    def level_up(self, ups:int):
        self.level += ups
        self.set_stats_by_level()
        print('Parabens vc subiu de level')
        input(
            'Seu estatus atuais:\n'
            f'{"Vida":<10} -> {self.hp}\n'
            f'{"Ataque":<10} -> {self.atk}\n'
            f'{"Velocidade":<10} -> {self.spd}\n'
            'Aperte enter ara continuar\n',
        )
    
    def atk_enemy(self, enemy):
        enemy.take_damage(self.atk)
        if not enemy.is_alive:
            self.gain_exp(enemy)

class Enemy(Ser):
    def __init__(self, hp, atk, spd) -> None:
        self.hp = hp
        self.atk = atk
        self.spd = spd
        self.is_alive = True
        self.exp_from_kill = hp+atk+spd

    def atk_hero(self, hero):
        hero.take_damage(self.atk)

def play():
    print('Bem vindo ao jogo')
    name = input('Qual é o seu nome?\n')
    player = Hero(name)
    while player.is_alive:
        monster = random_enemy(player)
        print(
            f'Você encontrou um inimigo com {monster.hp} de vida e {monster.atk} de ataque.',
            'Seus status são:',
            f'{"Vida":<10} -> {player.hp}',
            f'{"Ataque":<10} -> {player.atk}',
            f'{"Velocidade":<10} -> {player.spd}',
            f'{"Level":<10} -> {player.level}',
            sep='\n'
        )
        fight(player, monster)
        clear_tetminal()

def clear_tetminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def random_enemy(player:Hero) -> Enemy:
    hp = round(random.random()*player.level**2 + random.choice([x for x in range(player.level+1, player.level**2 + 10)]), 1)
    atk = round(random.random()*player.level**2 + random.choice([x for x in range(player.level+1, player.level*2 + 3)]), 1)
    spd = round(random.random()*player.level**2 + random.choice([x for x in range(player.level+1, player.level*2 + 2)]), 1)

    return Enemy(hp, atk, spd)

def fight(player:Hero, monster:Enemy):
    choise = int(input('Deseja tentar fugir ou lutar?\n1. Lutar\n2. Fugir\n'))
    if choise == 2 and player.spd > monster.spd:
        input('Vc conseguiu fugir')
        return
    elif choise == 2:
        input('Vai ter que lutar irmão')

    while True:
        clear_tetminal()
        print(
            f'Status:',
            f'{"":#^10}|{player.name:^10.10s}|{"Monstro":^10}',
            f'{"Vida":^10}|{player.hp:^10}|{monster.hp:^10}',
            f'{"ataque":^10}|{player.atk:^10}|{monster.atk:^10}',
            f'{"Velocidade":^10}|{player.spd:^10}|{monster.spd:^10}',
            sep='\n'
        )
        choise = input('O que você deseja fazer?\n1. Atacar\n2. Correr\n')
        if choise == 2 and player.spd*random.random() > monster.spd*random.random():
            input('Você fugiu')
            break
        elif choise == 2:
            input('Vai tomar porrada de graça')
            monster.atk_hero(player)
        else:
            player.atk_enemy(monster)
            if monster.is_alive:
                monster.atk_hero(player)
            else:
                break
        
        if not player.is_alive:
            break

if __name__ == "__main__":
    play()
