from __future__ import annotations
from datetime import date

from backend.app.model.DTO.member import MemberDTO
from backend.app.model.entities.entity import Entity
from backend.app.model.entities.member.member import Member


class Event(Entity):
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
