"""Controller for all bees"""

# TODO: implement is_in_range_of_site, find_sites, find_target_site, get_hub, get_site, check_quorum

from world.bee import Bee
from world.world import World
from world.bee_site import Site
from typing import List
import random

QUORUM = 8

class BeeEngine:
    def __init__(self, world: World) -> None:
        self.world = world
        self.bees : set(Bee) = world.bees
        self.sites : List[Site] = world.sites

        # dict of which bees are sponsoring which site
        # site is key and list of bees is value
        self.quorum = {}
        self.largest_quorum = 0

        # set of bees in dance state
        self.dancing = set()

        # set of bees in rest state
        # all bees start in rest state
        self.resting = set(self.bees)

        for bee in self.bees:
            bee.set_observer(self)

    # main method that does things
    # passes on updates to each bee
    # then coin flips for all dancers and checks the quorum
    def update(self) -> None:
        print("update")
        for bee in self.bees:
            bee.update()

        self.watch_dancers()
        self.check_quorum()

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
        for bee in self.resting:
            for b in self.dancing:
                if self.coin_flip():
                    # marks the bee to transition upon next round
                    bee.coin_heads = True
                    break

    # defines math that determines coin flip
    # currently weighted 70% heads and 30% tails
    # TODO: is the coin's weight affected by quality of site??
    def coin_flip(self) -> bool:
        i = random.randint(1, 10)
        return i < 8

    # scan within a certain radius for any sites
    def find_sites(self, bee: Bee) -> bool:
        pass

    # scan within a certain radius for a particular site
    def find_target_site(self, bee: Bee, site: Site) -> bool:
        pass

    # scan within a certain radius for the hub
    def find_hub(self, bee: Bee) -> bool:
        pass

    # calculate vector between bee and hub
    # used in travel_rest and travel_dance states
    def get_hub(self, bee: Bee):
        pass

    # calculate vector between bee and site
    # used in travel_assess and travel_site
    def get_site(self, bee: Bee, site: Site):
        pass

    # check quorum numbers
    def check_quorum(self):
        pass