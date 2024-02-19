from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app import db


class Player(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[str] = mapped_column(unique=True)

    def __repr__(self):
        return f"<Player {self.nickname}>"


class Match(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    player_1_id: Mapped[int] = mapped_column(ForeignKey("player.id"))
    player_1: Mapped[Player] = relationship()
    player_2_id: Mapped[int] = mapped_column(ForeignKey("player.id"))
    player_2: Mapped[Player] = relationship()
    player_3_id: Mapped[int] = mapped_column(ForeignKey("player.id"))
    player_3: Mapped[Player] = relationship()
    player_4_id: Mapped[int] = mapped_column(ForeignKey("player.id"))
    player_4: Mapped[Player] = relationship()
