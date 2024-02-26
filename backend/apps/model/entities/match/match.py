from datetime import datetime

from apps.model.entities.entity import Entity
from apps.model.DTO.event import EventDTO
from apps.model.DTO.member import MemberDTO


class Match(Entity):
    def __init__(
        self,
        id: int,
        team_1_player_1: MemberDTO,
        team_1_player_2: MemberDTO,
        team_2_player_1: MemberDTO,
        team_2_player_2: MemberDTO,
        event: EventDTO,
        round: int,
        created_at: datetime,
        started_at: datetime,
        ended_at: datetime,
        team_1_score: int,
        team_2_score: int,
        status: str,
        match_type: str,
    ) -> None:
        self.id = id
        self.team_1_player_1 = team_1_player_1
        self.team_1_player_2 = team_1_player_2
        self.team_2_player_1 = team_2_player_1
        self.team_2_player_2 = team_2_player_2
        self.event = event
        self.round = round
        self.created_at = created_at
        self.started_at = started_at
        self.ended_at = ended_at
        self.team_1_score = team_1_score
        self.team_2_score = team_2_score
        self.status = status
        self.match_type = match_type
