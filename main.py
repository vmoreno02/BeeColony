from .world import World
from .bee_engine import BeeEngine
from threading import Timer

def main():
    msg = "hello world"
    print(msg)

    world = World()
    engine = BeeEngine(world=world)

    def timed_update():
        engine.update()
        Timer(1, timed_update).start()
    
    timed_update()


if __name__ == '__main__':
    main()

