# global scope
enemies = 1

def new_enemies():
    global enemies
    enemies += 1
    print(f"Inside Enemies: {enemies}")

new_enemies()
print(f"Outside Enemies: {enemies}")