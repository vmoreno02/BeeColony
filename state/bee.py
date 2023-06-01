"""This class contains the behavior for each individual bee."""
"""Use of the Observer Pattern for access to the BeeEngine"""
"""Does not interact with any other bees"""

# TODO: implement moving functions

from state.state import State, RestState, AssessState, ExploreState, DanceState, TravelAssessState, TravelDanceState, TravelRestState, TravelSiteState
from state.state import REST_TIMER, ASSESS_TIMER, DANCE_TIMER, EXPLORE_TIMER
#from state.bee_engine import BeeEngine
from world.bee_site import Site
from world.vector import Vector
from typing import Tuple
import random, math


class Bee:
    def __init__(self, time: int, position, vector: Vector, id: int) -> None:
        self.position = position
        self.vector : Vector = vector
        self.chosen_site : Site = None # once the quorum num of bees have the same site as the chosen site, end simulation
        self.observer = None # observer will be the engine
        self.id = id

        self.num_dance_cycles = 0 # determined by quality of site and in assess state
        self.has_assessed = False # used to prevent dance cycles from going on forever
        self.coin_heads = False # used to force a resting bee to go to site

        self.state : State = RestState(observer=self, timer=time) # each bee begins in rest state


    def set_observer(self, observer) -> None:
        self.observer = observer

    def set_state(self, state : State) -> None:
        self.state = state

    # main method that is called every second
    # updates each state and then acts according to cur state
    def update(self) -> None:
        self.state.update()

        if isinstance(self.state, ExploreState):
            self.explore()

        elif isinstance(self.state, RestState):
            self.rest()

        elif isinstance(self.state, AssessState):
            self.assess()

        elif isinstance(self.state, DanceState):
            self.dance()

        elif isinstance(self.state, TravelAssessState):
            self.travel_assess()

        elif isinstance(self.state, TravelDanceState):
            self.travel_dance()

        elif isinstance(self.state, TravelRestState):
            self.travel_rest()

        elif isinstance(self.state, TravelSiteState):
            self.travel_site()

        print("new position: " + str(self.position))

    def explore(self) -> None:
        # used to move the bee as it explores
        # finds a 90 degree range with current vector in the middle
        # picks random vector in that range
        # moves forward 1 unit
        # also checks if in range of site and if so sets chosen site

        if self.position != (0, 0):
            vec = self.get_rand_direction()
            self.vector = self.vector.add(vec)            

        x, y = self.vector.get_cartesian()
        self.position = (x, y)

        site = self.observer.find_sites(self)
        if site:
            self.chosen_site = site

    def dance(self) -> None:
        if self.state.get_timer() == DANCE_TIMER:
            self.observer.notify_dance(self)
    
    def assess(self) -> None:
        if self.state.get_timer() == ASSESS_TIMER and not self.has_assessed:
            # hard coded for now, will change later
            if self.chosen_site.get_quality() >= 8:
                self.num_dance_cycles = 3

            elif self.chosen_site.get_quality() >= 5:
                self.num_dance_cycles = 2

            else:
                self.num_dance_cycles = 1

            self.has_assessed = True
            # quorum stuff here

    def rest(self) -> None:
        if self.state.get_timer() == REST_TIMER:
            self.observer.notify_rest(self)

    def travel_site(self) -> None:
        # move to site
        pass

    def travel_dance(self) -> None:
        # move to hub
        pass

    def travel_assess(self) -> None:
        # move to site
        pass

    def travel_rest(self) -> None:
        # move to hub
        pass

    def get_rand_direction(self):
        r1 = self.vector.r - (math.pi / 4) # 45 degrees
        r2 = self.vector.r + (math.pi / 4) # total range 90 degrees

        angle = random.uniform(r1, r2)

        return Vector(1, angle)

    def notify_not_rest(self):
        self.observer.notify_not_rest(self)

    def notify_not_dance(self):
        self.observer.notify_not_dance(self)

    # check if there's a site nearby
    def find_sites(self):
        return self.observer.find_sites(self)
    
    # check if the target site is nearby
    def find_target_site(self):
        return self.observer.find_target_site(self, self.chosen_site)
    
    # check if hub is nearby
    def find_hub(self):
        return self.observer.find_hub(self)
    
    # found a site to add to the quorum count
    def add_site_to_quorum(self):
        self.observer.add_site_to_quorum(self, self.chosen_site)
    
    # prints bee's data for testing
    def print_bee(self):
        s = "Bee no." + str(self.id)
        s = s + ", position: " + str(self.position)
        s = s + " , vector: " + self.vector.print()
        s = s + ", state: " + str(type(self.state))
        print(s)
