"""This class contains the behavior for each individual bee."""

from .state import State, RestState, AssessState, ExploreState, DanceState, TravelAssessState, TravelDanceState, TravelRestState, TravelSiteState
from typing import Tuple

# constants
REST_TIMER = 10
EXPLORE_TIMER = 20
DANCE_TIMER = 5
ASSESS_TIMER = 10

class Bee:
    def __init__(self, time: int, position: Tuple(int, int), vector = Tuple(int, int)) -> None:
        self.state : State = RestState(timer=time) # each bee begins in rest state
        self.position = position
        self.vector = vector

    def set_state(self, state : State) -> None:
        self.state = state

    def update(self) -> None:
        self.state.update()

