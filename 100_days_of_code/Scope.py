# # global scope
# enemies = 1

# def new_enemies(enemy):
#     # global enemies
#     # enemies += 1
#     print(f"Inside Enemies: {enemies}")
#     return enemy + 1

# ne = new_enemies(enemies)
# print(ne)
# print(f"Outside Enemies: {enemies}")

# Global constants
PI = 3.14159
GOOGLE_URL = "www.google.com"

# def my_func():
#     print(GOOGLE_URL)

# my_func()

def a_function(a_parameter):
    a_variable = 15
    return a_parameter
 
a_function(10)
print(a_variable)