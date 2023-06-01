from state.bee_engine import BeeEngine
from world.world import World
from threading import Timer
import random, math

def main():
    world = World()
    engine = BeeEngine(world=world)

    def timed_update():
        engine.update()
        Timer(1, timed_update).start()
    
    #timed_update()


if __name__ == '__main__':
    main()
    #print(random.uniform(0, 2 * math.pi))

