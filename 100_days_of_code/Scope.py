# global scope
enemies = 1

def new_enemies(enemy):
    # global enemies
    # enemies += 1
    print(f"Inside Enemies: {enemies}")
    return enemy + 1

ne = new_enemies(enemies)
print(ne)
print(f"Outside Enemies: {enemies}")