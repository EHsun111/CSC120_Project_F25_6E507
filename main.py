import random

game_name = "Blasting"
print(f"Welcome to {game_name}!")
print(f"{'=' * (12 + len(game_name))}")

name = input("Enter your character's name: ")
print(f"Hello, {name}! Let's begin your journey.")

player = {
    'name': name,
    'health': 100,
    'coin': 0
}

events = ["find a coin", "meet a monster", "do nothing"]
event = random.choice(events)
print(f"While exploring, you {event}!")

if event == "find a coin":
    player['coin'] += 1
    print(f"{player['name']} found a coin, {player['name']} now has {player['coin']} coins.")
elif event == "meet a monster":
    player['health'] -= 10
    print(f"{player['name']} got hurt during the combat with monster, health is now {player['health']}.")
elif event == "do nothing":
    pass
