from datetime import datetime
from typing import Optional

from sqlalchemy import extract

from backend.app.model.match import EventDTO
from backend.app.common.utils import get_current_standard_quarter


def get_current_month_tournament_event() -> Optional[EventDTO]:
    now = datetime.now()
    tournament_event = EventDTO.query.filter(
        EventDTO.type == "tournament",
        extract("year", EventDTO.event_date) == now.year,
        extract("month", EventDTO.event_date) == now.month,
    ).first()

    return tournament_event


def get_current_quarter() -> str:
    today = datetime.now().date()
    year = today.year
    next_tournament = get_current_month_tournament_event()
    offset = 0
    if next_tournament and next_tournament.event_date.day < today.day:
        offset = 1
    standard_quarter = get_current_standard_quarter()
    if offset == 1 and standard_quarter == 4:
        year += 1

    return f"{year}Q{standard_quarter + offset}"
