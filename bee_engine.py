"""Controller for all bees"""

from .bee import Bee
from .world import World
from .bee_site import Site
from typing import List

class BeeEngine:
    def __init__(self, world: World) -> None:
        self.world = world
        self.bees : set(Bee) = world.bees
        self.sites : List[Site] = world.sites

    def update(self) -> None:
        for bee in self.bees:
            bee.update()