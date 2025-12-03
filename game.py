import random

class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.health = 100
        self.coin = 0
        self.x = 0
        self.y = 0

    def move(self, direction, map_size):
        if direction == "s" and self.x < map_size - 1:
            self.x += 1
        elif direction == "d" and self.y < map_size - 1:
            self.y += 1
        elif direction == "w" and self.x > 0:
            self.x -= 1
        elif direction == "a" and self.y > 0:
            self.y -= 1
        else:
            print("You cannot move that way!")

class GameMap:
    def __init__(self, size=9):
        self.size = size

    def draw(self, player):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if i == player.x and j == player.y:
                    row.append("C")
                elif i == self.size - 1 and j == self.size - 1:
                    row.append("M")
                else:
                    row.append(".")
            print(" ".join(row))
        print(f"Health: {player.health}")
        print(f"Coin: {player.coin}")

class Game:
    def __init__(self):
        self.game_name = "Blasting"
        self.name = "Tester"
        self.events = ["find a coin", "meet a monster", "do nothing"]
        self.player = Player()
        self.map = GameMap()
        self.map_size = self.map.size

    def check_event(self):
        event = random.choice(self.events)
        if event == "find a coin":
            self.player.coin += 1
        elif event == "meet a monster":
            self.player.health -= 10

    def play(self):
        self.map.draw(self.player)
        direction = input("Your next move (w/a/s/d/q): ")
        while direction != "q":
            self.player.move(direction, self.map_size)
            if self.player.x == self.map_size - 1 and self.player.y == self.map_size - 1:
                print("Congratulations! You reach the gate for next level.")
                break
            self.check_event()
            self.map.draw(self.player)
            direction = input("Your next move (w/a/s/d/q): ")

if __name__ == "__main__":
    Game().play()
