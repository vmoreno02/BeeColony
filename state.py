"""This file contains the state classes and transitions."""
"""All times are ints and will be decremented by some int."""

class State:
    """base class, never actually instantiated, wish i could make it abstract"""
    def __init__(self, timer: int =0) -> None:
        self.timer: int = timer

    def update(self) -> None:
        # overridden method
        pass

    def get_timer(self) -> int:
        return self.timer
    
    def set_timer(self, timer: int) -> None:
        self.timer = timer

class RestState(State):
    def __init__(self, timer: int) -> None:
        super().__init__(timer=timer)
        # initialize timer to be a random int between 1 and timeout time

class ExploreState(State):
    def __init__(self, timer: int) -> None:
        super().__init__(timer=timer)
        # initialize timer to explore timer

class AssessState(State):
    def __init__(self, timer: int) -> None:
        super().__init__(timer=timer)
        # assess timer

class DanceState(State):
    def __init__(self, timer: int) -> None:
        super().__init__(timer=timer)
        # time spent dancing

class TravelState(State):
    """another abstract class for the 4 travel states"""
    def __init__(self) -> None:
        super().__init__()

class TravelRestState(TravelState):
    def __init__(self) -> None:
        super().__init__()

class TravelAssessState(TravelState):
    def __init__(self) -> None:
        super().__init__()

class TravelDanceState(TravelState):
    def __init__(self) -> None:
        super().__init__()

class TravelSiteState(TravelState):
    def __init__(self) -> None:
        super().__init__()