class Scene(object):
    def enter(self):
        print(f"you are entering a scene{self}")
    
class Engine(object):
    def __init(self,scene_map):
        pass

    def play(self):
        pass

class Death(Scene):
    
    def enter(self):
        pass

class Corridor(Scene):

    def enter(self):
        pass

class Weapon(Scene):
    
    def enter(self):
        pass

class Bridge(Scene):
    
    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):

        pass

class Map(object):

    def __init__(self, start_screen):
        print(f"youv'e entered the {start_screen}")
        pass

    def next_screen(self, scene_name):
        pass
    
    def opening_scene(self):
        pass

a_map = Map('corridor')
a_game = Engine()
a_game.play()

