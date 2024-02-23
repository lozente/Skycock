from __future__ import annotations
from datetime import date, datetime

from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import ChoiceType

from backend.app import db
from backend.app.model.member import Member


class Event(db.Model):
    TYPES = [
        ("regular", "정기모임"),
        ("tournament", "스콕대전"),
        ("etc", "기타"),
    ]
    STATUS_TYPES = [
        ("not_started", "준비중"),
        ("finished", "완료됨"),
        ("cancelled", "취소됨"),
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
    participants: Mapped[set[Member]] = relationship(
        "Member", secondary=event_member_association
    )


class Match(db.Model):
    STATUS_TYPES = [
        ("not_started", "대기중"),
        ("in_progress", "진행중"),
        ("finished", "완료됨"),
        ("cancelled", "취소됨"),
    ]
    TYPES = [
        ("normal", "일반"),
        ("ranked", "시드"),
        ("extra", "번외"),
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
    team_1_player_1: Mapped[Member] = relationship(
        "Member", foreign_keys=[team_1_player_1_id]
    )
    team_1_player_2: Mapped[Member] = relationship(
        "Member", foreign_keys=[team_1_player_2_id]
    )
    team_2_player_1: Mapped[Member] = relationship(
        "Member", foreign_keys=[team_2_player_1_id]
    )
    team_2_player_2: Mapped[Member] = relationship(
        "Member", foreign_keys=[team_2_player_2_id]
    )
    event: Mapped[Event] = relationship()
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
