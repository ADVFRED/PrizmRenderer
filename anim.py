import renderer 
from delayer import delay as delar
class screen():
    def __init__(self):
        cors=[]
        self.cors=cors
    def add_coords(self,coords):
        if str(type(coords))== "<class 'tuple'>":
            self.cors.append(coords)
        elif str(type(coords))=="<class 'list'>":
            for cord in coords:
                self.cors.append(cord)
    def send_coords(self,coords):
        renderer.set_chars(coords) 
    def cls(self):
        renderer.ResetMatrice()

        self.cors=[]
    def get_to_rend(self):
        return renderer.render_screen()
    def render(self):
        """outward facing meth. for full rend. process"""
        self.send_coords(self.cors)
        print(self.get_to_rend())
        self.cls()
   
game=screen()
def anim():    
    #delar(7)
    game.add_coords([(4,4,'A')])
    game.render()
    game.cls()
    print("#############")
    delar(4)    
    game.add_coords([(7,7,'A')])
    game.render()
    
anim()
