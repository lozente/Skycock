from backend.wsgi import db
from backend.app.matches.match_maker import REGULAR_EVENT_MATCH_MAKING_MAP_BY_RANK
from backend.app.member import apis as member_apis
from backend.app.model import constants
from backend.app.model.DTO.event import EventDTO
from backend.app.model.DTO.match import MatchDTO


def create_event(
    event_type: str, event_status: str, participant_ids: list[int]
) -> EventDTO:
    new_event = EventDTO()
    new_event.event_type = event_type
    new_event.status = event_status
    new_event.participants = member_apis.get_members_by_ids(participant_ids)

    db.session.add(new_event)
    db.session.commit()

    return new_event


def create_matches(event: EventDTO) -> list[MatchDTO]:
    if event.event_type == constants.EVENT_TYPE__REGULAR:
        pass
    else:
        raise NotImplementedError("Non-regular event match creation is not implemented")
