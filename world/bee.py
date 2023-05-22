"""This class contains the behavior for each individual bee."""

from state.state import State, RestState, AssessState, ExploreState, DanceState, TravelAssessState, TravelDanceState, TravelRestState, TravelSiteState
from state.bee_engine import BeeEngine
from bee_site import Site
from typing import Tuple

# constants
REST_TIMER = 10
EXPLORE_TIMER = 20
DANCE_TIMER = 5
ASSESS_TIMER = 10

class Bee:
    def __init__(self, time: int, position, vector, id: int) -> None:
        self.state : State = RestState(observer=self, timer=time) # each bee begins in rest state
        self.position = position
        self.vector = vector
        self.chosen_site : Site = None # once the quorum num of bees have the same site as the chosen site, end simulation
        self.observer : BeeEngine = None # observer will be the engine
        self.id = id

        self.num_dance_cycles = 0 # determined by quality of site and in assess state
        self.has_assessed = False # used to prevent dance cycles from going on forever
        self.coin_heads = False # used to force a resting bee to go to site

    def set_observer(self, observer : BeeEngine) -> None:
        self.observer = observer

    def set_state(self, state : State) -> None:
        self.state = state

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

    def explore(self) -> None:
        # used to move the bee as it explores
        # finds a 90 degree range with current vector in the middle
        # picks random vector in that range
        # moves forward 1 unit
        # also checks if in range of site and if so sets chosen site
        pass

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

    def rest(self) -> None:
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

    def notify_not_rest(self):
        self.observer.notify_not_rest(self)

    def notify_not_dance(self):
        self.observer.notify_not_dance(self)
