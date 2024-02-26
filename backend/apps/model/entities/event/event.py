from __future__ import annotations
from abc import abstractmethod
from datetime import date

from apps.model.DTO.event import EventDTO
from apps.model.DTO.member import MemberDTO
from apps.model.entities.entity import Entity
from apps.model.entities.match.match import Match
from apps.model.entities.member.member import Member


class Event(Entity):
    dto_class = EventDTO

    def __init__(
        self,
        id: int,
        event_date: date,
        event_type: str,
        status: str,
        participants: set[MemberDTO],
    ) -> None:
        self.id = id
        self.event_date = event_date
        self.event_type = event_type
        self.status = status
        participants_list = [Member.from_dto(memberDTO) for memberDTO in participants]
        self.participants = set(participants_list)

    @abstractmethod
    def create_matches() -> list[Match]:
        pass
