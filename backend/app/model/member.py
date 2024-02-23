from __future__ import annotations
from datetime import date, datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import ChoiceType, PhoneNumberType

from backend.app import db
from backend.app.model.member import Member


class Member(db.Model):
    TYPES = [
        ("guest", "게스트"),
        ("new", "신규회원"),
        ("excellent", "우수회원"),
        ("special", "특별회원"),
    ]

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(
        "phone", PhoneNumberType(region="KR"), unique=True, nullable=True
    )
    type: Mapped[str] = mapped_column("type", ChoiceType(TYPES), default="guest")
    is_staff: Mapped[bool] = mapped_column(default=False)

    def __repr__(self):
        return f"<Member {self.nickname}>"


class ScoreRecord(db.Model):
    player_id: Mapped[int] = mapped_column(ForeignKey("member.id"))

    id: Mapped[int] = mapped_column(primary_key=True)
    quarter: Mapped[str]
    record_date: Mapped[date] = mapped_column(default=datetime.now().date())
    player: Mapped[Member] = relationship()
    score: Mapped[float] = mapped_column(default=0.0)
