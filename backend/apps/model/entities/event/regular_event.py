from apps.model.entities.event.event import Event
from apps.model.entities.match.match import Match


class RegularEvent(Event):
    def create_matches(self) -> list[Match]:
        self.participants
