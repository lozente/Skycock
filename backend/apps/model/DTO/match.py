from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import ChoiceType

from apps.model import constants
from apps.model.db import db
from apps.model.DTO.event import EventDTO
from apps.model.DTO.member import MemberDTO


class MatchDTO(db.Model):
    __tablename__ = "match"

    TYPES = [
        (constants.MATCH_TYPE__NORMAL, constants.MATCH_TYPE_LABEL__NORMAL),
        (constants.MATCH_TYPE__RANKED, constants.MATCH_TYPE_LABEL__RANKED),
        (constants.MATCH_TYPE__EXTRA, constants.MATCH_TYPE_LABEL__EXTRA),
    ]
    STATUS_TYPES = [
        (
            constants.MATCH_STATUS_TYPE__NOT_STARTED,
            constants.MATCH_STATUS_TYPE_LABEL__NOT_STARTED,
        ),
        (
            constants.MATCH_STATUS_TYPE__IN_PROGRESS,
            constants.MATCH_STATUS_TYPE_LABEL__IN_PROGRESS,
        ),
        (
            constants.MATCH_STATUS_TYPE__FINISHED,
            constants.MATCH_STATUS_TYPE_LABEL__FINISHED,
        ),
        (
            constants.MATCH_STATUS_TYPE__CANCELLED,
            constants.MATCH_STATUS_TYPE_LABEL__CANCELLED,
        ),
    ]

    team_1_player_1_id: Mapped[int] = mapped_column(ForeignKey("member.id"))
    team_1_player_2_id: Mapped[int] = mapped_column(
        ForeignKey("member.id"), nullable=True
    )
    team_2_player_1_id: Mapped[int] = mapped_column(ForeignKey("member.id"))
    team_2_player_2_id: Mapped[int] = mapped_column(
        ForeignKey("member.id"), nullable=True
    )
    event_id: Mapped[int] = mapped_column(ForeignKey("event.id"))

    id: Mapped[int] = mapped_column(primary_key=True)
    team_1_player_1: Mapped[MemberDTO] = relationship(
        "MemberDTO", foreign_keys=[team_1_player_1_id]
    )
    team_1_player_2: Mapped[MemberDTO] = relationship(
        "MemberDTO", foreign_keys=[team_1_player_2_id]
    )
    team_2_player_1: Mapped[MemberDTO] = relationship(
        "MemberDTO", foreign_keys=[team_2_player_1_id]
    )
    team_2_player_2: Mapped[MemberDTO] = relationship(
        "MemberDTO", foreign_keys=[team_2_player_2_id]
    )
    event: Mapped[EventDTO] = relationship()
    round: Mapped[int] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
    started_at: Mapped[datetime] = mapped_column(nullable=True)
    ended_at: Mapped[datetime] = mapped_column(nullable=True)
    team_1_score: Mapped[int] = mapped_column(nullable=True)
    team_2_score: Mapped[int] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(
        "status", ChoiceType(STATUS_TYPES), default="not_started"
    )
    match_type: Mapped[str] = mapped_column(
        "match_type", ChoiceType(TYPES), default="normal"
    )
