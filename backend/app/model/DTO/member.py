from __future__ import annotations
from datetime import date, datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import ChoiceType, PhoneNumberType

from backend.app.model import constants
from backend.app.model.DTO.member import MemberDTO
from backend.wsgi import db


class MemberDTO(db.Model):
    TYPES = [
        (constants.MEMBER_TYPE__GUEST, constants.MEMBER_TYPE_LABEL__GUEST),
        (constants.MEMBER_TYPE__NEW, constants.MEMBER_TYPE_LABEL__NEW),
        (constants.MEMBER_TYPE__EXCELLENT, constants.MEMBER_TYPE_LABEL__EXCELLENT),
        (constants.MEMBER_TYPE__SPECIAL, constants.MEMBER_TYPE_LABEL__SPECIAL),
    ]

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(
        "phone", PhoneNumberType(region="KR"), unique=True, nullable=True
    )
    member_type: Mapped[str] = mapped_column(
        "member_type", ChoiceType(TYPES), default="guest"
    )
    is_staff: Mapped[bool] = mapped_column(default=False)

    def __repr__(self):
        return f"<Member {self.nickname}>"


class ScoreRecordDTO(db.Model):
    player_id: Mapped[int] = mapped_column(ForeignKey("member.id"))

    id: Mapped[int] = mapped_column(primary_key=True)
    quarter: Mapped[str]
    record_date: Mapped[date] = mapped_column(default=datetime.now().date())
    player: Mapped[MemberDTO] = relationship()
    score: Mapped[float] = mapped_column(default=0.0)
