"""This file contains the state classes and transitions."""
"""All times are ints and will be decremented by some int."""
"""Use of the State Pattern prevents the need for a giant transition function or storing prev state"""
"""Use of the Observer Pattern for access to the Bee that is using the state"""

# constants
REST_TIMER = 10
EXPLORE_TIMER = 20
DANCE_TIMER = 5
ASSESS_TIMER = 10

class State:
    """base class, never actually instantiated, wish i could make it abstract"""
    def __init__(self, observer, timer: int =0) -> None:

        self.timer: int = timer
        self.observer = observer

    def update(self) -> None:
        # overridden method
        pass

    def get_timer(self) -> int:
        return self.timer
    
    def set_timer(self, timer: int) -> None:
        self.timer = timer

    def transition(self) -> None:
        # overridden method so that transition logic is disseminated over all states
        pass

class RestState(State):
    def __init__(self, observer, timer: int) -> None:
        super().__init__(observer=observer, timer=timer)
        # initialize timer to be a random int between 1 and timeout time
        print("bee no. " + str(self.observer.id) + " is in rest state")
        # booleans for transition function
        self.to_travel_assess = False
        self.to_explore = False

    def update(self) -> None:
        # decrement timer and watch dancing bees
        self.timer -= 1
        if self.timer <= 0:
            # if not already moving to assess, go to explore
            self.to_explore = True
            self.transition()

        else:
            if self.observer.coin_heads:
                self.observer.coin_heads = False
                self.to_travel_assess = True
                self.transition()

    def transition(self) -> None:
        # from rest: explore or travel assess
        self.observer.notify_not_rest()

        if self.to_explore:
            self.observer.set_state(ExploreState(observer=self.observer, timer=EXPLORE_TIMER))
            
        elif self.to_travel_assess:
            self.observer.set_state(TravelAssessState(observer=self.observer))

        else:
            # error
            print("Error in transition from rest")
            exit()

class ExploreState(State):
    def __init__(self, observer, timer: int) -> None:
        super().__init__(observer=observer, timer=timer)
        # initialize timer to explore timer
        print("bee no. " + str(self.observer.id) + " is in explore state")
        # booleans for transition function
        self.to_travel_rest = False
        self.to_assess = False

    def update(self) -> None:
        # decrement timer and check if site is in range
        self.timer -= 1
        if self.timer <= 0:
            # go to travel rest
            self.to_travel_rest = True
            self.transition()

        else:
            # if there is a chosen site, assess it
            if self.observer.chosen_site:
                self.to_assess = True
                self.transition()

    def transition(self) -> None:
        # from explore: assess and travel rest
        if self.to_assess:
            self.observer.set_state(AssessState(self.observer, ASSESS_TIMER))
        
        elif self.to_travel_rest:
            self.observer.set_state(TravelRestState(self.observer))

        else:
            # error
            print("Error in transition from explore")
            exit()

class AssessState(State):
    def __init__(self, observer, timer: int) -> None:
        super().__init__(observer=observer, timer=timer)
        # assess timer
        print("bee no. " + str(self.observer.id) + " is in assess state")
        # no bools needed, only one transition

    def update(self) -> None:
        # getting quality of site and num times to do dance done elsewhere
        # decrement timer
        self.timer -= 1
        if self.timer <= 0:
            self.transition()

    def transition(self) -> None:
        # from assess: travel dance
        self.observer.set_state(TravelDanceState(self.observer))

class DanceState(State):
    def __init__(self, observer, timer: int) -> None:
        super().__init__(observer=observer, timer=timer)
        # time spent dancing
        print("bee no. " + str(self.observer.id) + " is in dance state")
        self.to_rest = False
        self.to_travel_site = False

    def update(self) -> None:
        # decrement timer and check num cycles
        self.timer -= 1
        if self.timer <= 0:
            if self.observer.num_dance_cycles > 0:
                self.observer.num_dance_cycles -= 1
                self.to_travel_site = True
            else:
                self.to_rest = True

            self.transition()

    def transition(self) -> None:
        self.observer.notify_not_dance()
        
        if self.to_rest:
            self.observer.set_state(RestState(self.observer, REST_TIMER))

        elif self.to_travel_site:
            self.observer.set_state(TravelSiteState(self.observer))

        else:
            # error
            print("Error in transition from dance")
            exit()

class TravelState(State):
    """another abstract class for the 4 travel states"""
    def __init__(self, observer) -> None:
        super().__init__(observer=observer)

class TravelRestState(TravelState):
    def __init__(self, observer) -> None:
        super().__init__(observer)

    def update(self) -> None:
        # if hub is within sensor reading, transition
        if self.observer.find_hub():
            self.transition()

    def transition(self) -> None:
        self.observer.set_state(RestState(self.observer, REST_TIMER))

class TravelAssessState(TravelState):
    def __init__(self, observer) -> None:
        super().__init__(observer)

    def update(self) -> None:
        # if site is within sensor reading, transition
        if self.observer.find_target_site():
            self.transition()

    def transition(self) -> None:
        self.observer.set_state(AssessState(self.observer, ASSESS_TIMER))

class TravelDanceState(TravelState):
    def __init__(self, observer) -> None:
        super().__init__(observer)

    def update(self) -> None:
        # if hub is within sensor reading, transition
        if self.observer.find_hub():
            self.transition()

    def transition(self) -> None:
        self.observer.set_state(DanceState(self.observer, DANCE_TIMER))

class TravelSiteState(TravelState):
    def __init__(self, observer) -> None:
        super().__init__(observer)

    def update(self) -> None:
        # if site is within sensor reading, transition
        if self.observer.find_target_site():
            self.transition()

    def transition(self) -> None:
        self.observer.set_state(AssessState(self.observer, ASSESS_TIMER))