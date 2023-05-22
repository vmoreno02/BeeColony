"""Properties of the world"""
"""Sets up world but doesn't do much else, all calculations happen in other places"""

from typing import List, Tuple
from .bee import Bee, REST_TIMER
from .bee_site import Site
import random

# constants
NUM_BEES = 15
NUM_SITES = 5
MAX_LENGTH = 25
MIN_LENGTH = -25
BAD_SITE = 2

class World:
    def __init__(self) -> None:
        self.bees : set() = self.create_bees()
        self.sites : List[Site] =  []#self.create_sites()

    def create_bees(self) -> set():
        bees = set()
        for i in range(NUM_BEES):
            time = random.randint(1, REST_TIMER)
            # TODO: fix position, figure out how bees are situated at colony
            bee = Bee(time, None, None, i)
            bees.add(bee)

        return bees
    
    def create_sites(self) -> List[Site]:
        sites = []
        positions = self.get_rand_positions()

        for pos in positions:
            site = Site(pos=pos, quality=BAD_SITE)
            sites.append(site)

        # make one site really good
        good_site : Site = sites[0]
        good_site.set_quality(10)

        return sites

    def get_rand_positions(self) -> List:
        # TODO: implement for a circle of sites around the colony
        return []


