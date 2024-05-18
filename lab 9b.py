#Brenda Castañeda 

from numpy import random, mean

#agents
class Agent():
    def __init__(self, color, pref):
        self.color=color
        self.pref=pref
        pass 

    def move(self):
    #does agent want to move?
        if self.am_i_happy():
            return
        else: 
            self.move_to_new_position()
        pass 

    def am_i_happy(self):
        neighbors=self.locate_neighbors()
    #return boolean for whether an agent is happy its current location
    #uses self.locate_neighbors method
        pass 

    def locate_neighbors(self):
    #given location, return list of all patches that count as neighbors
        pass 

#world
class World():
    def __init__(self, width, length, num_agents):
        self.width = width
        self.length = length
        self.num_agents=num_agents
        self.agents = self.build_agents()
        self.grid=self.build_grid()
    
    def build_grid(self):
        #sets up world agents can move in, returning a dict
        grid={}
        for x in range(self.width):
            for y in range(self.length):
                grid[(x,y)]=None 
            return grid
    
    def build_agents(self):
        #generates list of agents that can be iterated over
        agents = []
        for _ in range(self.num_agents):
            agent=Agent(color=random.choice(["red", "blue"]), 
                        pref=random.choice(["1", "2"]))
            agents.append(agent)
            return agents
        pass 
    def find_vacant(self):
        #find list of empty patches and returns random one
        empty=[patch for patch, agent in self.grid.items() if agent is None]
        if empty:
            return random.choice(empty)
        else:
            return None
        pass 
    def report_integration(self):
        #generates report at end of current round
        pass
    def report (self):
        #generate final report at model end
        pass
    def run (self):
        #execute model as set up
        pass 
    
world = World(width=5, length=5, num_agents=10)
world.run()    

#loop (agents that find empty path; agents move there)

#End