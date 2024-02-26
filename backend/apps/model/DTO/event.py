from datetime import date, datetime

from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import ChoiceType

from apps.model import constants
from apps.model.db import db
from apps.model.DTO.member import MemberDTO


class EventDTO(db.Model):
    __tablename__ = "event"

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
    event_type: Mapped[str] = mapped_column(
        "event_type", ChoiceType(TYPES), default="regular"
    )
    status: Mapped[str] = mapped_column(
        "status", ChoiceType(STATUS_TYPES), default="not_started"
    )
    participants: Mapped[set[MemberDTO]] = relationship(
        "MemberDTO", secondary=event_member_association
    )
