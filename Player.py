
#Player 

class Player:

    def __init__(self):
        self.name = ""
        self.job = ""
        self.light = False
        self.action=""
        self.visited_rooms = []
        self.saved_all_children = False
        self.fought_imperials = False
        self.num_rooms_explored = 1
        self.current_room = 0

    def set_job(self, job):
        self.job = job
        match self.job:
            case "swordlord":
                self.job="swordlord"
            case "rogue":
                self.job="rogue"
            case "pugilist":
                self.job="pugilist"

    def add_visited_room(self,room_index):
        if room_index not in self.visited_rooms:
            self.visited_rooms.append(room_index)
        else:
            pass
class Item:
    def __init__(self, name="", description=""):
        self.name = name
        self.description = description