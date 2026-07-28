import random
import time


class Character:
    def __init__(self, name, health, damage, defense, luck):
        self.name = name
        self.health = health
        self.damage = damage
        self.max_health = health
        self.defense = defense
        self.luck = luck

    def take_damage(self, damage):
        damage_taken = max(0, damage - self.defense)
        self.health -= damage_taken
        return damage_taken

    def true_damage(self, damage):
        damage_taken = max(0, damage)
        self.health -= damage_taken
        return damage_taken

    def attack(self, target):
        critical = random.randint(1, 50) <= self.luck
        damage = self.damage

        if critical:
            damage *= 1.5
            print("")
            print("Critical Hit!")

        return target.take_damage(int(damage))

    def is_alive(self):
        return self.health > 0
    def heal(self):
        self.health += 5 + random.randint(2, self.luck)
    def reset_health(self):
        self.health = self.max_health
    def show_stats(self):
        print(" ")
        print(f"HP:  {self.health}")
        print(f"Damage: {self.damage}")
        print(f"Defense: {self.defense}")
        print(f"Luck: {self.luck}")
        time.sleep(0.5)

class Rogue(Character):
    def attack(self, target):
        critical = random.randint(1, 50) <= self.luck
        damage = self.damage

        if critical:
            damage *= 1.35
            print("")
            print("Critical Hit!")
            self.yap()

        return target.true_damage(int(damage))
    def yap(self):
        dialogue = random.randint(1, 3)
        if dialogue == 1:
            print("")
            print("Homeless bum: hahaha im gonna steal all your money!")
            print("")
        if dialogue == 2:
            print("")
            print("Homeless bum: prepare to be beaten by the coolest homeless guy in town!")
            print("")
        if dialogue == 3:
            print("")
            print("*the homeless bum makes some homeless noises*")
            print("")
class Priest(Character):
    def attack(self, target):
        damage = self.damage + (self.luck / 5)
        heal = random.randint(1, 50) <= self.luck

        if heal:
            self.health += 5

        return target.take_damage(int(damage))
    def heal(self):
        self.health += random.randint(5 + round(self.luck / 3), 10 + round(self.luck / 3))
# Arena Battle
def arena_battle(player, enemy):

    print(f"\n=== {player.name} vs. {enemy.name} ===")

    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name}: {player.health} HP")
        print(f"{enemy.name}: {enemy.health} HP")

        action = input("Press 1 to attack, press 2 to heal, press 3 to view stats:  ")
        if action == "1":
            dmg = player.attack(enemy)
            print(f"{player.name} hits {enemy.name} for {dmg}")

        elif action == "2":
            old_health = player.health
            player.heal()
            healed = player.health - old_health
            print(f"{player.name} healed for {healed} HP!")
        elif action == "3":
            player.show_stats()
            continue
        elif action == "Open sesame":
            player.max_health += 10000
            player.defense += 10000
            player.luck += 10000
            player.damage += 10000
            player.health += 10000
        else:
            print(" ")
            print("Invalid action >:(")
            continue


        if not enemy.is_alive():
            break
        if not player.is_alive():
            break

        dmg = enemy.attack(player)
        print(f"{enemy.name} hits {player.name} for {dmg}")

        time.sleep(0.3)

    # Declaring the winner
    if player.is_alive():
        print(f"\n{player.name} wins!")
        while True:
            player.reset_health()
            enemy.reset_health()
            replay = input("Do you want to play again? Replaying buffs both you and the enemy. (y/n): ")
            if replay == "y":
                enemy.max_health += random.randint(5, 8)
                enemy.defense += random.randint(1, 3)
                enemy.damage += random.randint(3, 5)
                player.max_health += 5
                player.luck += random.randint(3, 4)
                player.reset_health()
                enemy.reset_health()
                time.sleep(0.1)

                stats = input("Choose 1 stat to boost. 1 for health, 2 for damage, 3 for luck. ")
                if stats == "1":
                    player.health += 5
                    enemy.health += 2
                elif stats == "2":
                    player.damage += 3
                    enemy.damage += 2
                elif stats == "3":
                    player.luck += 3
                    enemy.luck += 1
                else:
                    print("No stat boost for you then >:(")

                arena_battle(player, enemy)
            if replay == "n":
                exit()



    if enemy.is_alive():
        print(f"\n{enemy.name} wins!")
        return False


def Main(player, enemy):
    print(f"Welcome, {playername}, to Fighting Game!")
    print("")
    input("Press Enter To Continue")
    arena_battle(player, enemy)

def start():
    while True:
        playername = input("Enter your name: ")
        if len(playername) <= 4:
            print("Please enter a name longer than 4 characters >:(")
            continue
        elif len(playername) > 15:
            print("Name is too long >:(")
            continue
        else:
            break
    return playername
playername = start()
def choose():
    while True:
        character = input("1 for average Joe, 2 for guy with a cool staff")
        if character == "1":
            player = Character(playername, 100, 20, 5, 15)
            Main(player, enemy)
        if character == "2":
            player = Priest(playername, 80, 10, 5, 20)
            Main(player, enemy)
        else:
            print("Please enter a valid option >:(")
            continue
enemy = Rogue("Homeless Bum", 70, 10, 6, 30)
player = choose()
def Main(player, enemy):
    print(f"Welcome, {player.name}, to the Beat Up Homeless People Fighting Game! ")
    print("")
    input("Press Enter to continue")
    arena_battle(player, enemy)

Main(player, enemy)
