import time
import os
import random
import msvcrt
  
# Game settings
WIDTH = 40
HEIGHT = 10
DINO_X = 5
JUMP_HEIGHT = 3

# Game state
dino_y = 0
velocity = 0
is_jumping = False
obstacle_x = WIDTH - 1
score = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_frame(dino_y, obstacle_x, score):
    clear_screen()
    for y in range(HEIGHT):
        line = ""
        for x in range(WIDTH):
            if x == DINO_X and y == HEIGHT - 2 - dino_y:
                line += "O"
            elif x == obstacle_x and y == HEIGHT - 2:
                line += "||||"
            elif y == HEIGHT - 1:
                line += "_"
            else:
                line += " "
        print(line)
    print(f"Score: {score}")

def update_jump():
    global dino_y, velocity, is_jumping
    if is_jumping:
        dino_y += velocity
        velocity -= 1
        if dino_y <= 0:
            dino_y = 0
            is_jumping = False
            velocity = 0

def check_collision():
    return dino_y == 0 and obstacle_x == DINO_X

def main():
    global obstacle_x, is_jumping, velocity, score

    print("Press SPACE to jump. Press Q to quit.")
    time.sleep(4)

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b' ' and not is_jumping:
                is_jumping = True
                velocity = JUMP_HEIGHT
            elif key == b'q':
                break

        update_jump()

        if obstacle_x == 0:
            obstacle_x = random.randint(WIDTH - 10, WIDTH - 1)
            score += 1
        else:
            obstacle_x -= 1

        draw_frame(dino_y, obstacle_x, score)

        if check_collision():
            print("\nGame Over!")
            break

        time.sleep(0.1)

if __name__ == "__main__":
    main()
