import random

game_name = "Blasting"
print(f"Welcome to {game_name}!")
print(f"{'=' * (12 + len(game_name))}")

name = "Tester"
print(f"Hello, {name}! Let's begin your journey.")

player = {
    'name': name,
    'health': 100,
    'coin': 0,
    'x': 0,
    'y': 0
}

events = ["find a coin", "meet a monster", "do nothing"]
map_size = 9

def check_event():
    global events, player
    event = random.choice(events)
    if event == "find a coin":
        player['coin'] += 1
    elif event == "meet a monster":
        player['health'] -= 10

def draw_ui(x, y):
    print("=" * 25)
    for i in range(map_size):
        for j in range(map_size):
            if i == y and j == x:
                print("C", end="  ")
            elif i == map_size - 1 and j == map_size - 1:
                print("M", end="  ")
            else:
                print(".", end="  ")
        print()
    print("=" * 25)
    print(f"Health: {player['health']}")
    print(f"Coin: {player['coin']}")
    print("=" * 25)

def move(direction):
    if direction == 'w' and player['y'] > 0:
        player['y'] -= 1
    elif direction == 'a' and player['x'] > 0:
        player['x'] -= 1
    elif direction == 's' and player['y'] < map_size - 1:
        player['y'] += 1
    elif direction == 'd' and player['x'] < map_size - 1:
        player['x'] += 1
    else:
        print("You cannot move that way!")

def main():
    draw_ui(player['x'], player['y'])
    direction = input("Your next move (w/a/s/d/q): ")
    while direction != 'q':
        move(direction)
        if player['x'] == map_size - 1 and player['y'] == map_size - 1:
            print("Congratulations! You reach the gate for next level.")
            break
        check_event()
        draw_ui(player['x'], player['y'])
        direction = input("Your next move (w/a/s/d/q): ")

if __name__ == "__main__":
    main()
