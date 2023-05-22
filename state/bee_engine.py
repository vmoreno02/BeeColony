"""Controller for all bees"""

from world.bee import Bee
from world.world import World
from world.bee_site import Site
from typing import List

QUORUM = 8

class BeeEngine:
    def __init__(self, world: World) -> None:
        self.world = world
        self.bees : set(Bee) = world.bees
        self.sites : List[Site] = world.sites

        # dict of which bees are sponsoring which site
        # site is key and list of bees is value
        self.quorum = {}

        # set of bees in dance state
        self.dancing = set()

        # set of bees in rest state
        self.resting = set()

        for bee in self.bees:
            bee.set_observer(self)

    def update(self) -> None:
        print("update")
        for bee in self.bees:
            bee.update()

    def notify_dance(self, bee: Bee) -> None:
        self.dancing.add(bee)

    def notify_not_dance(self, bee: Bee) -> None:
        self.remove_bee_by_id(bee, self.dancing)

    def notify_rest(self, bee: Bee) -> None:
        self.resting.add(bee)

    def notify_not_rest(self, bee: Bee) -> None:
        self.remove_bee_by_id(bee, self.resting)

    # safeguard in case changing state or position makes the sets wonky
    def remove_bee_by_id(self, bee: Bee, list: set) -> None:
        for b in list:
            if b.id == bee.id:
                list.remove(b)
                break

    def is_in_range_of_site(self, bee: Bee) -> Site:
        # returns true if bee is within a range of a certain radius of the site
        # used only in explore state
        return None
    
    # for each resting bee, coin flip for each dancing bee
    # engine forces state change to travel assess
    def watch_dancers(self) -> None:
        pass