from __future__ import annotations
from datetime import date, datetime

from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import ChoiceType

from backend.app.model import constants
from backend.app.model.member import MemberDTO
from backend.wsgi import db


class EventDTO(db.Model):
    TYPES = [
        (constants.EVENT_TYPE__REGULAR, constants.EVENT_TYPE_LABEL__REGULAR),
        (constants.EVENT_TYPE__TOURNAMENT, constants.EVENT_TYPE_LABEL__TOURNAMENT),
        (constants.EVENT_TYPE__ETC, constants.EVENT_TYPE_LABEL__ETC),
    ]
    STATUS_TYPES = [
        (
            constants.EVENT_STATUS_TYPE__NOT_STARTED,
            constants.EVENT_STATUS_TYPE_LABEL__NOT_STARTED,
        ),
        (
            constants.EVENT_STATUS_TYPE__IN_PROGRESS,
            constants.EVENT_STATUS_TYPE_LABEL__IN_PROGRESS,
        ),
        (
            constants.EVENT_STATUS_TYPE__FINISHED,
            constants.EVENT_STATUS_TYPE_LABEL__FINISHED,
        ),
        (
            constants.EVENT_STATUS_TYPE__CANCELLED,
            constants.EVENT_STATUS_TYPE_LABEL__CANCELLED,
        ),
    ]
    event_member_association = Table(
        "event_member_association",
        db.Model.metadata,
        Column("event_id", ForeignKey("event.id")),
        Column("member_id", ForeignKey("member.id")),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    event_date: Mapped[date] = mapped_column(default=datetime.now().date())
    type: Mapped[str] = mapped_column("type", ChoiceType(TYPES), default="regular")
    status: Mapped[str] = mapped_column(
        "status", ChoiceType(STATUS_TYPES), default="not_started"
    )
    participants: Mapped[set[MemberDTO]] = relationship(
        "Member", secondary=event_member_association
    )


class MatchDTO(db.Model):
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
        "Member", foreign_keys=[team_1_player_1_id]
    )
    team_1_player_2: Mapped[MemberDTO] = relationship(
        "Member", foreign_keys=[team_1_player_2_id]
    )
    team_2_player_1: Mapped[MemberDTO] = relationship(
        "Member", foreign_keys=[team_2_player_1_id]
    )
    team_2_player_2: Mapped[MemberDTO] = relationship(
        "Member", foreign_keys=[team_2_player_2_id]
    )
    event: Mapped[EventDTO] = relationship()
    created_at: Mapped[datetime] = mapped_column()
    started_at: Mapped[datetime] = mapped_column(nullable=True)
    ended_at: Mapped[datetime] = mapped_column(nullable=True)
    team_1_score: Mapped[int] = mapped_column(nullable=True)
    team_2_score: Mapped[int] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(
        "status", ChoiceType(STATUS_TYPES), default="not_started"
    )
    type: Mapped[str] = mapped_column("type", ChoiceType(TYPES), default="normal")
    is_score_counted: Mapped[bool] = mapped_column(default=False)
